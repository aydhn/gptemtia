from advanced_technical_indicators.indicator_quality_handoff import (
    build_indicator_quality_handoff_report,
    summarize_indicator_quality_handoff,
)
from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile


def test_indicator_quality_handoff():
    prof = get_default_technical_indicator_profile()
    df, summary = build_indicator_quality_handoff_report(prof)
    assert not df.empty
    assert summary["all_checks_ready"] is True
    assert summary["current_phase"] == 117
    assert summary["next_phase"] == 118
