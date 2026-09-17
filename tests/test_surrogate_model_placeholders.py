# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Surrogate Model Placeholders."""

import pytest
from advanced_explainability_attribution.surrogate_model_placeholders import (
    build_surrogate_model_placeholder_registry,
    summarize_surrogate_model_placeholders,
)


def test_surrogate_model_placeholders():
    df, summary = build_surrogate_model_placeholder_registry()
    assert len(df) >= 3
    assert summary["all_placeholder_only"] is True
    assert summary["all_surrogate_executed_false"] is True
    assert summary["all_non_signal"] is True
