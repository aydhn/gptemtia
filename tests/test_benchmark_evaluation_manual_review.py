# -*- coding: utf-8 -*-
"""Phase 151 Unit Tests: Benchmark Evaluation Manual Review."""

from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    get_default_benchmark_evaluation_profile,
)
from advanced_benchmark_evaluation.benchmark_evaluation_manual_review import (
    build_benchmark_evaluation_manual_review_queue,
)


def test_benchmark_evaluation_manual_review():
    profile = get_default_benchmark_evaluation_profile()
    df, s = build_benchmark_evaluation_manual_review_queue(profile)

    assert not df.empty
    assert len(df) >= 7
    assert "review_id" in df.columns
    assert (df["mandatory"] == True).all()
    assert s["all_mandatory"] is True
    assert s["non_signal"] is True
