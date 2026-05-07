import pytest
import pandas as pd
import numpy as np
from backtesting.benchmark_comparison import (
    align_equity_and_benchmarks,
    calculate_benchmark_relative_return,
    calculate_alpha_vs_benchmark,
    calculate_tracking_error,
    calculate_information_ratio,
    calculate_benchmark_hit_rate,
    build_benchmark_comparison_table,
)


def test_align_equity_and_benchmarks():
    idx = pd.date_range("2024-01-01", periods=5)
    eq = pd.DataFrame({"equity": [100, 110, 120, 130, 140]}, index=idx)
    bm = pd.DataFrame({"bench_usdtry_index": [50, 52, 54, 56, 58]}, index=idx)

    aligned = align_equity_and_benchmarks(eq, bm)
    assert "bench_usdtry_index" in aligned.columns


def test_metrics():
    idx = pd.date_range("2024-01-01", periods=5)
    aligned = pd.DataFrame(
        {
            "equity": [100, 101, 102, 103, 104],
            "bench_usdtry_index": [100, 102, 104, 106, 108],
        },
        index=idx,
    )

    rel_ret = calculate_benchmark_relative_return(
        aligned, "equity", "bench_usdtry_index"
    )
    assert not rel_ret.empty

    alpha = calculate_alpha_vs_benchmark(aligned, "equity", "bench_usdtry_index")
    assert not np.isnan(alpha)

    te = calculate_tracking_error(aligned, "equity", "bench_usdtry_index")
    assert not np.isnan(te)

    ir = calculate_information_ratio(aligned, "equity", "bench_usdtry_index")
    assert not np.isnan(ir)

    hr = calculate_benchmark_hit_rate(aligned, "equity", "bench_usdtry_index")
    assert not np.isnan(hr)


def test_build_table():
    idx = pd.date_range("2024-01-01", periods=5)
    eq = pd.DataFrame({"equity": [100, 110, 120, 130, 140]}, index=idx)
    bm = pd.DataFrame({"bench_usdtry_index": [100, 102, 104, 106, 108]}, index=idx)

    df, summary = build_benchmark_comparison_table(eq, bm)
    assert "usdtry_index_total_return_vs" in summary
    assert "outperformed_usdtry_index" in summary
