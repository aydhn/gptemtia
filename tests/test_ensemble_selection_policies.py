# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Selection Policies."""

from advanced_ensemble_model_registry.ensemble_selection_policies import (
    build_ensemble_selection_policies,
    validate_ensemble_selection_policies,
    validate_ensemble_selection_request,
    summarize_ensemble_selection_policies,
)


def test_ensemble_selection_policies():
    df, summary = build_ensemble_selection_policies()
    assert len(df) == 3
    assert summary["total_policies"] == 3
    assert summary["all_selection_blocked"] is True
    assert summary["zero_selection_executed"] is True
    assert summary["all_scores_non_signal"] is True
    assert summary["non_signal"] is True
    assert validate_ensemble_selection_policies(df, summary) is True


def test_validate_ensemble_selection_request():
    safe = {"policy_name": "diversity_based_selection_policy", "action": "inspect"}
    res_safe = validate_ensemble_selection_request(safe)
    assert res_safe["selection_allowed"] is False
    assert res_safe["blocked"] is False

    unsafe = {"policy_name": "diversity_based_selection_policy", "action": "select_best_models"}
    res_unsafe = validate_ensemble_selection_request(unsafe)
    assert res_unsafe["selection_allowed"] is False
    assert res_unsafe["blocked"] is True
