import pandas as pd
from scenario_regression.drift_detection import detect_golden_output_drift
from scenario_regression.regression_config import get_default_scenario_regression_profile

def test_drift_detection():
    prof = get_default_scenario_regression_profile()
    g_df = pd.DataFrame([{"scenario_id": "s1", "matched": True}])
    df = detect_golden_output_drift(g_df, prof)
    assert not df.empty
    assert df.iloc[0]["drift_label"] == "no_drift"
