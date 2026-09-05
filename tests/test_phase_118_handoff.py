from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile
from advanced_technical_indicators.phase_118_handoff import (
    build_phase_118_multi_window_feature_grid_handoff_report,
    summarize_phase_118_handoff,
)


def test_phase_118_handoff():
    profile = get_default_technical_indicator_profile()
    df, summary = build_phase_118_multi_window_feature_grid_handoff_report(profile)

    assert not df.empty
    assert len(df) >= 8
    assert summary["handoff_status"] == "READY"
    assert summary["all_items_ready"] is True
    assert summary["current_phase"] == 117
    assert summary["next_phase"] == 118
    assert summary["target_final_phase"] == 160
