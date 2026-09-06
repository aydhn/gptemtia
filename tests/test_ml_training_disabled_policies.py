"""Test suite for Phase 136 ML Training Disabled Policies."""

import pytest
from advanced_gpu_ml_runtime.ml_training_disabled_policies import (
    build_ml_training_disabled_policy_registry,
)


def test_training_disabled_policies():
    df, summary = build_ml_training_disabled_policy_registry()
    assert not df.empty
    assert summary["training_blocked"] is True
    assert summary["all_enforced"] is True
    assert summary["non_signal"] is True
