# quant-management

Monorepo para la asignatura *Quant Portfolio Management*. Contiene la librería
`quantmgmt`, con la que se implementan y evalúan todas las prácticas del curso:
descarga de datos, métricas de riesgo, factores/atribución, optimización de
carteras y backtesting.

## Estructura

```
quant-management/
├── README.md              # este archivo
├── pyproject.toml         # dependencias y configuración del paquete
├── quantmgmt/
│   ├── data/               # descarga y caché de precios
│   ├── risk/                # métricas de riesgo (P1)
│   ├── analytics/          # factores y atribución (P2)
│   ├── optimizers/          # MPT, Black-Litterman, HRP (P2-P3)
│   └── backtest/           # backtesting (prácticas posteriores)
├── notebooks/
│   └── 01_riesgo.ipynb      # aplicación práctica del módulo risk
├── tests/
│   └── test_risk.py
└── data/cache/              # caché local de datos descargados (en .gitignore)
```

## Instalación

Se recomienda usar un entorno virtual (venv, conda, etc.) con Python >= 3.10.

```bash
cd quant-management
python -m venv .venv
source .venv/bin/activate        # en Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

Esto instala `quantmgmt` en modo editable junto con las dependencias de
desarrollo (`pytest`, `jupyter`, etc.) definidas en `pyproject.toml`.

## Uso rápido

```python
import pandas as pd
from quantmgmt.data import download_prices
from quantmgmt.risk import (
    to_returns,
    cagr,
    annualized_volatility,
    sharpe_ratio,
    max_drawdown,
    var_historical,
    cvar_historical,
)

prices = download_prices(["SPY", "AGG"], start="2013-01-01")
returns = to_returns(prices, method="log")

periods_per_year = 252
summary = pd.DataFrame({
    "CAGR": cagr(returns, periods_per_year),
    "Vol anualizada": annualized_volatility(returns, periods_per_year),
    "Sharpe": sharpe_ratio(returns, periods_per_year),
    "Max Drawdown": max_drawdown(returns),
    "VaR 95% hist.": var_historical(returns, level=0.95),
    "CVaR 95% hist.": cvar_historical(returns, level=0.95),
})
print(summary)
```

## Tests

```bash
pytest
```

