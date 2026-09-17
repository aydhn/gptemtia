# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Explainability Forbidden Column Policies."""

import pytest
from advanced_explainability_attribution.explainability_forbidden_column_policies import (
    build_forbidden_column_policy_registry,
    summarize_forbidden_column_policies,
    check_forbidden_columns,
)


def test_explainability_forbidden_column_policies():
    df, summary = build_forbidden_column_policy_registry()
    assert len(df) >= 10
    assert summary["all_enforced"] is True
    assert summary["all_non_signal"] is True

    valid_cols = ["brent_crude_close", "gold_volume", "macro_cpi_rate"]
    ok_valid, viols_valid = check_forbidden_columns(valid_cols)
    assert ok_valid is True
    assert len(viols_valid) == 0

    invalid_cols = ["future_price", "article_body", "trade_signal"]
    ok_invalid, viols_invalid = check_forbidden_columns(invalid_cols)
    assert ok_invalid is False
    assert len(viols_invalid) == 3
