"""Test suite for Phase 137 Advanced ML Dataset Safety Boundaries."""

import pytest
from advanced_ml_dataset_registry.advanced_ml_dataset_safety_boundary import (
    build_advanced_ml_dataset_safety_boundary,
    build_advanced_ml_dataset_no_go_conditions,
    build_advanced_ml_dataset_safe_go_conditions,
    summarize_advanced_ml_dataset_safety_boundary,
)


def test_build_safety_boundaries():
    df, summary = build_advanced_ml_dataset_safety_boundary()
    assert not df.empty
    assert summary["no_go_count"] >= 20
    assert summary["safe_go_count"] >= 10
    assert summary["safety_status"] == "SECURE"
    assert summary["live_trading_prohibited"] is True
    assert summary["model_training_blocked"] is True


def test_no_go_and_safe_go_sets():
    df_ng, s_ng = build_advanced_ml_dataset_no_go_conditions()
    assert not df_ng.empty
    assert s_ng["all_enforced"] is True

    df_sg, s_sg = build_advanced_ml_dataset_safe_go_conditions()
    assert not df_sg.empty
    assert s_sg["all_active"] is True
