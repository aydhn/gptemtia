"""Tests for Regime Source Preservation Acceptance."""

from advanced_regime_validation_acceptance.regime_source_preservation_acceptance import (
    build_regime_source_preservation_acceptance_report,
    validate_source_preservation_action,
    summarize_source_preservation_acceptance,
    FORBIDDEN_SOURCE_ACTIONS,
)


def test_source_preservation_acceptance():
    df, summary = build_regime_source_preservation_acceptance_report()
    assert not df.empty
    assert summary["source_preservation_enforced"] is True

    s_df = summarize_source_preservation_acceptance(df)
    assert s_df["all_prohibited"] is True

    # Validate forbidden actions
    for action in FORBIDDEN_SOURCE_ACTIONS:
        res = validate_source_preservation_action(action)
        assert res["passed"] is False

    # Validate permitted action
    assert validate_source_preservation_action("read_only_query")["passed"] is True
