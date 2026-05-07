import pytest
import pandas as pd
import numpy as np
from backtesting.rolling_metrics import (
    calculate_rolling_returns,
    calculate_rolling_volatility,
    calculate_rolling_sharpe,
    calculate_rolling_drawdown,
    build_rolling_metrics_frame,
)


def get_dummy_equity():
    return pd.DataFrame({"equity": np.linspace(100, 200, 100)})


def test_calculate_rolling_returns():
    eq = get_dummy_equity()
    res = calculate_rolling_returns(eq, windows=(10, 20))
    assert "rolling_return_10" in res.columns
    assert "rolling_return_20" in res.columns
    assert pd.isna(res["rolling_return_10"].iloc[0])


def test_calculate_rolling_volatility():
    eq = get_dummy_equity()
    res = calculate_rolling_volatility(eq, windows=(10,))
    assert "rolling_volatility_10" in res.columns


def test_calculate_rolling_sharpe():
    eq = get_dummy_equity()
    res = calculate_rolling_sharpe(eq, windows=(10,))
    assert "rolling_sharpe_10" in res.columns


def test_calculate_rolling_drawdown():
    eq = get_dummy_equity()
    res = calculate_rolling_drawdown(eq, windows=(10,))
    assert "rolling_max_drawdown_10" in res.columns


def test_build_rolling_metrics_frame():
    eq = get_dummy_equity()
    df, summary = build_rolling_metrics_frame(eq, windows=(10, 20))
    assert not df.empty
    assert "latest_rolling_return_10" in summary
