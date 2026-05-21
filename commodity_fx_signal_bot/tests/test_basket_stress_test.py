import pytest
import pandas as pd
from portfolio_regime.basket_stress_test import (
    run_scenario_stress_test_for_basket,
    run_historical_stress_test_for_basket,
    build_basket_stress_test_summary,
    VirtualBasketDefinition
)
from portfolio_regime.regime_models import MacroScenarioDefinition

def test_basket_stress_test():
    basket = VirtualBasketDefinition("basket_1", {"AAPL": 1.0})
    scen = MacroScenarioDefinition("id1", "label1", "desc", "f", "up", 0.05, ["AAPL"], "m", [])
    exp_df = pd.DataFrame({"id1": [1.0]}, index=["AAPL"])

    res = run_scenario_stress_test_for_basket(basket, [scen], exp_df)
    assert not res.empty

    windows = pd.DataFrame({"stress_window_id": ["w1"], "stress_severity": ["severe_stress"]})
    ret = pd.Series([1.0])
    hist = run_historical_stress_test_for_basket(ret, windows)
    assert not hist.empty

    summary = build_basket_stress_test_summary(res, hist)
    assert summary["scenario_tests_run"] == 1
