"""Familia "Ratios": sharpe_ratio, sortino_ratio, calmar_ratio, tracking_error."""

from __future__ import annotations

import pandas as pd

from .dispersion import annualized_volatility, downside_deviation
from .drawdown import max_drawdown
from .returns import annualized_return, cagr


def sharpe_ratio(
    returns: pd.Series | pd.DataFrame,
    periods_per_year: int = 252,
    risk_free: float = 0.0,
) -> float | pd.Series:
    """Ratio de Sharpe anualizado: (retorno anualizado - rf) / volatilidad anualizada.

    `risk_free` es una tasa anual (p. ej. 0.03 para un 3%).
    """
    excess = annualized_return(returns, periods_per_year) - risk_free
    return excess / annualized_volatility(returns, periods_per_year)


def sortino_ratio(
    returns: pd.Series | pd.DataFrame,
    periods_per_year: int = 252,
    risk_free: float = 0.0,
    threshold: float = 0.0,
) -> float | pd.Series:
    """Ratio de Sortino anualizado: usa `downside_deviation` en vez de la volatilidad total.

    `risk_free` es una tasa anual; `threshold` es un retorno por periodo.
    """
    excess = annualized_return(returns, periods_per_year) - risk_free
    return excess / downside_deviation(returns, threshold, periods_per_year)


def calmar_ratio(
    returns: pd.Series | pd.DataFrame,
    periods_per_year: int = 252,
) -> float | pd.Series:
    """Ratio de Calmar: retorno anualizado / |max_drawdown|.

    Se usa el CAGR como retorno anualizado, siguiendo la definición habitual.
    """
    return cagr(returns, periods_per_year) / abs(max_drawdown(returns))


def tracking_error(
    returns: pd.Series | pd.DataFrame,
    benchmark_returns: pd.Series,
    periods_per_year: int = 252,
) -> float | pd.Series:
    """Volatilidad anualizada de la diferencia de retornos frente a un benchmark."""
    active = returns.sub(benchmark_returns, axis=0).dropna()
    return annualized_volatility(active, periods_per_year)
