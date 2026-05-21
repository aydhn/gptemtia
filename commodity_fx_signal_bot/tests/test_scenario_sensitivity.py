import pytest
import pandas as pd
from portfolio_regime.scenario_sensitivity import (
    calculate_symbol_scenario_sensitivity,
    calculate_basket_scenario_sensitivity
)

def test_scenario_sensitivity():
    ret_df = pd.DataFrame({"AAPL": [0.01], "GOOG": [0.02]})
    exp_df = pd.DataFrame({"scen1": [1.0, -1.0]}, index=["AAPL", "GOOG"])

    sym_sens = calculate_symbol_scenario_sensitivity(ret_df, exp_df)
    assert not sym_sens.empty

    bask_sens = calculate_basket_scenario_sensitivity({"AAPL": 0.5, "GOOG": 0.5}, exp_df)
    assert not bask_sens.empty
