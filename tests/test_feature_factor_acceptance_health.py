from pathlib import Path
from advanced_feature_factor_acceptance.feature_factor_acceptance_health import (
    build_feature_factor_acceptance_health_check,
    summarize_feature_factor_acceptance_health,
)

def test_feature_factor_acceptance_health():
    root = Path(__file__).resolve().parent.parent
    df, summary = build_feature_factor_acceptance_health_check(project_root=root)
    assert not df.empty
    assert summary["health_status"] == "HEALTHY"
    assert summary["failed_checks"] == 0
    assert summary["non_signal"] is True

    s = summarize_feature_factor_acceptance_health(df)
    assert s["overall_health"] == "HEALTHY"
    assert s["all_passed"] is True
    assert s["non_signal"] is True
