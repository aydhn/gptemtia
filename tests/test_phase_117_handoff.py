from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.phase_117_handoff import (
    build_phase_117_technical_indicator_expansion_handoff_report,
    summarize_phase_117_handoff,
)


def test_phase_117_handoff():
    profile = get_default_feature_engine_profile()
    df, summary = build_phase_117_technical_indicator_expansion_handoff_report(profile)

    assert not df.empty
    assert len(df) >= 8
    assert summary["readiness_status"] == "READY"
    assert summary["target_phase"] == 117
    assert summary["current_phase"] == 116
    assert summary["target_final_phase"] == 160
    assert summary["all_items_ready"] is True
