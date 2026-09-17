# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Explainability Report Contracts."""

import pytest
from advanced_explainability_attribution.explainability_report_contracts import (
    build_explainability_report_contract_registry,
    validate_explainability_report_contract,
    summarize_explainability_report_contracts,
)


def test_explainability_report_contracts():
    df, summary = build_explainability_report_contract_registry()
    assert len(df) == 7
    assert summary["all_zero_calculation"] is True
    assert summary["all_non_signal"] is True
    assert summary["all_manual_review_required"] is True

    for _, row in df.iterrows():
        val = validate_explainability_report_contract(row.to_dict())
        assert val["is_valid"] is True
