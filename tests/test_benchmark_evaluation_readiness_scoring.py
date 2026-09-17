# -*- coding: utf-8 -*-
"""Phase 151 Unit Tests: Readiness Scoring."""

from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    get_default_benchmark_evaluation_profile,
)
from advanced_benchmark_evaluation.benchmark_evaluation_readiness_scoring import (
    calculate_benchmark_evaluation_readiness_score,
    build_benchmark_evaluation_readiness_score_report,
)


def test_readiness_scoring():
    profile = get_default_benchmark_evaluation_profile()
    res = calculate_benchmark_evaluation_readiness_score(None, profile)
    assert res.score >= 0.75
    assert res.meets_threshold is True
    assert res.classification == "benchmark_evaluation_contract_ready_non_production"

    df, s = build_benchmark_evaluation_readiness_score_report(profile)
    assert not df.empty
    assert s["score"] >= 0.75
    assert s["meets_threshold"] is True
