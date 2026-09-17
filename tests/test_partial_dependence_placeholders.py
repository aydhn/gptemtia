# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Partial Dependence Placeholders."""

import pytest
from advanced_explainability_attribution.partial_dependence_placeholders import (
    build_partial_dependence_placeholder_registry,
    summarize_partial_dependence_placeholders,
)


def test_partial_dependence_placeholders():
    df, summary = build_partial_dependence_placeholder_registry()
    assert len(df) >= 3
    assert summary["all_placeholder_only"] is True
    assert summary["all_pdp_executed_false"] is True
    assert summary["all_non_signal"] is True
