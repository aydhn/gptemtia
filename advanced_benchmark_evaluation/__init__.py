# -*- coding: utf-8 -*-
"""Phase 151: Benchmark Comparison and Strategy Evaluation Reports Package.

Provides local/offline report contracts, summary placeholders, uncalculated metric placeholders,
claim boundaries, and Phase 152 handoff mechanisms.
Strictly offline, non-signal, and non-production. Zero live execution.
"""

from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    BenchmarkEvaluationProfile,
    get_benchmark_evaluation_profile,
    list_benchmark_evaluation_profiles,
    get_default_benchmark_evaluation_profile,
)

__all__ = [
    "BenchmarkEvaluationProfile",
    "get_benchmark_evaluation_profile",
    "list_benchmark_evaluation_profiles",
    "get_default_benchmark_evaluation_profile",
]
