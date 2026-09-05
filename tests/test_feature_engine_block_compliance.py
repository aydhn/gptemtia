from advanced_feature_factor_acceptance.feature_engine_block_compliance import (
    build_feature_engine_block_non_signal_compliance_report,
    build_feature_engine_block_no_lookahead_compliance_report,
    build_feature_engine_block_forbidden_column_compliance_report,
    build_feature_engine_block_news_metadata_only_compliance_report,
    build_feature_engine_block_source_preservation_report,
    build_feature_engine_block_feature_store_readiness_report,
    summarize_feature_engine_block_compliance,
)

def test_feature_engine_block_compliance():
    df_ns, s_ns = build_feature_engine_block_non_signal_compliance_report()
    assert s_ns["compliant_modules"] == 10
    assert s_ns["non_signal"] is True
    assert s_ns["contains_trading_recommendation"] is False

    df_la, s_la = build_feature_engine_block_no_lookahead_compliance_report()
    assert s_la["compliant_modules"] == 10
    assert s_la["lookahead_detected"] is False

    df_fc, s_fc = build_feature_engine_block_forbidden_column_compliance_report()
    assert s_fc["compliant_modules"] == 10
    assert s_fc["forbidden_columns_detected"] == 0

    df_nm, s_nm = build_feature_engine_block_news_metadata_only_compliance_report()
    assert s_nm["compliant_modules"] == 10
    assert s_nm["full_article_detected"] is False

    df_sp, s_sp = build_feature_engine_block_source_preservation_report()
    assert s_sp["compliant_modules"] == 10
    assert s_sp["source_preserved"] is True

    df_sr, s_sr = build_feature_engine_block_feature_store_readiness_report()
    assert s_sr["aligned_modules"] == 10
    assert s_sr["production_approval"] is False
    assert s_sr["broker_ready"] is False

    s = summarize_feature_engine_block_compliance(df_ns)
    assert s["all_verified"] is True
    assert s["non_signal"] is True
