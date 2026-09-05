from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile
from advanced_technical_indicators.technical_indicator_safety_boundary import (
    build_technical_indicator_safety_boundary,
    build_technical_indicator_no_go_conditions,
    build_technical_indicator_safe_go_conditions,
    summarize_technical_indicator_safety_boundary,
)


def test_technical_indicator_safety_boundary():
    profile = get_default_technical_indicator_profile()
    df, summary = build_technical_indicator_safety_boundary(profile)

    assert not df.empty
    assert summary["total_no_go"] >= 15
    assert summary["total_safe_go"] >= 8
    assert summary["safety_status"] == "ACTIVE"
