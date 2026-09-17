"""Test suite for Phase 137 ML Dataset Quality Gates."""

import pytest
from advanced_ml_dataset_registry.ml_dataset_quality_gates import (
    build_ml_dataset_quality_gate_registry,
    summarize_ml_dataset_quality_gates,
)


def test_build_quality_gates():
    df, summary = build_ml_dataset_quality_gate_registry()
    assert not df.empty
    assert summary["total_quality_gates"] >= 8
    assert summary["all_mandatory"] is True
