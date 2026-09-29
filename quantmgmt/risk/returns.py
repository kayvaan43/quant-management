"""Familia "Rentabilidad": to_returns, cumulative_returns, cagr, annualized_return.

Convención general del módulo `risk`: todas las funciones reciben un
`pd.Series` (un activo) o `pd.DataFrame` (varios activos/carteras en columnas)
de retornos o precios, indexado por fecha, y un parámetro `periods_per_year`
cuando aplique (252 para diario, 12 para mensual, etc.). Devuelven un escalar
(o un `pd.Series` con un valor por columna cuando la entrada es un DataFrame).
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def to_returns(
    prices: pd.Series | pd.DataFrame,
    method: str = "simple",
) -> pd.Series | pd.DataFrame:
    """Convierte precios en retornos.

    Parameters
    ----------
    prices : pd.Series | pd.DataFrame
        Precios (no retornos) indexados por fecha.
    method : {"simple", "log"}
        "simple" -> P_t / P_{t-1} - 1
        "log"    -> ln(P_t / P_{t-1})

    Returns
    -------
    pd.Series | pd.DataFrame
        Retornos por periodo (primera fila descartada por el NaN inicial).
    """

    """
    pct_change(): Método de pandas para calcular cambios porcentuales.
    """
    if method == "simple":
        return prices.pct_change().iloc[1:]
    if method == "log":
        return np.log(prices / prices.shift(1)).iloc[1:]
    raise ValueError(f"method debe ser 'simple' o 'log', no {method!r}")

def cumulative_returns(returns: pd.Series | pd.DataFrame) -> pd.Series | pd.DataFrame:
    """Rentabilidad acumulada (base 1 / 100%) a partir de una serie de retornos."""
    return (1 + returns).cumprod() - 1


def cagr(
    returns: pd.Series | pd.DataFrame,
    periods_per_year: int = 252,
) -> float | pd.Series:
    """Compound Annual Growth Rate: rentabilidad anualizada geométrica."""
    n = returns.shape[0]
    total_growth = (1 + returns).prod()
    return total_growth ** (periods_per_year / n) - 1


def annualized_return(
    returns: pd.Series | pd.DataFrame,
    periods_per_year: int = 252,
) -> float | pd.Series:
    """Rentabilidad media por periodo, anualizada."""
    return returns.mean() * periods_per_year
