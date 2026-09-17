# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Global Explanation Contracts."""

import pytest
from advanced_explainability_attribution.global_explanation_contracts import (
    build_global_explanation_contract_registry,
    summarize_global_explanation_contracts,
)


def test_global_explanation_contracts():
    df, summary = build_global_explanation_contract_registry()
    assert len(df) >= 3
    assert summary["all_zero_calculation"] is True
    assert summary["all_non_signal"] is True
    assert summary["current_phase"] == 143
