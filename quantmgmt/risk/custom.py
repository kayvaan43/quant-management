"""Métrica de riesgo propia (pedida en el enunciado de la Práctica 1).

TODO: diseñar una métrica de riesgo innovadora. Puede ser una combinación de
otras métricas (p.ej. algo tipo "Sharpe ajustado por cola") o algo
completamente nuevo. Requisitos del enunciado:
  - Debe estar bien documentada (qué mide, cómo se interpreta, rango de
    valores esperado).
  - Debe ser estandarizada, es decir, calculable igual para cualquier
    pd.Series/pd.DataFrame de retornos con la misma firma que el resto de
    funciones de `risk` (returns, periods_per_year, ...).
  - Debe permitir comparar carteras/NAVs distintos entre sí (¿cuál es mejor
    según esta métrica?).
"""

from __future__ import annotations

import pandas as pd


def custom_risk_metric(
    returns: pd.Series | pd.DataFrame,
    periods_per_year: int = 252,
) -> float | pd.Series:
    """Métrica de riesgo propia.

    TODO:
        1. Definir la fórmula/idea (¿combina Sharpe, drawdown, cola...? ¿es
           nueva?).
        2. Documentar aquí qué mide y cómo interpretar valores altos/bajos.
        3. Implementar el cálculo.
        4. Usarla en `notebooks/01_riesgo.ipynb` para comparar las carteras y
           responder a la pregunta "¿qué nos dice la métrica que habéis
           creado?".
    """
    raise NotImplementedError
