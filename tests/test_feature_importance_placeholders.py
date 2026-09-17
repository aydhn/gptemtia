# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Feature Importance Placeholders."""

import pytest
from advanced_explainability_attribution.feature_importance_placeholders import (
    build_feature_importance_placeholder_registry,
    summarize_feature_importance_placeholders,
)


def test_feature_importance_placeholders():
    df, summary = build_feature_importance_placeholder_registry()
    assert len(df) >= 3
    assert summary["all_placeholder_only"] is True
    assert summary["all_feature_importance_calculated_false"] is True
    assert summary["all_non_signal"] is True
