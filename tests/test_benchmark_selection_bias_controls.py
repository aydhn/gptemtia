# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Benchmark Selection Bias Controls."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.benchmark_selection_bias_controls import (
    build_benchmark_selection_bias_control_registry,
    BENCHMARK_CONTROLS,
)


def test_build_benchmark_selection_bias_controls():
    profile = get_default_backtest_governance_profile()
    df, summary = build_benchmark_selection_bias_control_registry(profile)

    assert not df.empty
    assert len(df) == 3
    assert "control_id" in df.columns
    assert "name" in df.columns
    assert (df["execution_allowed"] == False).all()
    assert (df["status"] == "ACTIVE").all()
    assert summary["total_controls"] == 3
    assert len(BENCHMARK_CONTROLS) == 3
