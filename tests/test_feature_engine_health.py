from pathlib import Path
from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.feature_engine_health import (
    build_feature_engine_health_check,
    summarize_feature_engine_health,
)


def test_feature_engine_health():
    profile = get_default_feature_engine_profile()
    project_root = Path(__file__).resolve().parent.parent

    df, summary = build_feature_engine_health_check(project_root, profile)

    assert not df.empty
    assert len(df) >= 10
    assert summary["overall_status"] == "PASS"
    assert summary["all_passed"] is True
    assert summary["failed_checks"] == 0
