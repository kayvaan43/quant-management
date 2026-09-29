"""Familia "Dispersión": annualized_volatility, downside_deviation, rolling_volatility."""

from __future__ import annotations

import pandas as pd


def annualized_volatility(
    returns: pd.Series | pd.DataFrame,
    periods_per_year: int = 252,
) -> float | pd.Series:
    """Desviación estándar de los retornos, anualizada (sqrt(periods_per_year))."""
    raise NotImplementedError


def downside_deviation(
    returns: pd.Series | pd.DataFrame,
    threshold: float = 0.0,
    periods_per_year: int = 252,
) -> float | pd.Series:
    """Desviación estándar de los retornos por debajo de `threshold`, anualizada.

    Es la base del ratio de Sortino.
    """
    raise NotImplementedError


def rolling_volatility(
    returns: pd.Series | pd.DataFrame,
    window: int = 63,
    periods_per_year: int = 252,
) -> pd.Series | pd.DataFrame:
    """Volatilidad anualizada calculada en una ventana móvil de `window` periodos."""
    raise NotImplementedError
