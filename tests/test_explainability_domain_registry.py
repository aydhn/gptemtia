# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Explainability Domain Registry."""

import pytest
from advanced_explainability_attribution.explainability_domain_registry import (
    build_explainability_domain_registry,
    summarize_explainability_domains,
)


def test_explainability_domain_registry():
    df, summary = build_explainability_domain_registry()
    assert len(df) >= 9
    assert summary["all_non_signal"] is True
    assert summary["all_zero_calculation"] is True
    assert summary["current_phase"] == 143
    assert summary["next_phase"] == 144
    assert summary["target_final_phase"] == 160
