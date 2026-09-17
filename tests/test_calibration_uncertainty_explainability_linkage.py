# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Calibration Uncertainty Explainability Linkage."""

import pytest
from advanced_explainability_attribution.calibration_uncertainty_explainability_linkage import (
    build_calibration_uncertainty_explainability_linkage_registry,
    summarize_calibration_uncertainty_explainability_linkage,
)


def test_calibration_uncertainty_explainability_linkage():
    df, summary = build_calibration_uncertainty_explainability_linkage_registry()
    assert len(df) == 3
    assert summary["all_linkage_contract"] is True
    assert summary["all_calibration_linked"] is True
    assert summary["all_non_signal"] is True
