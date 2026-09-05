from advanced_regime_rule_free.regime_candidate_state_validation_dependencies import (
    build_regime_candidate_state_validation_dependency_registry,
    summarize_candidate_state_validation_dependencies,
    VALIDATION_DEPENDENCIES,
)


def test_build_regime_candidate_state_validation_dependency_registry():
    df, summary = build_regime_candidate_state_validation_dependency_registry()
    assert len(df) == 6
    assert summary["total_validation_dependencies"] == 6
    assert summary["blocking_validation_count"] == 6
    assert summary["all_enforced"] is True
    assert summary["status"] == "VALID"

    val_ids = df["validation_id"].tolist()
    assert "val_phase_121_no_lookahead" in val_ids
    assert "val_forbidden_columns" in val_ids
    assert "val_timestamp_order" in val_ids
    assert "val_news_metadata_only" in val_ids
    assert "val_source_preservation" in val_ids
    assert "val_non_signal_compliance" in val_ids
