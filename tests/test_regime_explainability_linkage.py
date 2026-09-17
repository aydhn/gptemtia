# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Regime Explainability Linkage."""

import pytest
from advanced_explainability_attribution.regime_explainability_linkage import (
    build_regime_explainability_linkage_registry,
    summarize_regime_explainability_linkage,
)


def test_regime_explainability_linkage():
    df, summary = build_regime_explainability_linkage_registry()
    assert len(df) == 4
    assert summary["all_linkage_contract"] is True
    assert summary["all_non_signal"] is True
