# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Explainability Candidate Model Dependencies."""

import pytest
from advanced_explainability_attribution.explainability_candidate_model_dependencies import (
    verify_explainability_candidate_model_dependencies,
    summarize_explainability_candidate_model_dependencies,
)


def test_explainability_candidate_model_dependencies():
    df, summary = verify_explainability_candidate_model_dependencies()
    assert len(df) == 4
    assert summary["all_contracts_verified"] is True
    assert summary["all_fit_executed_false"] is True
    assert summary["all_predict_executed_false"] is True
    assert summary["all_non_signal"] is True
