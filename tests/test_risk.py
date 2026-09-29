"""Tests unitarios para quantmgmt.risk.

Nota del enunciado: los tests están para comprobar que lo implementado tiene
sentido, no hace falta hacer cientos de tests. Aquí hay un esqueleto con
fixtures y un test por familia de funciones; están marcados con
`pytest.mark.skip` hasta que se implemente la lógica correspondiente en
`quantmgmt/risk/*.py` (quitar el `skip` a medida que se vaya implementando).
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from quantmgmt import risk


@pytest.fixture
def sample_returns() -> pd.Series:
    """Serie de retornos diarios sintética y reproducible."""
    rng = np.random.default_rng(42)
    dates = pd.date_range("2015-01-01", periods=252 * 3, freq="B")
    data = rng.normal(loc=0.0004, scale=0.01, size=len(dates))
    return pd.Series(data, index=dates, name="ASSET_A")


@pytest.fixture
def sample_returns_df(sample_returns: pd.Series) -> pd.DataFrame:
    """DataFrame con dos activos para probar el comportamiento multi-columna."""
    rng = np.random.default_rng(7)
    other = pd.Series(
        rng.normal(loc=0.0002, scale=0.015, size=len(sample_returns)),
        index=sample_returns.index,
        name="ASSET_B",
    )
    return pd.concat([sample_returns, other], axis=1)


@pytest.mark.skip(reason="TODO: implementar to_returns/cagr/annualized_return")
def test_returns_family(sample_returns: pd.Series) -> None:
    cumulative = risk.cumulative_returns(sample_returns)
    assert cumulative.iloc[-1] > -1  # no se puede perder más del 100%

    value = risk.cagr(sample_returns, periods_per_year=252)
    assert isinstance(value, float)


@pytest.mark.skip(reason="TODO: implementar annualized_volatility/downside_deviation")
def test_dispersion_family(sample_returns: pd.Series) -> None:
    vol = risk.annualized_volatility(sample_returns, periods_per_year=252)
    assert vol > 0

    dd_dev = risk.downside_deviation(sample_returns, periods_per_year=252)
    assert dd_dev >= 0


@pytest.mark.skip(reason="TODO: implementar drawdown_series/max_drawdown")
def test_drawdown_family(sample_returns: pd.Series) -> None:
    dd = risk.drawdown_series(sample_returns)
    assert (dd <= 0).all()

    mdd = risk.max_drawdown(sample_returns)
    assert mdd <= 0
    assert mdd == pytest.approx(dd.min())


@pytest.mark.skip(reason="TODO: implementar sharpe_ratio/sortino_ratio/calmar_ratio")
def test_ratios_family(sample_returns: pd.Series) -> None:
    sharpe = risk.sharpe_ratio(sample_returns, periods_per_year=252)
    sortino = risk.sortino_ratio(sample_returns, periods_per_year=252)
    calmar = risk.calmar_ratio(sample_returns, periods_per_year=252)
    assert np.isfinite(sharpe)
    assert np.isfinite(sortino)
    assert np.isfinite(calmar)


@pytest.mark.skip(reason="TODO: implementar var/cvar historico y parametrico")
def test_tail_family(sample_returns: pd.Series) -> None:
    var_hist = risk.var_historical(sample_returns, level=0.95)
    cvar_hist = risk.cvar_historical(sample_returns, level=0.95)
    # el CVaR (pérdida media más allá del VaR) debe ser >= al VaR
    assert cvar_hist >= var_hist

    var_gauss = risk.var_parametric(sample_returns, level=0.95, method="gaussian")
    var_cf = risk.var_parametric(sample_returns, level=0.95, method="cornish-fisher")
    assert np.isfinite(var_gauss)
    assert np.isfinite(var_cf)


@pytest.mark.skip(reason="TODO: implementar la metrica de riesgo propia")
def test_custom_metric(sample_returns: pd.Series) -> None:
    value = risk.custom_risk_metric(sample_returns, periods_per_year=252)
    assert np.isfinite(value)


@pytest.mark.skip(reason="TODO: comprobar que las funciones aceptan DataFrame multi-activo")
def test_dataframe_input(sample_returns_df: pd.DataFrame) -> None:
    vol = risk.annualized_volatility(sample_returns_df, periods_per_year=252)
    assert isinstance(vol, pd.Series)
    assert set(vol.index) == set(sample_returns_df.columns)
