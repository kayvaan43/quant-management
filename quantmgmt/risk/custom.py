"""Métrica de riesgo propia (pedida en el enunciado de la Práctica 1): índice de insomnio."""

from __future__ import annotations

import pandas as pd

from .drawdown import drawdown_series


def custom_risk_metric(
    returns: pd.Series | pd.DataFrame,
    periods_per_year: int = 252,
    threshold: float = -0.10,
) -> float | pd.Series:
    """Índice de insomnio: fracción de periodos con drawdown peor que `threshold`.

    Mide cuánto tiempo pasa la cartera en una caída "que quita el sueño"
    (por defecto, más de un 10% bajo su máximo previo). A diferencia de
    `time_under_water`, no mira solo el episodio más largo sino el total.

    Rango [0, 1]: 0 = nunca cayó tanto; 1 = siempre estuvo así de abajo.
    Menor es mejor. `periods_per_year` no se usa (la métrica es una
    proporción), pero se mantiene por consistencia con el resto de `risk`.
    """
    return (drawdown_series(returns) < threshold).mean()
