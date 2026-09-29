"""Familia "Rentabilidad": to_returns, cumulative_returns, cagr, annualized_return.

Convención general del módulo `risk`: todas las funciones reciben un
`pd.Series` (un activo) o `pd.DataFrame` (varios activos/carteras en columnas)
de retornos o precios, indexado por fecha, y un parámetro `periods_per_year`
cuando aplique (252 para diario, 12 para mensual, etc.). Devuelven un escalar
(o un `pd.Series` con un valor por columna cuando la entrada es un DataFrame).
"""

from __future__ import annotations

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
    raise NotImplementedError


def cumulative_returns(returns: pd.Series | pd.DataFrame) -> pd.Series | pd.DataFrame:
    """Rentabilidad acumulada (base 1 / 100%) a partir de una serie de retornos."""
    raise NotImplementedError


def cagr(
    returns: pd.Series | pd.DataFrame,
    periods_per_year: int = 252,
) -> float | pd.Series:
    """Compound Annual Growth Rate: rentabilidad anualizada geométrica."""
    raise NotImplementedError


def annualized_return(
    returns: pd.Series | pd.DataFrame,
    periods_per_year: int = 252,
) -> float | pd.Series:
    """Rentabilidad media por periodo, anualizada."""
    raise NotImplementedError
