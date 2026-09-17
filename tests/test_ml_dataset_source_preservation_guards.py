"""Test suite for Phase 137 ML Dataset Source Preservation Guards."""

import pytest
from advanced_ml_dataset_registry.ml_dataset_source_preservation_guards import (
    build_ml_dataset_source_preservation_guard_registry,
    validate_ml_dataset_source_preservation_action,
    summarize_ml_dataset_source_preservation_guards,
)


def test_build_source_preservation_guards():
    df, summary = build_ml_dataset_source_preservation_guard_registry()
    assert not df.empty
    assert summary["total_sp_guards"] >= 5
    assert summary["non_signal"] is True


def test_validate_preservation_actions():
    v_clean = validate_ml_dataset_source_preservation_action("read_metadata")
    assert v_clean["valid"] is True

    v_bad = validate_ml_dataset_source_preservation_action("auto_impute_missing_values")
    assert v_bad["valid"] is False
