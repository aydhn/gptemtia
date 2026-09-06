"""Test suite for Phase 135 Block Status."""

from advanced_regime_acceptance.regime_block_status import (
    build_regime_block_status_report,
    summarize_regime_block_status,
)


def test_block_status():
    df, summary = build_regime_block_status_report()
    assert not df.empty
    assert summary["phase_start"] == 126
    assert summary["phase_end"] == 135
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 136
    assert summary["overall_status"] == "acceptance_pass"
    assert summary["non_signal"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False

    s2 = summarize_regime_block_status(df)
    assert s2["overall_status"] == "acceptance_pass"
