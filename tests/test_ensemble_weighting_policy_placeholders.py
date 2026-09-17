# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Weighting Policy Placeholders."""

from advanced_ensemble_model_registry.ensemble_weighting_policy_placeholders import (
    build_ensemble_weighting_policy_placeholders,
    validate_ensemble_weighting_policy_placeholders,
    summarize_ensemble_weighting_policy_placeholders,
)


def test_ensemble_weighting_policy_placeholders():
    df, summary = build_ensemble_weighting_policy_placeholders()
    assert len(df) == 3
    assert summary["total_weighting_policies"] == 3
    assert summary["all_calculations_blocked"] is True
    assert summary["zero_weights_calculated"] is True
    assert summary["non_signal"] is True
    assert validate_ensemble_weighting_policy_placeholders(df, summary) is True
