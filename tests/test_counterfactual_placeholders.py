# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Counterfactual Placeholders."""

import pytest
from advanced_explainability_attribution.counterfactual_placeholders import (
    build_counterfactual_placeholder_registry,
    summarize_counterfactual_placeholders,
)


def test_counterfactual_placeholders():
    df, summary = build_counterfactual_placeholder_registry()
    assert len(df) >= 3
    assert summary["all_placeholder_only"] is True
    assert summary["all_counterfactual_generated_false"] is True
    assert summary["all_non_signal"] is True
