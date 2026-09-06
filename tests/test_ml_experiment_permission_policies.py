"""Test suite for Phase 136 ML Experiment Permission Policies."""

import pytest
from advanced_gpu_ml_runtime.ml_experiment_permission_policies import (
    build_ml_experiment_permission_policy_registry,
)


def test_build_ml_experiment_permission_policy_registry():
    df, summary = build_ml_experiment_permission_policy_registry()
    assert not df.empty
    assert summary["total_policies"] > 0
    assert summary["blocked_now_count"] > 0
    assert summary["allowed_now_count"] > 0
    assert summary["non_signal"] is True
