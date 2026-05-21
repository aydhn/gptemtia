import pytest
import pandas as pd
from portfolio_regime.regime_config import PortfolioRegimeProfile
from portfolio_regime.macro_scenarios import (
    build_default_macro_scenarios,
    build_scenario_exposure_matrix,
    macro_scenarios_to_dataframe
)

def test_macro_scenarios():
    profile = PortfolioRegimeProfile(name="test", description="")
    scenarios = build_default_macro_scenarios(profile)
    assert len(scenarios) > 0

    df = macro_scenarios_to_dataframe(scenarios)
    assert not df.empty

    exposure = build_scenario_exposure_matrix(["AAPL", "GOOG"], pd.DataFrame(), scenarios)
    assert not exposure.empty
    assert "AAPL" in exposure.index
