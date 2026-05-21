import pytest
import pandas as pd
from portfolio_regime.regime_classifier import (
    calculate_portfolio_proxy_return,
    calculate_rolling_volatility,
    calculate_rolling_trend,
    calculate_rolling_drawdown,
    classify_volatility_state,
    classify_trend_state,
    classify_drawdown_state,
    classify_portfolio_regimes
)
from portfolio_regime.regime_config import PortfolioRegimeProfile

def test_proxy_return():
    df = pd.DataFrame({"A": [0.01, -0.01], "B": [0.02, 0.02]})
    res = calculate_portfolio_proxy_return(df)
    assert len(res) == 2
    assert res.iloc[0] == 0.015
    assert res.iloc[1] == 0.005

def test_classify_volatility_state():
    assert classify_volatility_state(0.1, 0.2, 0.4) == "low_volatility"
    assert classify_volatility_state(0.3, 0.2, 0.4) == "normal_volatility"
    assert classify_volatility_state(0.5, 0.2, 0.4) == "high_volatility"

def test_classify_trend_state():
    assert classify_trend_state(0.005) == "positive_trend"
    assert classify_trend_state(-0.005) == "negative_trend"
    assert classify_trend_state(0.0005) == "sideways_trend"

def test_classify_portfolio_regimes():
    profile = PortfolioRegimeProfile(name="test", description="")
    df = pd.DataFrame({"A": [0.01]*50, "B": [-0.01]*50})
    res_df, summary = classify_portfolio_regimes(df, profile)
    assert not res_df.empty
    assert "regime_label" in res_df.columns
    assert "volatility_state" in res_df.columns
