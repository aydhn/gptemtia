# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Explainability No-Lookahead Guards."""

import pytest
from advanced_explainability_attribution.explainability_no_lookahead_guards import (
    verify_explainability_no_lookahead_guards,
    summarize_explainability_no_lookahead_guards,
)


def test_explainability_no_lookahead_guards():
    df, summary = verify_explainability_no_lookahead_guards()
    assert len(df) == 4
    assert summary["all_active"] is True
    assert summary["zero_violations"] is True
    assert summary["all_non_signal"] is True
