"""Familia "Ratios": sharpe_ratio, sortino_ratio, calmar_ratio, tracking_error."""

from __future__ import annotations

import pandas as pd


def sharpe_ratio(
    returns: pd.Series | pd.DataFrame,
    periods_per_year: int = 252,
    risk_free: float = 0.0,
) -> float | pd.Series:
    """Ratio de Sharpe anualizado: (retorno anualizado - rf) / volatilidad anualizada."""
    raise NotImplementedError


def sortino_ratio(
    returns: pd.Series | pd.DataFrame,
    periods_per_year: int = 252,
    risk_free: float = 0.0,
    threshold: float = 0.0,
) -> float | pd.Series:
    """Ratio de Sortino anualizado: usa `downside_deviation` en vez de la volatilidad total."""
    raise NotImplementedError


def calmar_ratio(
    returns: pd.Series | pd.DataFrame,
    periods_per_year: int = 252,
) -> float | pd.Series:
    """Ratio de Calmar: retorno anualizado / |max_drawdown|."""
    raise NotImplementedError


def tracking_error(
    returns: pd.Series | pd.DataFrame,
    benchmark_returns: pd.Series,
    periods_per_year: int = 252,
) -> float | pd.Series:
    """Volatilidad anualizada de la diferencia de retornos frente a un benchmark."""
    raise NotImplementedError
