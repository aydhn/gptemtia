import pandas as pd
from scenario_regression.demo_workflow_regression import build_demo_workflow_regression_report
from scenario_regression.regression_config import get_default_scenario_regression_profile

def test_demo_workflow_regression():
    prof = get_default_scenario_regression_profile()
    df, summ = build_demo_workflow_regression_report(None, None, None, prof)
    assert summ["summary"]["workflow_valid"] is False
