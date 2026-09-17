# -*- coding: utf-8 -*-
"""Phase 151 Unit Tests: Benchmark Evaluation Domain Registry."""

from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    get_default_benchmark_evaluation_profile,
)
from advanced_benchmark_evaluation.benchmark_evaluation_domain_registry import (
    build_benchmark_evaluation_domain_registry,
    summarize_benchmark_evaluation_domains,
)


def test_build_benchmark_evaluation_domain_registry():
    profile = get_default_benchmark_evaluation_profile()
    df, summary = build_benchmark_evaluation_domain_registry(profile)

    assert not df.empty
    assert len(df) >= 12
    assert "domain_name" in df.columns
    assert (df["execution_allowed"] == False).all()
    assert (df["metric_calculation_allowed"] == False).all()
    assert (df["signal_allowed"] == False).all()

    assert summary["all_contract_ready"] is True
    assert summary["all_execution_disabled"] is True
    assert summary["all_signals_disabled"] is True
    assert summary["total_domains"] >= 12
