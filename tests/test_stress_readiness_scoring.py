# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Readiness Scoring."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_readiness_scoring import (
    build_stress_readiness_score_report,
    classify_stress_readiness_score,
)


def test_readiness_scoring():
    prof = get_default_stress_testing_profile()
    df, summary = build_stress_readiness_score_report(prof)
    assert not df.empty
    assert summary["score"] == 1.0
    assert summary["classification"] == "stress_testing_contract_ready_non_production"
    assert summary["meets_threshold"] is True
    assert summary["non_signal"] is True

    cls_str = classify_stress_readiness_score(0.85)
    assert "stress_testing_contract_ready" in cls_str
