# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Forbidden Column Policies."""

from advanced_ensemble_model_registry.ensemble_forbidden_column_policies import (
    get_ensemble_forbidden_column_patterns,
    check_columns_against_ensemble_policy,
    summarize_ensemble_forbidden_column_policy,
)


def test_ensemble_forbidden_column_policies():
    patterns = get_ensemble_forbidden_column_patterns()
    assert len(patterns) >= 10
    assert "target" in patterns
    assert "signal" in patterns

    safe_cols = ["open", "high", "low", "close", "volume", "rsi_14", "macd"]
    res_safe = check_columns_against_ensemble_policy(safe_cols)
    assert res_safe["policy_passed"] is True
    assert res_safe["violations_count"] == 0

    unsafe_cols = ["close", "target_return_5d", "order_size", "embedding_vector"]
    res_unsafe = check_columns_against_ensemble_policy(unsafe_cols)
    assert res_unsafe["policy_passed"] is False
    assert res_unsafe["violations_count"] == 3

    summary = summarize_ensemble_forbidden_column_policy()
    assert summary["enforced"] is True
