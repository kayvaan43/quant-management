"""quantmgmt.risk

Librería de métricas de riesgo. Todas las funciones reciben un `pd.Series`
(un activo) o `pd.DataFrame` (varios activos/carteras en columnas), indexado
por fecha, de retornos (o precios en el caso de `to_returns`) y, cuando
aplique, un parámetro `periods_per_year`.

Familias
--------
Rentabilidad  to_returns, cumulative_returns, cagr, annualized_return
Dispersión    annualized_volatility, downside_deviation, rolling_volatility
Drawdown      drawdown_series, max_drawdown, time_under_water, recovery_time
Ratios        sharpe_ratio, sortino_ratio, calmar_ratio, tracking_error
Cola          var_historical, var_parametric, cvar_historical,
              cvar_parametric, skewness, kurtosis
Propia        custom_risk_metric
"""

from .returns import (
    to_returns,
    cumulative_returns,
    cagr,
    annualized_return,
)
from .dispersion import (
    annualized_volatility,
    downside_deviation,
    rolling_volatility,
)
from .drawdown import (
    drawdown_series,
    max_drawdown,
    time_under_water,
    recovery_time,
)
from .ratios import (
    sharpe_ratio,
    sortino_ratio,
    calmar_ratio,
    tracking_error,
)
from .tail import (
    var_historical,
    var_parametric,
    cvar_historical,
    cvar_parametric,
    skewness,
    kurtosis,
)
from .custom import custom_risk_metric

__all__ = [
    # Rentabilidad
    "to_returns",
    "cumulative_returns",
    "cagr",
    "annualized_return",
    # Dispersión
    "annualized_volatility",
    "downside_deviation",
    "rolling_volatility",
    # Drawdown
    "drawdown_series",
    "max_drawdown",
    "time_under_water",
    "recovery_time",
    # Ratios
    "sharpe_ratio",
    "sortino_ratio",
    "calmar_ratio",
    "tracking_error",
    # Cola
    "var_historical",
    "var_parametric",
    "cvar_historical",
    "cvar_parametric",
    "skewness",
    "kurtosis",
    # Propia
    "custom_risk_metric",
]
