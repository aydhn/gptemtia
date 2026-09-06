"""Tests for Regime Validation Acceptance Safety Boundary."""

from advanced_regime_validation_acceptance.regime_validation_acceptance_safety_boundary import (
    build_regime_validation_acceptance_safety_boundary,
    build_regime_validation_acceptance_no_go_conditions,
    build_regime_validation_acceptance_safe_go_conditions,
    summarize_regime_validation_acceptance_safety_boundary,
    NO_GO_CONDITIONS,
    SAFE_GO_CONDITIONS,
)


def test_safety_boundary():
    assert len(NO_GO_CONDITIONS) >= 19
    assert len(SAFE_GO_CONDITIONS) >= 12

    no_go_df = build_regime_validation_acceptance_no_go_conditions()
    assert len(no_go_df) >= 19
    assert (no_go_df["enforced"] == True).all()
    assert (no_go_df["violated"] == False).all()

    safe_go_df = build_regime_validation_acceptance_safe_go_conditions()
    assert len(safe_go_df) >= 12
    assert (safe_go_df["permitted"] == True).all()

    df, summary = build_regime_validation_acceptance_safety_boundary()
    assert not df.empty
    assert summary["safety_status"] == "SECURE"
    assert summary["non_signal"] is True

    s_df = summarize_regime_validation_acceptance_safety_boundary(df)
    assert s_df["safety_status"] == "SECURE"
