import pytest
from advanced_factor_metadata.factor_validation_dependencies import (
    build_factor_validation_dependency_registry,
    summarize_factor_validation_dependencies,
)


def test_build_factor_validation_dependency_registry():
    df, summary = build_factor_validation_dependency_registry()
    assert not df.empty
    assert summary["total_validation_dependencies"] >= 8
    assert summary["critical_checks"] >= 3
    assert summary["non_signal"] is True

    check_ids = list(df["check_id"])
    assert "val_dep_no_lookahead" in check_ids
    assert "val_dep_forbidden_columns" in check_ids
    assert "val_dep_news_metadata_only" in check_ids
    assert "val_dep_warmup_nan" in check_ids

    stats = summarize_factor_validation_dependencies(df)
    assert stats["total_rules"] == len(df)
    assert stats["non_signal"] is True
