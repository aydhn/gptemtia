# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Explainability Validation Dependencies."""

import pytest
from advanced_explainability_attribution.explainability_validation_dependencies import (
    verify_explainability_validation_dependencies,
    summarize_explainability_validation_dependencies,
)


def test_explainability_validation_dependencies():
    df, summary = verify_explainability_validation_dependencies()
    assert len(df) == 5
    assert summary["all_satisfied"] is True
    assert summary["all_non_signal"] is True
