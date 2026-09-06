"""Tests for Regime Matrix Validation Acceptance."""

from advanced_regime_validation_acceptance.regime_matrix_validation_acceptance import (
    build_regime_matrix_validation_acceptance_report,
    summarize_regime_matrix_validation_acceptance,
)


def test_matrix_validation_acceptance():
    df, summary = build_regime_matrix_validation_acceptance_report()
    assert not df.empty
    assert summary["all_passed"] is True
    assert summary["component"] == "phase_127_regime_matrix"
    assert summary["non_signal"] is True
    assert summary["source_preserved"] is True

    s_df = summarize_regime_matrix_validation_acceptance(df)
    assert s_df["all_passed"] is True
