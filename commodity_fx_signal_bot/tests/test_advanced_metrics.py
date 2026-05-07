import pytest
import pandas as pd
import numpy as np
from backtesting.advanced_metrics import (
    calculate_total_return,
    calculate_cagr,
    calculate_annualized_volatility,
    calculate_sharpe_ratio,
    calculate_sortino_ratio,
    calculate_calmar_ratio,
    calculate_profit_factor,
    calculate_expectancy,
    calculate_payoff_ratio,
    build_advanced_performance_metrics,
)


def test_calculate_total_return():
    df = pd.DataFrame({"equity": [100.0, 110.0, 120.0]})
    assert calculate_total_return(df) == pytest.approx(0.2)
    assert calculate_total_return(pd.DataFrame()) == 0.0


def test_calculate_cagr():
    df = pd.DataFrame({"equity": [100.0, 110.0, 121.0]})
    cagr = calculate_cagr(df, 252)
    assert not np.isnan(cagr)


def test_calculate_annualized_volatility():
    df = pd.DataFrame({"equity": [100.0, 101.0, 100.0, 102.0]})
    vol = calculate_annualized_volatility(df)
    assert not np.isnan(vol)


def test_calculate_sharpe_and_sortino():
    df = pd.DataFrame({"equity": [100.0, 102.0, 101.0, 105.0]})
    sharpe = calculate_sharpe_ratio(df)
    sortino = calculate_sortino_ratio(df)
    assert not np.isnan(sharpe)
    assert not np.isnan(sortino)


def test_calculate_calmar_ratio():
    df = pd.DataFrame({"equity": [100.0, 120.0, 90.0, 150.0]})
    calmar = calculate_calmar_ratio(df)
    assert not np.isnan(calmar)


def test_calculate_profit_factor():
    trades = pd.DataFrame({"net_pnl": [10.0, -5.0, 20.0, -10.0]})
    assert calculate_profit_factor(trades) == pytest.approx(2.0)


def test_calculate_expectancy():
    trades = pd.DataFrame({"net_pnl": [10.0, -5.0, 10.0, -5.0]})
    assert calculate_expectancy(trades) == pytest.approx(2.5)


def test_calculate_payoff_ratio():
    trades = pd.DataFrame({"net_pnl": [10.0, -5.0, 20.0, -10.0]})
    assert calculate_payoff_ratio(trades) == pytest.approx(2.0)


def test_build_advanced_performance_metrics():
    trades = pd.DataFrame(
        {"net_pnl": [10.0, -5.0], "return_pct": [0.1, -0.05], "holding_bars": [2, 3]}
    )
    equity = pd.DataFrame({"equity": [100.0, 110.0, 105.0]})
    metrics = build_advanced_performance_metrics(trades, equity, 100.0)
    assert "total_return_pct" in metrics
    assert "cagr" in metrics
    assert "sharpe_ratio" in metrics
    assert "profit_factor" in metrics
    assert "exposure_time_proxy" in metrics
