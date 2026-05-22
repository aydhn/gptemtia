import pandas as pd
from synthetic_indices.benchmark_comparison import (
    compare_symbol_to_synthetic_benchmark,
    compare_universe_to_benchmarks
)
from synthetic_indices.index_models import SyntheticIndexSeries

def test_benchmark_comparison():
    dates = pd.date_range("2023-01-01", periods=10)
    bench_ret = pd.Series([0.01]*10, index=dates)
    sym_ret = pd.Series([0.02]*10, index=dates)

    comp = compare_symbol_to_synthetic_benchmark(sym_ret, bench_ret, "A", "BENCH1")
    assert "error" not in comp
    assert comp["relative_return"] > 0
    assert "beta_like_proxy" in comp

    returns_df = pd.DataFrame({"A": sym_ret})
    series = SyntheticIndexSeries(
        index_id="BENCH1",
        timeframe="1d",
        level_series=pd.Series(),
        return_series=bench_ret,
        start_date=None,
        end_date=None,
        observation_count=10,
        warnings=[]
    )

    df = compare_universe_to_benchmarks(returns_df, {"BENCH1": series})
    assert len(df) == 1
    assert "A" in df["symbol"].values
