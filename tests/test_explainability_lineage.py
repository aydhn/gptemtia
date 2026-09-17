# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Explainability Lineage."""

import pytest
from advanced_explainability_attribution.explainability_lineage import (
    build_explainability_lineage_registry,
    summarize_explainability_lineage,
)


def test_explainability_lineage():
    df, summary = build_explainability_lineage_registry()
    assert len(df) >= 5
    assert summary["all_verified"] is True
    assert summary["all_non_signal"] is True
