# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Drift Explainability Linkage."""

import pytest
from advanced_explainability_attribution.drift_explainability_linkage import (
    build_drift_explainability_linkage_registry,
    summarize_drift_explainability_linkage,
)


def test_drift_explainability_linkage():
    df, summary = build_drift_explainability_linkage_registry()
    assert len(df) == 3
    assert summary["all_linkage_contract"] is True
    assert summary["all_investigation_blocked"] is True
    assert summary["all_non_signal"] is True
