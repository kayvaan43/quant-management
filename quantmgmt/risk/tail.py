"""Familia "Cola": var_historical, var_parametric, cvar_historical, cvar_parametric,
skewness, kurtosis.
"""

from __future__ import annotations

from typing import Callable

import numpy as np
import pandas as pd
from scipy import stats

_METHODS = ("gaussian", "cornish-fisher")


def _check_level(level: float) -> float:
    """Valida el nivel de confianza y devuelve alpha = 1 - level (masa de la cola)."""
    if not 0.0 < level < 1.0:
        raise ValueError(f"`level` debe estar en (0, 1); recibido {level}")
    return 1.0 - level


def _check_method(method: str) -> str:
    if method not in _METHODS:
        raise ValueError(f"`method` debe ser uno de {_METHODS}; recibido {method!r}")
    return method


def _apply(
    returns: pd.Series | pd.DataFrame,
    func: Callable[[pd.Series], float],
) -> float | pd.Series:
    """Aplica `func` a una Serie (ignorando NaN) o a cada columna de un DataFrame."""
    if isinstance(returns, pd.DataFrame):
        return returns.apply(lambda col: func(col.dropna()))
    return func(returns.dropna())


def _cornish_fisher_z(z: np.ndarray | float, s: float, k: float) -> np.ndarray | float:
    """Cuantil normal ajustado por Cornish-Fisher (s = skewness, k = curtosis en exceso)."""
    return (
        z
        + (z**2 - 1) * s / 6
        + (z**3 - 3 * z) * k / 24
        - (2 * z**3 - 5 * z) * s**2 / 36
    )


def var_historical(
    returns: pd.Series | pd.DataFrame,
    level: float = 0.95,
) -> float | pd.Series:
    """Value at Risk histórico al nivel de confianza `level` (percentil empírico).

    Se devuelve como número positivo (pérdida esperada).
    """
    alpha = _check_level(level)
    return _apply(returns, lambda r: float(-r.quantile(alpha)))


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
    alpha = _check_level(level)
    _check_method(method)
    z = stats.norm.ppf(alpha)

    def _single(r: pd.Series) -> float:
        mu, sigma = r.mean(), r.std(ddof=1)
        q = z
        if method == "cornish-fisher":
            q = _cornish_fisher_z(z, skewness(r), kurtosis(r, excess=True))
        return float(-(mu + q * sigma))

    return _apply(returns, _single)


def cvar_historical(
    returns: pd.Series | pd.DataFrame,
    level: float = 0.95,
) -> float | pd.Series:
    """Conditional VaR (Expected Shortfall) histórico: media de las pérdidas más allá del VaR."""
    alpha = _check_level(level)

    def _single(r: pd.Series) -> float:
        cutoff = r.quantile(alpha)
        return float(-r[r <= cutoff].mean())

    return _apply(returns, _single)


def cvar_parametric(
    returns: pd.Series | pd.DataFrame,
    level: float = 0.95,
    method: str = "gaussian",
) -> float | pd.Series:
    """Conditional VaR paramétrico (gaussiano o con ajuste Cornish-Fisher).

    - "gaussian": ES = -(mu - sigma * phi(z_alpha) / alpha).
    - "cornish-fisher": ES = -(mu + sigma * (1/alpha) * integral_0^alpha z_cf(p) dp),
      integrando numéricamente el cuantil ajustado sobre la cola.
    """
    alpha = _check_level(level)
    _check_method(method)

    def _single(r: pd.Series) -> float:
        mu, sigma = r.mean(), r.std(ddof=1)
        if method == "gaussian":
            tail_mean_z = -stats.norm.pdf(stats.norm.ppf(alpha)) / alpha
        else:
            s, k = skewness(r), kurtosis(r, excess=True)
            # Regla del punto medio sobre una rejilla fina de probabilidades en (0, alpha)
            n = 10_000
            p = (np.arange(n) + 0.5) * alpha / n
            tail_mean_z = _cornish_fisher_z(stats.norm.ppf(p), s, k).mean()
        return float(-(mu + sigma * tail_mean_z))

    return _apply(returns, _single)


def skewness(returns: pd.Series | pd.DataFrame) -> float | pd.Series:
    """Asimetría (tercer momento estandarizado) de los retornos."""
    return _apply(returns, lambda r: float(stats.skew(r, bias=False)))


def kurtosis(returns: pd.Series | pd.DataFrame, excess: bool = True) -> float | pd.Series:
    """Curtosis (cuarto momento estandarizado) de los retornos.

    Si `excess` es True, se resta 3 (curtosis en exceso respecto a la normal).
    """
    return _apply(returns, lambda r: float(stats.kurtosis(r, fisher=excess, bias=False)))
