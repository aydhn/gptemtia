from scenario_regression.acceptance_checklist import build_regression_acceptance_checklist
from scenario_regression.regression_config import get_default_scenario_regression_profile

def test_acceptance_checklist():
    prof = get_default_scenario_regression_profile()
    df = build_regression_acceptance_checklist(prof)
    assert not df.empty
