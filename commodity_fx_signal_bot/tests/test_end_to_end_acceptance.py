import pandas as pd
from scenario_regression.end_to_end_acceptance import build_end_to_end_demo_acceptance_report
from scenario_regression.regression_config import get_default_scenario_regression_profile

def test_end_to_end_acceptance():
    prof = get_default_scenario_regression_profile()
    df, summ = build_end_to_end_demo_acceptance_report(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), prof)
    assert "score" in summ
