from pathlib import Path
from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile
from advanced_technical_indicators.technical_indicator_health import (
    build_technical_indicator_health_check,
    summarize_technical_indicator_health,
)


def test_technical_indicator_health():
    project_root = Path(__file__).resolve().parent.parent
    profile = get_default_technical_indicator_profile()
    df, summary = build_technical_indicator_health_check(project_root, profile)

    assert not df.empty
    assert summary["health_status"] == "HEALTHY"
    assert summary["all_passed"] is True
