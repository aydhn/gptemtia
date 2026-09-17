# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Explainability Ensemble Dependencies."""

import pytest
from advanced_explainability_attribution.explainability_ensemble_dependencies import (
    verify_explainability_ensemble_dependencies,
    summarize_explainability_ensemble_dependencies,
)


def test_explainability_ensemble_dependencies():
    df, summary = verify_explainability_ensemble_dependencies()
    assert len(df) == 4
    assert summary["all_contracts_verified"] is True
    assert summary["all_predict_executed_false"] is True
    assert summary["all_rebalance_executed_false"] is True
    assert summary["all_non_signal"] is True
