# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Permutation Importance Placeholders."""

import pytest
from advanced_explainability_attribution.permutation_importance_placeholders import (
    build_permutation_importance_placeholder_registry,
    summarize_permutation_importance_placeholders,
)


def test_permutation_importance_placeholders():
    df, summary = build_permutation_importance_placeholder_registry()
    assert len(df) >= 3
    assert summary["all_placeholder_only"] is True
    assert summary["all_permutation_executed_false"] is True
    assert summary["all_non_signal"] is True
