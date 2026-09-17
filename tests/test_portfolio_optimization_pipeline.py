# -*- coding: utf-8 -*-
"""Unit tests for Phase 154 Portfolio Optimization Pipeline."""

from advanced_portfolio_optimization.portfolio_optimization_config import (
    get_default_portfolio_optimization_profile,
)
from advanced_portfolio_optimization.portfolio_optimization_pipeline import (
    PortfolioOptimizationPipeline,
)


def test_pipeline_stages_execution():
    profile = get_default_portfolio_optimization_profile()
    pipeline = PortfolioOptimizationPipeline(profile=profile)

    # Stage 1
    tables_1, sum_1 = pipeline.build_profiles_domains_scope(save=False)
    assert "profiles" in tables_1
    assert "domains" in tables_1
    assert "scopes" in tables_1

    # Stage 2
    tables_2, sum_2 = pipeline.build_optimization_contracts(save=False)
    assert "contracts" in tables_2

    # Stage 3
    tables_3, sum_3 = pipeline.build_objective_contracts(save=False)
    assert "objectives" in tables_3
    assert "mean_variance" in tables_3

    # Stage 4
    tables_4, sum_4 = pipeline.build_allocation_constraints(save=False)
    assert "constraints" in tables_4
    assert "long_only" in tables_4

    # Stage 5
    tables_5, sum_5 = pipeline.build_solver_outputs_metrics(save=False)
    assert "solvers" in tables_5
    assert "result_output" in tables_5

    # Stage 6
    tables_6, sum_6 = pipeline.build_dependencies_guards(save=False)
    assert "dependencies" in tables_6
    assert "forbidden_columns" in tables_6

    # Stage 7
    tables_7, sum_7 = pipeline.build_disabled_execution_reports(save=False)
    assert "opt_disabled" in tables_7

    # Stage 8
    tables_8, sum_8 = pipeline.build_findings_scoring_manifest(save=False)
    assert "manifest" in tables_8
    assert sum_8["readiness_summary"]["readiness_score"] >= 0.75

    # Stage 9
    tables_9, sum_9 = pipeline.build_health_validation_safety_handoff(save=False)
    assert "health" in tables_9
    assert sum_9["handoff_summary"]["all_satisfied"] is True


def test_pipeline_status():
    profile = get_default_portfolio_optimization_profile()
    pipeline = PortfolioOptimizationPipeline(profile=profile)
    df_status, s_status = pipeline.build_portfolio_optimization_status(save=False)
    assert not df_status.empty
    assert len(df_status) == 9
    assert s_status["all_stages_completed"] is True
    assert s_status["phase_155_handoff_ready"] is True
