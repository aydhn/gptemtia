from advanced_market_behavior_diagnostics.behavior_quality_findings import (
    build_behavior_quality_findings_registry,
    summarize_behavior_quality_findings,
    CORE_BEHAVIOR_QUALITY_FINDINGS,
)


def test_behavior_quality_findings():
    df, summary = build_behavior_quality_findings_registry()

    assert not df.empty
    assert len(df) == len(CORE_BEHAVIOR_QUALITY_FINDINGS)
    assert "finding_id" in df.columns
    assert summary["destructive_action_allowed"] is False
    assert summary["auto_fix_allowed"] is False
    assert summary["auto_drop_allowed"] is False
    assert summary["non_signal"] is True
