# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Attribution Drift Linkage."""

import pytest
from advanced_explainability_attribution.attribution_drift_linkage import (
    build_attribution_drift_linkage_registry,
    summarize_attribution_drift_linkage,
)


def test_attribution_drift_linkage():
    df, summary = build_attribution_drift_linkage_registry()
    assert len(df) == 4
    assert summary["all_linkage_contract"] is True
    assert summary["all_drift_calculated_false"] is True
    assert summary["all_non_signal"] is True
