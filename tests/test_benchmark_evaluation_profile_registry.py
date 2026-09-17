# -*- coding: utf-8 -*-
"""Phase 151 Unit Tests: Benchmark Evaluation Profile Registry."""

from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    get_default_benchmark_evaluation_profile,
)
from advanced_benchmark_evaluation.benchmark_evaluation_profile_registry import (
    build_benchmark_evaluation_profile_registry,
    summarize_benchmark_evaluation_profiles,
)


def test_build_benchmark_evaluation_profile_registry():
    profile = get_default_benchmark_evaluation_profile()
    df, summary = build_benchmark_evaluation_profile_registry(profile)

    assert not df.empty
    assert len(df) >= 3
    assert "profile_name" in df.columns
    assert (df["current_phase"] == 151).all()
    assert (df["target_final_phase"] == 160).all()
    assert (df["local_only"] == True).all()
    assert (df["allow_live_trading"] == False).all()
    assert (df["allow_metric_calculation"] == False).all()

    assert summary["all_local_only"] is True
    assert summary["all_live_trading_prohibited"] is True
    assert summary["non_signal"] is True
    assert summary["total_profiles"] >= 3
