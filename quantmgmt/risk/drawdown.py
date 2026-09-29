"""Familia "Drawdown": drawdown_series, max_drawdown, time_under_water, recovery_time."""

from __future__ import annotations

import pandas as pd


def drawdown_series(returns: pd.Series | pd.DataFrame) -> pd.Series | pd.DataFrame:
    """Serie de drawdown: caída porcentual respecto al máximo acumulado previo.

    drawdown_t = valor_t / max(valor_0..t) - 1, con valor = rentabilidad acumulada.
    """
    raise NotImplementedError


def max_drawdown(returns: pd.Series | pd.DataFrame) -> float | pd.Series:
    """Máxima caída (mínimo de `drawdown_series`), como número negativo."""
    raise NotImplementedError


def time_under_water(returns: pd.Series | pd.DataFrame) -> pd.Series:
    """Duración (en periodos) de cada episodio de drawdown, o estadístico resumen."""
    raise NotImplementedError


def recovery_time(returns: pd.Series | pd.DataFrame) -> pd.Series:
    """Periodos necesarios para recuperar el máximo previo tras el mayor drawdown."""
    raise NotImplementedError
