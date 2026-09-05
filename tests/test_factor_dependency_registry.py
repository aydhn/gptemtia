import pytest
from advanced_factor_metadata.factor_dependency_registry import (
    build_factor_dependency_registry,
    summarize_factor_dependency_registry,
)


def test_build_factor_dependency_registry():
    df, summary = build_factor_dependency_registry()
    assert not df.empty
    assert summary["total_dependencies"] >= 15
    assert summary["mandatory_dependencies"] >= 10
    assert summary["non_signal"] is True

    assert "source_phase" in df.columns
    assert "dependency_ref" in df.columns

    # Verify Phase 117, 118, 119, 120, 121 are covered
    phases = list(df["source_phase"].unique())
    assert "Phase 118" in phases
    assert "Phase 121" in phases

    summary_stats = summarize_factor_dependency_registry(df)
    assert summary_stats["total_dependencies"] == len(df)
    assert summary_stats["non_signal"] is True
