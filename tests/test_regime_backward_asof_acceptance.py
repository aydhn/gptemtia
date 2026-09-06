"""Tests for Regime Backward Asof Acceptance."""

from advanced_regime_validation_acceptance.regime_backward_asof_acceptance import (
    build_regime_backward_asof_acceptance_report,
    validate_backward_asof_policy,
    summarize_regime_backward_asof_acceptance,
)


def test_backward_asof_acceptance():
    df, summary = build_regime_backward_asof_acceptance_report()
    assert not df.empty
    assert summary["all_passed"] is True
    assert summary["backward_only_enforced"] is True

    s_df = summarize_regime_backward_asof_acceptance(df)
    assert s_df["backward_only_enforced"] is True

    # Policy validation
    assert validate_backward_asof_policy("merge_asof(..., direction='backward')")["passed"] is True

    res_fwd = validate_backward_asof_policy("merge_asof(..., direction='forward')")
    assert res_fwd["passed"] is False

    res_nearest = validate_backward_asof_policy("merge_asof(..., direction='nearest')")
    assert res_nearest["passed"] is False
