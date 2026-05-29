import pandas as pd
from scenario_regression.regression_registry import build_default_regression_definitions, regression_definitions_to_dataframe
from scenario_regression.regression_config import get_default_scenario_regression_profile

def test_build_default_regression_definitions():
    scen_df = pd.DataFrame([{"scenario_id": "scen1"}])
    prof = get_default_scenario_regression_profile()
    defs = build_default_regression_definitions(scen_df, prof)
    assert len(defs) > 0

    df = regression_definitions_to_dataframe(defs)
    assert "regression_id" in df.columns
