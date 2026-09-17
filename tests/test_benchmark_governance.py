# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Benchmark Governance."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.benchmark_governance import (
    build_benchmark_governance_registry,
    BENCHMARK_GOVERNANCE_ITEMS,
)


def test_build_benchmark_governance():
    profile = get_default_backtest_governance_profile()
    df, summary = build_benchmark_governance_registry(profile)

    assert not df.empty
    assert len(df) == 3
    assert "governance_id" in df.columns
    assert "name" in df.columns
    assert (df["execution_allowed"] == False).all()
    assert summary["execution_disabled"] is True
    assert summary["total_benchmarks"] == 3
    assert len(BENCHMARK_GOVERNANCE_ITEMS) == 3
