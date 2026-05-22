import pandas as pd
import numpy as np
import logging
from synthetic_indices.index_config import SyntheticIndexProfile
from synthetic_indices.index_models import SyntheticIndexSeries

logger = logging.getLogger(__name__)

def compare_symbol_to_synthetic_benchmark(symbol_returns: pd.Series, benchmark_returns: pd.Series, symbol: str, benchmark_id: str) -> dict:
    if symbol_returns.empty or benchmark_returns.empty:
        return {"symbol": symbol, "benchmark_id": benchmark_id, "error": "empty series"}

    # Align
    df = pd.concat([symbol_returns, benchmark_returns], axis=1, join="inner").dropna()
    if df.empty:
        return {"symbol": symbol, "benchmark_id": benchmark_id, "error": "no overlapping data"}

    s_ret = df.iloc[:, 0]
    b_ret = df.iloc[:, 1]

    total_s = s_ret.sum()
    total_b = b_ret.sum()

    rel_ret = total_s - total_b

    # Beta-like proxy (covariance / variance)
    cov = df.cov().iloc[0, 1]
    var_b = b_ret.var()
    beta_proxy = cov / var_b if var_b > 0 else np.nan

    # Tracking diff (std dev of difference)
    diff = s_ret - b_ret
    tracking_diff = diff.std()

    # Correlation
    corr = s_ret.corr(b_ret)

    # Up/down capture
    up_b = b_ret > 0
    down_b = b_ret < 0

    up_capture = (s_ret[up_b].sum() / b_ret[up_b].sum()) if b_ret[up_b].sum() > 0 else np.nan
    down_capture = (s_ret[down_b].sum() / b_ret[down_b].sum()) if b_ret[down_b].sum() < 0 else np.nan

    return {
        "symbol": symbol,
        "benchmark_id": benchmark_id,
        "relative_return": float(rel_ret),
        "tracking_difference": float(tracking_diff),
        "correlation_to_benchmark": float(corr),
        "beta_like_proxy": float(beta_proxy),
        "upside_capture_proxy": float(up_capture) if pd.notna(up_capture) else None,
        "downside_capture_proxy": float(down_capture) if pd.notna(down_capture) else None,
        "observations": len(df)
    }

def compare_universe_to_benchmarks(returns_df: pd.DataFrame, index_series_map: dict[str, SyntheticIndexSeries]) -> pd.DataFrame:
    records = []

    for benchmark_id, series in index_series_map.items():
        bench_ret = series.return_series

        for symbol in returns_df.columns:
            sym_ret = returns_df[symbol]
            metrics = compare_symbol_to_synthetic_benchmark(sym_ret, bench_ret, symbol, benchmark_id)
            if "error" not in metrics:
                records.append(metrics)

    return pd.DataFrame(records)

def calculate_benchmark_relative_metrics(symbol_returns: pd.Series, benchmark_returns: pd.Series) -> dict:
    return compare_symbol_to_synthetic_benchmark(symbol_returns, benchmark_returns, "symbol", "benchmark")

def build_benchmark_comparison_report(returns_df: pd.DataFrame, index_series_map: dict[str, SyntheticIndexSeries], profile: SyntheticIndexProfile) -> tuple[pd.DataFrame, dict]:
    summary = {"warnings": [], "comparisons_made": 0}

    if returns_df.empty or not index_series_map:
         summary["warnings"].append("Empty returns or benchmark map.")
         return pd.DataFrame(), summary

    df = compare_universe_to_benchmarks(returns_df, index_series_map)
    summary["comparisons_made"] = len(df)

    return df, summary
