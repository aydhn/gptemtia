# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Feature Quality Drift Linkage."""

import pytest
from advanced_model_drift_monitoring.feature_quality_drift_linkage import (
    build_feature_quality_drift_linkages,
    validate_feature_quality_drift_linkage,
)


def test_feature_quality_drift_linkages():
    links = build_feature_quality_drift_linkages()
    assert len(links) >= 3
    for link in links:
        val = validate_feature_quality_drift_linkage(link)
        assert val["valid"] is True
