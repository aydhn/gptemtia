"""Tests for Transition Validation Acceptance."""

from advanced_regime_validation_acceptance.transition_validation_acceptance import (
    build_transition_validation_acceptance_report,
    summarize_transition_validation_acceptance,
)


def test_transition_validation_acceptance():
    df, summary = build_transition_validation_acceptance_report()
    assert not df.empty
    assert summary["all_passed"] is True
    assert summary["component"] == "phase_130_regime_transition"
    assert summary["non_signal"] is True

    s_df = summarize_transition_validation_acceptance(df)
    assert s_df["all_passed"] is True
