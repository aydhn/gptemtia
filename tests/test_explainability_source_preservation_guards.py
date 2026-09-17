# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Explainability Source Preservation Guards."""

import pytest
from advanced_explainability_attribution.explainability_source_preservation_guards import (
    verify_explainability_source_preservation_guards,
    summarize_explainability_source_preservation_guards,
)


def test_explainability_source_preservation_guards():
    df, summary = verify_explainability_source_preservation_guards()
    assert len(df) == 4
    assert summary["all_active"] is True
    assert summary["zero_violations"] is True
    assert summary["all_non_signal"] is True
