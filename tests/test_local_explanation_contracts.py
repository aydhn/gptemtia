# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Local Explanation Contracts."""

import pytest
from advanced_explainability_attribution.local_explanation_contracts import (
    build_local_explanation_contract_registry,
    summarize_local_explanation_contracts,
)


def test_local_explanation_contracts():
    df, summary = build_local_explanation_contract_registry()
    assert len(df) >= 3
    assert summary["all_zero_calculation"] is True
    assert summary["all_non_signal"] is True
    assert summary["current_phase"] == 143
