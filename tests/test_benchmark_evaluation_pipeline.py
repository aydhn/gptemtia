# -*- coding: utf-8 -*-
"""Phase 151 Unit Tests: Benchmark Evaluation Pipeline."""

from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    get_default_benchmark_evaluation_profile,
)
from advanced_benchmark_evaluation.benchmark_evaluation_pipeline import (
    BenchmarkEvaluationPipeline,
)


def test_benchmark_evaluation_pipeline():
    profile = get_default_benchmark_evaluation_profile()
    pipeline = BenchmarkEvaluationPipeline(profile=profile)

    status_df, summary = pipeline.build_benchmark_evaluation_status(save=False)

    assert not status_df.empty
    assert len(status_df) == 9
    assert summary["all_stages_ready"] is True
    assert summary["non_signal"] is True
    assert summary["current_phase"] == 151
    assert summary["next_phase"] == 152
