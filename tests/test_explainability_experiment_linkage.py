# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Explainability Experiment Linkage."""

import pytest
from advanced_explainability_attribution.explainability_experiment_linkage import (
    build_explainability_experiment_linkage_registry,
    summarize_explainability_experiment_linkage,
)


def test_explainability_experiment_linkage():
    df, summary = build_explainability_experiment_linkage_registry()
    assert len(df) == 3
    assert summary["all_linked"] is True
    assert summary["all_non_signal"] is True
