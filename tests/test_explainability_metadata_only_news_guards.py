# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Explainability Metadata-Only News Guards."""

import pytest
from advanced_explainability_attribution.explainability_metadata_only_news_guards import (
    verify_explainability_metadata_only_news_guards,
    summarize_explainability_metadata_only_news_guards,
)


def test_explainability_metadata_only_news_guards():
    df, summary = verify_explainability_metadata_only_news_guards()
    assert len(df) == 5
    assert summary["all_active"] is True
    assert summary["zero_violations"] is True
    assert summary["all_non_signal"] is True
