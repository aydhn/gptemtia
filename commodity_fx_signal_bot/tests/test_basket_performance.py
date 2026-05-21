import pandas as pd
import numpy as np
from portfolio_research.portfolio_config import get_default_portfolio_research_profile
from portfolio_research.basket_definitions import build_equal_weight_basket
from portfolio_research.basket_performance import (
    calculate_virtual_basket_returns,
    calculate_virtual_basket_equity_curve,
    calculate_virtual_basket_performance
)

def test_basket_performance():
    profile = get_default_portfolio_research_profile()
    b = build_equal_weight_basket(["A", "B"], "1d", profile)

    dates = pd.date_range("2023-01-01", periods=10)
    ret_df = pd.DataFrame({
        "A": np.random.randn(10) * 0.01,
        "B": np.random.randn(10) * 0.01
    }, index=dates)

    bret = calculate_virtual_basket_returns(ret_df, b)
    assert len(bret) == 10

    eq = calculate_virtual_basket_equity_curve(bret)
    assert not eq.empty

    perf = calculate_virtual_basket_performance(b, ret_df)
    assert perf.observation_count == 10
