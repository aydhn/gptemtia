# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Feature Attribution Contracts."""

import pytest
from advanced_explainability_attribution.feature_attribution_contracts import (
    build_feature_attribution_contract_registry,
    validate_feature_attribution_contract,
    summarize_feature_attribution_contracts,
)


def test_feature_attribution_contracts():
    df, summary = build_feature_attribution_contract_registry()
    assert len(df) == 8
    assert summary["all_zero_calculation"] is True
    assert summary["all_zero_shap"] is True
    assert summary["all_zero_lime"] is True

    for _, row in df.iterrows():
        val = validate_feature_attribution_contract(row.to_dict())
        assert val["is_valid"] is True
