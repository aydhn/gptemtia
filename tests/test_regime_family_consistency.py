from advanced_market_behavior_diagnostics.regime_family_consistency import (
    build_regime_family_consistency_report,
    summarize_regime_family_consistency,
)


def test_regime_family_consistency():
    df, summary = build_regime_family_consistency_report()

    assert not df.empty
    assert "family_name" in df.columns
    assert "consistency_score" in df.columns
    assert summary["average_consistency"] >= 0.90
    assert summary["total_blockers"] == 0
    assert summary["non_signal"] is True
