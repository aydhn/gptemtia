"""Tests for Regime Validation Findings."""

from advanced_regime_validation_acceptance.regime_validation_findings import (
    build_regime_validation_findings_registry,
    create_regime_validation_finding,
    summarize_regime_validation_findings,
    FINDING_TYPES,
)


def test_validation_findings():
    assert len(FINDING_TYPES) >= 10

    df, summary = build_regime_validation_findings_registry()
    assert not df.empty
    assert summary["destructive_action_allowed"] is False
    assert summary["critical_blockers"] == 0

    s_df = summarize_regime_validation_findings(df)
    assert s_df["destructive_action_allowed"] is False

    finding = create_regime_validation_finding(
        finding_type="no_lookahead_acceptance_blocker",
        acceptance_domain="no_lookahead_acceptance_domain",
        severity_label="acceptance_critical",
        message="test msg",
        recommendation="test rec",
    )
    assert finding.destructive_action_allowed is False
    assert finding.auto_fix_allowed is False
    assert finding.auto_drop_allowed is False
