from scenario_regression.snapshot_capture import capture_snapshot_for_artifact
from scenario_regression.regression_config import get_default_scenario_regression_profile
from pathlib import Path

def test_snapshot_capture(tmp_path):
    f = tmp_path / "test.csv"
    f.write_text("a,b\n1,2")
    prof = get_default_scenario_regression_profile()

    rec = capture_snapshot_for_artifact("scen1", "snap1", f, prof)
    assert rec.scenario_id == "scen1"
    assert rec.snapshot_name == "snap1"
    assert rec.row_count == 1
