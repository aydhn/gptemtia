# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Drift Candidate Model Dependencies."""

import pytest
from advanced_model_drift_monitoring.drift_candidate_model_dependencies import check_drift_candidate_model_dependencies


def test_drift_candidate_model_dependencies():
    res = check_drift_candidate_model_dependencies()
    assert res["status"] == "satisfied"
    assert res["all_satisfied"] is True
    assert res["total_checks"] == 2
