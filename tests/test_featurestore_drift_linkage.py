# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 FeatureStore Drift Linkage."""

import pytest
from advanced_model_drift_monitoring.featurestore_drift_linkage import (
    build_featurestore_drift_linkages,
    validate_featurestore_drift_linkage,
)


def test_featurestore_drift_linkages():
    links = build_featurestore_drift_linkages()
    assert len(links) >= 3
    for link in links:
        val = validate_featurestore_drift_linkage(link)
        assert val["valid"] is True
