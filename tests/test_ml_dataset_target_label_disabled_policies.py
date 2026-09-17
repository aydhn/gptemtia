"""Test suite for Phase 137 ML Dataset Target Label Disabled Policies."""

import pytest
from advanced_ml_dataset_registry.ml_dataset_target_label_disabled_policies import (
    build_ml_dataset_target_label_disabled_policy_registry,
    validate_no_target_label_request,
    summarize_ml_dataset_target_label_disabled_policies,
)


def test_build_target_label_disabled_policies():
    df, summary = build_ml_dataset_target_label_disabled_policy_registry()
    assert not df.empty
    assert summary["target_label_generation_allowed"] is False
    assert summary["all_enforced"] is True


def test_validate_target_label_request():
    v_clean = validate_no_target_label_request("load historical feature metadata")
    assert v_clean["valid"] is True

    v_target = validate_no_target_label_request("create forward_return classification label")
    assert v_target["valid"] is False
