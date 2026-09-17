# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Drift Readiness Scoring."""

import pytest
from advanced_model_drift_monitoring.drift_readiness_scoring import (
    compute_domain_readiness_scores,
    evaluate_aggregate_drift_readiness,
)


def test_drift_readiness_scoring():
    scores = compute_domain_readiness_scores()
    assert len(scores) == 6
    eval_res = evaluate_aggregate_drift_readiness(scores)
    assert eval_res["overall_score"] == 100.0
    assert eval_res["overall_status"] == "ready"
    assert eval_res["all_ready"] is True
    assert eval_res["total_blockers"] == 0
