# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Regime Drift Linkage."""

import pytest
from advanced_model_drift_monitoring.regime_drift_linkage import (
    build_regime_drift_linkages,
    validate_regime_drift_linkage,
)


def test_regime_drift_linkages():
    links = build_regime_drift_linkages()
    assert len(links) >= 3
    for link in links:
        val = validate_regime_drift_linkage(link)
        assert val["valid"] is True
