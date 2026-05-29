import pandas as pd
from scenario_regression.failure_register import build_failures_from_regression_results, classify_failure_severity

def test_failure_register():
    t_df = pd.DataFrame([{"scenario_id": "s1", "warnings": "live order found"}])
    fails = build_failures_from_regression_results({"tbl1": t_df})
    assert len(fails) > 0
    assert fails[0].severity == "critical_regression_failure"
