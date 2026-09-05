from advanced_feature_factor_acceptance.feature_engine_block_safety_boundary import (
    build_feature_engine_block_safety_boundary_report,
    build_feature_engine_block_no_go_conditions,
    build_feature_engine_block_safe_go_conditions,
    summarize_feature_engine_block_safety_boundary,
)

def test_feature_engine_block_safety_boundary():
    df_nogo = build_feature_engine_block_no_go_conditions()
    assert len(df_nogo) >= 15
    assert df_nogo["enforced"].all()

    df_safego = build_feature_engine_block_safe_go_conditions()
    assert len(df_safego) >= 7
    assert df_safego["active"].all()

    df, summary = build_feature_engine_block_safety_boundary_report()
    assert summary["all_no_go_enforced"] is True
    assert summary["all_safe_go_active"] is True
    assert summary["non_signal"] is True
    assert summary["source_preserved"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False

    s = summarize_feature_engine_block_safety_boundary(df)
    assert s["secure"] is True
    assert s["no_go_rules"] >= 15
    assert s["safe_go_rules"] >= 7
