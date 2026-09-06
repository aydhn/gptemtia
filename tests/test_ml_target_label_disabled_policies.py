"""Test suite for Phase 136 ML Target and Label Disabled Policies."""

import pytest
from advanced_gpu_ml_runtime.ml_target_label_disabled_policies import (
    build_ml_target_label_disabled_policy_registry,
)


def test_target_label_disabled_policies():
    df, summary = build_ml_target_label_disabled_policy_registry()
    assert not df.empty
    assert summary["target_label_blocked"] is True
    assert summary["all_enforced"] is True
    assert summary["non_signal"] is True
