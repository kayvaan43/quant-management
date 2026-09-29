"""Familia "Dispersión": annualized_volatility, downside_deviation, rolling_volatility."""

from __future__ import annotations

import numpy as np
import pandas as pd


def annualized_volatility(
    returns: pd.Series | pd.DataFrame,
    periods_per_year: int = 252,
) -> float | pd.Series:
    """Desviación estándar de los retornos, anualizada (sqrt(periods_per_year))."""
    return returns.std(ddof=1) * np.sqrt(periods_per_year)
            # ddof=n; n=grados de libertad
            # Pandas ddof=1 ; Numpy ddof=0 || Tener cuidado a la hora de usarlo.

def downside_deviation(
    returns: pd.Series | pd.DataFrame,
    threshold: float = 0.0,
    periods_per_year: int = 252,
) -> float | pd.Series:
    """Desviación estándar de los retornos por debajo de `threshold`, anualizada.

    Es la base del ratio de Sortino.

    Se usa la definición estándar (semidesviación respecto al objetivo):
    sqrt(mean(min(r - threshold, 0)^2)), promediando sobre TODOS los periodos
    (los que superan el umbral aportan 0), y se anualiza con sqrt(periods_per_year).
    """
    shortfall = np.minimum(returns - threshold, 0.0)
    return np.sqrt((shortfall**2).mean()) * np.sqrt(periods_per_year)


def rolling_volatility(
    returns: pd.Series | pd.DataFrame,
    window: int = 63,
    periods_per_year: int = 252,
) -> pd.Series | pd.DataFrame:
    """Volatilidad anualizada calculada en una ventana móvil de `window` periodos."""
    return returns.rolling(window).std(ddof=1) * np.sqrt(periods_per_year)
