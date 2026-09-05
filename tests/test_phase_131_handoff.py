"""Tests for Phase 131 Cross-Asset Regime Context Handoff."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.phase_131_handoff import (
    build_phase_131_cross_asset_regime_context_handoff_report,
    summarize_phase_131_handoff,
    HANDOFF_ITEMS,
)


def test_build_phase_131_cross_asset_regime_context_handoff_report():
    profile = get_default_regime_transition_profile()
    df, summary = build_phase_131_cross_asset_regime_context_handoff_report(profile)

    assert not df.empty
    assert len(df) == 9
    assert "handoff_item" in df.columns
    assert "status" in df.columns
    assert (df["status"] == "READY").all()


    assert summary["handoff_status"] == "READY"
    assert summary["source_phase"] == 130
    assert summary["next_phase"] == 131
    assert summary["target_final_phase"] == 160
    assert summary["all_ready"] is True


def test_summarize_phase_131_handoff():
    profile = get_default_regime_transition_profile()
    df, _ = build_phase_131_cross_asset_regime_context_handoff_report(profile)
    summary = summarize_phase_131_handoff(df)
    assert summary["handoff_status"] == "READY"
    assert summary["all_ready"] is True
