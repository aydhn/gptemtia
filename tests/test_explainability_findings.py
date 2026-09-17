# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Explainability Findings."""

import pytest
from advanced_explainability_attribution.explainability_findings import (
    build_explainability_findings_registry,
    summarize_explainability_findings,
)


def test_explainability_findings():
    df, summary = build_explainability_findings_registry()
    assert len(df) == 4
    assert summary["all_info_severity"] is True
    assert summary["all_manual_review_required"] is True
    assert summary["all_non_signal"] is True
