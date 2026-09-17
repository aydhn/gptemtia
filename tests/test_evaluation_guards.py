# -*- coding: utf-8 -*-
"""Phase 151 Unit Tests: Evaluation Guards."""

from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    get_default_benchmark_evaluation_profile,
)
from advanced_benchmark_evaluation.evaluation_no_lookahead_guards import build_evaluation_no_lookahead_guard_registry
from advanced_benchmark_evaluation.evaluation_result_claim_guards import build_evaluation_result_claim_guard_registry
from advanced_benchmark_evaluation.evaluation_performance_claim_guards import build_evaluation_performance_claim_guard_registry
from advanced_benchmark_evaluation.evaluation_strategy_approval_guards import build_evaluation_strategy_approval_guard_registry
from advanced_benchmark_evaluation.evaluation_benchmark_selection_bias_guards import build_evaluation_benchmark_selection_bias_guard_registry
from advanced_benchmark_evaluation.evaluation_data_snooping_bias_guards import build_evaluation_data_snooping_bias_guard_registry
from advanced_benchmark_evaluation.evaluation_overfitting_guards import build_evaluation_overfitting_guard_registry
from advanced_benchmark_evaluation.evaluation_multiple_testing_guards import build_evaluation_multiple_testing_guard_registry
from advanced_benchmark_evaluation.evaluation_metadata_only_news_guards import build_evaluation_metadata_only_news_guard_registry
from advanced_benchmark_evaluation.evaluation_source_preservation_guards import build_evaluation_source_preservation_guard_registry


def test_build_evaluation_guards():
    profile = get_default_benchmark_evaluation_profile()
    guards = [
        build_evaluation_no_lookahead_guard_registry(profile),
        build_evaluation_result_claim_guard_registry(profile),
        build_evaluation_performance_claim_guard_registry(profile),
        build_evaluation_strategy_approval_guard_registry(profile),
        build_evaluation_benchmark_selection_bias_guard_registry(profile),
        build_evaluation_data_snooping_bias_guard_registry(profile),
        build_evaluation_overfitting_guard_registry(profile),
        build_evaluation_multiple_testing_guard_registry(profile),
        build_evaluation_metadata_only_news_guard_registry(profile),
        build_evaluation_source_preservation_guard_registry(profile),
    ]

    for df, s in guards:
        assert not df.empty
        assert (df["is_active"] == True).all()
        assert s["all_active"] is True
        assert s["non_signal"] is True
