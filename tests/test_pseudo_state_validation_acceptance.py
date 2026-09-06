"""Tests for Pseudo-State Validation Acceptance."""

from advanced_regime_validation_acceptance.pseudo_state_validation_acceptance import (
    build_pseudo_state_validation_acceptance_report,
    summarize_pseudo_state_validation_acceptance,
)


def test_pseudo_state_validation_acceptance():
    df, summary = build_pseudo_state_validation_acceptance_report()
    assert not df.empty
    assert summary["all_passed"] is True
    assert summary["component"] == "phase_128_pseudo_state"
    assert summary["non_signal"] is True

    s_df = summarize_pseudo_state_validation_acceptance(df)
    assert s_df["all_passed"] is True
