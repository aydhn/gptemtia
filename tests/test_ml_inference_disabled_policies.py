"""Test suite for Phase 136 ML Inference Disabled Policies."""

import pytest
from advanced_gpu_ml_runtime.ml_inference_disabled_policies import (
    build_ml_inference_disabled_policy_registry,
)


def test_inference_disabled_policies():
    df, summary = build_ml_inference_disabled_policy_registry()
    assert not df.empty
    assert summary["inference_blocked"] is True
    assert summary["all_enforced"] is True
    assert summary["non_signal"] is True
