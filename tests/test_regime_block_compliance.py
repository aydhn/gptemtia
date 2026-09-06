"""Test suite for Phase 135 Regime Block Compliance."""

from advanced_regime_acceptance.regime_block_compliance import (
    build_regime_block_non_signal_compliance_report,
    build_regime_block_no_lookahead_compliance_report,
    build_regime_block_metadata_only_news_compliance_report,
    build_regime_block_forbidden_column_compliance_report,
    build_regime_block_source_preservation_report,
    build_regime_block_featurestore_readiness_report,
    summarize_regime_block_compliance,
)


def test_compliance_reports():
    df1, s1 = build_regime_block_non_signal_compliance_report()
    assert s1["all_compliant"] is True
    assert s1["non_signal"] is True

    df2, s2 = build_regime_block_no_lookahead_compliance_report()
    assert s2["all_compliant"] is True

    df3, s3 = build_regime_block_metadata_only_news_compliance_report()
    assert s3["all_compliant"] is True

    df4, s4 = build_regime_block_forbidden_column_compliance_report()
    assert s4["all_compliant"] is True

    df5, s5 = build_regime_block_source_preservation_report()
    assert s5["all_compliant"] is True

    df6, s6 = build_regime_block_featurestore_readiness_report()
    assert s6["all_compliant"] is True
    assert s6["official_approval"] is False
    assert s6["production_ready"] is False
    assert s6["broker_ready"] is False

    assert summarize_regime_block_compliance(df1)["all_compliant"] is True
