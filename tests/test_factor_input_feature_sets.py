import pytest
from advanced_factor_metadata.factor_input_feature_sets import (
    build_factor_input_feature_set_registry,
    summarize_factor_input_feature_sets,
)


def test_build_factor_input_feature_set_registry():
    df, summary = build_factor_input_feature_set_registry()
    assert not df.empty
    assert summary["total_feature_sets"] == 12
    assert summary["total_required_features"] > 0
    assert summary["non_signal"] is True

    assert "required_features" in df.columns
    assert "source_phase_refs" in df.columns

    # Verify source phases reference Phases 116-121
    all_refs = []
    for refs in df["source_phase_refs"]:
        all_refs.extend(refs)
    assert any("Phase 117" in r or "Phase 118" in r or "Phase 119" in r or "Phase 120" in r for r in all_refs)

    stats = summarize_factor_input_feature_sets(df)
    assert stats["total_feature_sets"] == 12
    assert stats["non_signal"] is True
