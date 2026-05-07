import pytest
import pandas as pd
from backtesting.relative_performance import (
    calculate_relative_equity_curve,
    calculate_strategy_vs_usdtry,
    calculate_strategy_vs_gold,
    calculate_strategy_vs_commodity_basket,
    build_relative_performance_report,
)


def test_relative_curve():
    idx = pd.date_range("2024-01-01", periods=5)
    eq = pd.DataFrame({"equity": [100, 110, 120, 130, 140]}, index=idx)
    bench = pd.Series([100, 102, 104, 106, 108], index=idx)

    df = calculate_relative_equity_curve(eq, bench, "test_bench")
    assert "relative_to_test_bench" in df.columns


def test_build():
    idx = pd.date_range("2024-01-01", periods=5)
    eq = pd.DataFrame({"equity": [100, 110, 120, 130, 140]}, index=idx)
    bench_df = pd.DataFrame(
        {
            "bench_usdtry_index": [100, 102, 104, 106, 108],
            "bench_gold_usd_index": [100, 101, 102, 103, 104],
        },
        index=idx,
    )

    rep = build_relative_performance_report(eq, bench_df)
    assert "outperformed_usdtry" in rep
    assert "outperformed_gold_usd" in rep
