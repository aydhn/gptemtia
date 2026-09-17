# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Explainability Safety Boundary."""

import pytest
from advanced_explainability_attribution.explainability_safety_boundary import (
    assert_safe_explainability_operation,
    check_all_safety_boundaries,
    ExplainabilitySafetyViolationError,
)


def test_explainability_safety_boundary():
    # Safe operation
    assert assert_safe_explainability_operation("check_profile_metadata") is True

    # Forbidden operation: train_model
    with pytest.raises(ExplainabilitySafetyViolationError):
        assert_safe_explainability_operation("train_model")

    # Forbidden operation: compute_shapley_values
    with pytest.raises(ExplainabilitySafetyViolationError):
        assert_safe_explainability_operation("compute_shapley_values")

    # Forbidden kwargs: live_trading
    with pytest.raises(ExplainabilitySafetyViolationError):
        assert_safe_explainability_operation("check_status", {"live_trading": True})

    # Forbidden kwargs: calculate_attribution
    with pytest.raises(ExplainabilitySafetyViolationError):
        assert_safe_explainability_operation("check_status", {"calculate_attribution": True})

    boundaries = check_all_safety_boundaries()
    assert boundaries["all_safe"] is True
    assert boundaries["current_phase"] == 143
    assert boundaries["next_phase"] == 144
