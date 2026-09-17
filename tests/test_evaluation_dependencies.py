# -*- coding: utf-8 -*-
from advanced_benchmark_evaluation.benchmark_evaluation_config import get_default_benchmark_evaluation_profile
from advanced_benchmark_evaluation.evaluation_backtest_dependencies import build_evaluation_backtest_dependency_registry
from advanced_benchmark_evaluation.evaluation_walk_forward_dependencies import build_evaluation_walk_forward_dependency_registry
from advanced_benchmark_evaluation.evaluation_stress_dependencies import build_evaluation_stress_dependency_registry
from advanced_benchmark_evaluation.evaluation_monte_carlo_dependencies import build_evaluation_monte_carlo_dependency_registry
from advanced_benchmark_evaluation.evaluation_governance_dependencies import build_evaluation_governance_dependency_registry
from advanced_benchmark_evaluation.evaluation_benchmark_dependencies import build_evaluation_benchmark_dependency_registry

def test_build_evaluation_dependencies():
    profile = get_default_benchmark_evaluation_profile()
    deps = [
        build_evaluation_backtest_dependency_registry(profile),
        build_evaluation_walk_forward_dependency_registry(profile),
        build_evaluation_stress_dependency_registry(profile),
        build_evaluation_monte_carlo_dependency_registry(profile),
        build_evaluation_governance_dependency_registry(profile),
        build_evaluation_benchmark_dependency_registry(profile),
    ]
    for df, s in deps:
        assert not df.empty
        assert (df['dependency_status'] == 'SATISFIED').all()
        assert s['all_satisfied'] is True
