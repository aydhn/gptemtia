# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Drift Experiment Linkage."""

import pytest
from advanced_model_drift_monitoring.drift_experiment_linkage import build_drift_experiment_linkages


def test_drift_experiment_linkages():
    links = build_drift_experiment_linkages()
    assert len(links) == 3
    for link in links:
        assert link["status"] == "linked"
