"""Test suite for Phase 137 Advanced ML Dataset Domain Registry."""

import pytest
from advanced_ml_dataset_registry.advanced_ml_dataset_domain_registry import (
    build_advanced_ml_dataset_domain_registry,
    summarize_advanced_ml_dataset_domains,
)


def test_build_domain_registry():
    df, summary = build_advanced_ml_dataset_domain_registry()
    assert not df.empty
    assert summary["total_domains"] >= 35
    assert summary["current_phase"] == 137
    assert summary["target_final_phase"] == 160
    assert summary["non_signal"] is True
