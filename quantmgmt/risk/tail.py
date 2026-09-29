"""Familia "Cola": var_historical, var_parametric, cvar_historical, cvar_parametric,
skewness, kurtosis.
"""

from __future__ import annotations

import pandas as pd


def var_historical(
    returns: pd.Series | pd.DataFrame,
    level: float = 0.95,
) -> float | pd.Series:
    """Value at Risk histórico al nivel de confianza `level` (percentil empírico).

    Se devuelve como número positivo (pérdida esperada).
    """
    raise NotImplementedError


def var_parametric(
    returns: pd.Series | pd.DataFrame,
    level: float = 0.95,
    method: str = "gaussian",
) -> float | pd.Series:
    """Value at Risk paramétrico.

    Parameters
    ----------
    method : {"gaussian", "cornish-fisher"}
        "gaussian"       -> asume normalidad de los retornos.
        "cornish-fisher" -> ajusta el cuantil normal con skewness y kurtosis.
    """
    raise NotImplementedError


def cvar_historical(
    returns: pd.Series | pd.DataFrame,
    level: float = 0.95,
) -> float | pd.Series:
    """Conditional VaR (Expected Shortfall) histórico: media de las pérdidas más allá del VaR."""
    raise NotImplementedError


def cvar_parametric(
    returns: pd.Series | pd.DataFrame,
    level: float = 0.95,
    method: str = "gaussian",
) -> float | pd.Series:
    """Conditional VaR paramétrico (gaussiano o con ajuste Cornish-Fisher)."""
    raise NotImplementedError


def skewness(returns: pd.Series | pd.DataFrame) -> float | pd.Series:
    """Asimetría (tercer momento estandarizado) de los retornos."""
    raise NotImplementedError


def kurtosis(returns: pd.Series | pd.DataFrame, excess: bool = True) -> float | pd.Series:
    """Curtosis (cuarto momento estandarizado) de los retornos.

    Si `excess` es True, se resta 3 (curtosis en exceso respecto a la normal).
    """
    raise NotImplementedError
