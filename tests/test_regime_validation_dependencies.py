from advanced_regime_foundation.regime_validation_dependencies import (
    build_regime_validation_dependency_registry,
    summarize_regime_validation_dependencies,
)


def test_regime_validation_dependencies():
    df, summary = build_regime_validation_dependency_registry()
    assert not df.empty
    assert summary["all_blocking"] is True
    assert summary["all_non_signal"] is True

    rules = list(df["validation_rule"])
    assert "no_forbidden_columns" in rules
    assert "no_lookahead_guarantee" in rules
    assert "no_target_or_prediction" in rules
    assert "monotonic_timestamp_order" in rules
    assert "metadata_only_news_context" in rules
    assert "source_preservation_invariant" in rules
    assert "non_signal_policy_compliance" in rules
    assert "feature_store_validation_status" in rules

    summ = summarize_regime_validation_dependencies(df)
    assert summ["total_rules"] == len(df)
    assert summ["all_blocking"] is True
