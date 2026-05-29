import pandas as pd
from scenario_regression.snapshot_compare import compare_snapshot_tables
from scenario_regression.regression_config import get_default_scenario_regression_profile

def test_snapshot_compare():
    prof = get_default_scenario_regression_profile()
    b_df = pd.DataFrame([{"scenario_id": "s1", "snapshot_name": "n1", "snapshot_id": "b1", "schema_hash": "h1", "content_hash": "c1", "row_count": 1}])
    c_df = pd.DataFrame([{"scenario_id": "s1", "snapshot_name": "n1", "snapshot_id": "c1", "schema_hash": "h1", "content_hash": "c1", "row_count": 1}])

    diff_df, summary = compare_snapshot_tables(b_df, c_df, prof)
    assert not diff_df.empty
    assert diff_df.iloc[0]["diff_label"] == "snapshot_identical"
