"""Familia "Drawdown": drawdown_series, max_drawdown, time_under_water, recovery_time."""

from __future__ import annotations

import numpy as np
import pandas as pd


def drawdown_series(returns: pd.Series | pd.DataFrame) -> pd.Series | pd.DataFrame:
    """Serie de drawdown: caída porcentual respecto al máximo acumulado previo.

    drawdown_t = valor_t / max(valor_0..t) - 1, con valor = rentabilidad acumulada.
    """
    wealth = (1.0 + returns).cumprod()
    running_max = wealth.cummax()
    return wealth / running_max - 1.0


def max_drawdown(returns: pd.Series | pd.DataFrame) -> float | pd.Series:
    """Máxima caída (mínimo de `drawdown_series`), como número negativo."""
    return drawdown_series(returns).min()


def _underwater_counter(dd: pd.Series) -> pd.Series:
    """Nº de periodos consecutivos en drawdown (0 cuando se está en máximos)."""
    under = dd < 0
    groups = (~under).cumsum()  # nuevo grupo cada vez que se toca un máximo
    return under.groupby(groups).cumsum()


def time_under_water(returns: pd.Series | pd.DataFrame) -> float | pd.Series:
    """Duración (en periodos) del episodio de drawdown más largo.

    Un episodio empieza cuando el valor cae bajo su máximo previo y termina al
    recuperarlo. Si el último episodio sigue abierto, se cuenta hasta el final.
    """
    dd = drawdown_series(returns)
    if isinstance(dd, pd.DataFrame):
        return dd.apply(lambda c: _underwater_counter(c).max())
    return _underwater_counter(dd).max()


def _recovery_time_single(dd: pd.Series) -> float:
    trough = dd.idxmin()
    if dd.loc[trough] >= 0:
        return 0.0  # nunca hubo drawdown
    pos_trough = dd.index.get_loc(trough)
    after = dd.iloc[pos_trough:]
    recovered = np.flatnonzero(after.to_numpy() >= 0)
    if len(recovered) == 0:
        return np.nan  # aún no se ha recuperado el máximo previo
    return float(recovered[0])


def recovery_time(returns: pd.Series | pd.DataFrame) -> float | pd.Series:
    """Periodos necesarios para recuperar el máximo previo tras el mayor drawdown.

    Se cuenta desde el mínimo (trough) del mayor drawdown hasta que el valor
    vuelve al máximo previo. Devuelve NaN si no se ha recuperado.
    """
    dd = drawdown_series(returns)
    if isinstance(dd, pd.DataFrame):
        return dd.apply(_recovery_time_single)
    return _recovery_time_single(dd)
