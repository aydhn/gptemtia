from portable_packaging.environment_drift import (
    compare_environment_snapshots,
    classify_environment_drift,
    build_environment_drift_report
)

def test_environment_drift():
    comp = compare_environment_snapshots({"os_name": "linux"}, {"os_name": "linux"})
    assert comp["is_identical"]

    cls = classify_environment_drift(comp)
    assert cls == "environment_match"

    df, s = build_environment_drift_report(None, None)
    assert s["drift_status"] == "environment_missing_snapshot"
