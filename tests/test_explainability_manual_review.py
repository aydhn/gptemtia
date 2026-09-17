# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Explainability Manual Review Queue."""

import pytest
from advanced_explainability_attribution.explainability_manual_review import (
    build_explainability_manual_review_queue,
    summarize_explainability_manual_review,
)


def test_explainability_manual_review():
    df, summary = build_explainability_manual_review_queue()
    assert len(df) == 4
    assert summary["all_pending"] is True
    assert summary["all_manual_review_required"] is True
    assert summary["all_non_signal"] is True
