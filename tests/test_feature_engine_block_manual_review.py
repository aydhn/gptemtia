from advanced_feature_factor_acceptance.feature_engine_block_manual_review import (
    build_feature_engine_block_manual_review_queue,
    summarize_feature_engine_block_manual_review_queue,
)

def test_feature_engine_block_manual_review():
    df, summary = build_feature_engine_block_manual_review_queue()
    assert not df.empty
    assert summary["destructive_actions_prevented"] is True
    assert summary["auto_imputation_prevented"] is True
    assert summary["auto_drop_prevented"] is True
    assert summary["non_signal"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False

    # Check that forbidden suggestions are never present in suggested_action
    forbidden_terms = ["delete file", "drop column", "overwrite", "auto-impute", "buy signal", "sell signal"]
    for action in df["suggested_action"].str.lower():
        for term in forbidden_terms:
            assert term not in action

    s = summarize_feature_engine_block_manual_review_queue(df)
    assert s["total_reviews"] == len(df)
    assert s["destructive_allowed"] is False
    assert s["non_signal"] is True
