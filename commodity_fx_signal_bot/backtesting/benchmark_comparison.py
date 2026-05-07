import pandas as pd
import numpy as np
from backtesting.advanced_metrics import calculate_cagr


def align_equity_and_benchmarks(
    equity_curve: pd.DataFrame, benchmark_df: pd.DataFrame
) -> pd.DataFrame:
    if equity_curve.empty or benchmark_df.empty:
        return equity_curve.copy() if not equity_curve.empty else pd.DataFrame()

    df = equity_curve.copy()
    benchmarks_aligned = benchmark_df.reindex(df.index, method="ffill")

    for col in benchmarks_aligned.columns:
        df[col] = benchmarks_aligned[col]

    return df


def calculate_benchmark_relative_return(
    aligned_df: pd.DataFrame, equity_col: str = "equity", benchmark_col: str = ""
) -> pd.Series:
    if (
        aligned_df.empty
        or equity_col not in aligned_df.columns
        or benchmark_col not in aligned_df.columns
    ):
        return pd.Series()

    eq_initial = aligned_df[equity_col].iloc[0]
    bench_initial = aligned_df[benchmark_col].iloc[0]

    if eq_initial <= 0 or bench_initial <= 0:
        return pd.Series(index=aligned_df.index, data=0.0)

    eq_cum = aligned_df[equity_col] / eq_initial
    bench_cum = aligned_df[benchmark_col] / bench_initial

    return eq_cum - bench_cum


def calculate_alpha_vs_benchmark(
    aligned_df: pd.DataFrame, equity_col: str = "equity", benchmark_col: str = ""
) -> float:
    if (
        aligned_df.empty
        or equity_col not in aligned_df.columns
        or benchmark_col not in aligned_df.columns
    ):
        return np.nan

    eq_cagr = calculate_cagr(pd.DataFrame({"equity": aligned_df[equity_col]}))
    bench_cagr = calculate_cagr(pd.DataFrame({"equity": aligned_df[benchmark_col]}))

    if np.isnan(eq_cagr) or np.isnan(bench_cagr):
        return np.nan

    return eq_cagr - bench_cagr


def calculate_tracking_error(
    aligned_df: pd.DataFrame,
    equity_col: str = "equity",
    benchmark_col: str = "",
    trading_days_per_year: int = 252,
) -> float:
    if (
        aligned_df.empty
        or equity_col not in aligned_df.columns
        or benchmark_col not in aligned_df.columns
    ):
        return np.nan

    eq_ret = aligned_df[equity_col].pct_change().dropna()
    bench_ret = aligned_df[benchmark_col].pct_change().dropna()

    common = eq_ret.index.intersection(bench_ret.index)
    if len(common) < 2:
        return np.nan

    excess = eq_ret.loc[common] - bench_ret.loc[common]
    std = excess.std()

    if np.isnan(std) or std == 0:
        return 0.0

    return float(std * np.sqrt(trading_days_per_year))


def calculate_information_ratio(
    aligned_df: pd.DataFrame,
    equity_col: str = "equity",
    benchmark_col: str = "",
    trading_days_per_year: int = 252,
) -> float:
    if (
        aligned_df.empty
        or equity_col not in aligned_df.columns
        or benchmark_col not in aligned_df.columns
    ):
        return np.nan

    eq_ret = aligned_df[equity_col].pct_change().dropna()
    bench_ret = aligned_df[benchmark_col].pct_change().dropna()

    common = eq_ret.index.intersection(bench_ret.index)
    if len(common) < 2:
        return np.nan

    excess = eq_ret.loc[common] - bench_ret.loc[common]
    mean_excess = excess.mean()
    std_excess = excess.std()

    if np.isnan(std_excess) or std_excess == 0:
        return 0.0

    return float((mean_excess / std_excess) * np.sqrt(trading_days_per_year))


def calculate_benchmark_hit_rate(
    aligned_df: pd.DataFrame, equity_col: str = "equity", benchmark_col: str = ""
) -> float:
    if (
        aligned_df.empty
        or equity_col not in aligned_df.columns
        or benchmark_col not in aligned_df.columns
    ):
        return np.nan

    eq_ret = aligned_df[equity_col].pct_change().dropna()
    bench_ret = aligned_df[benchmark_col].pct_change().dropna()

    common = eq_ret.index.intersection(bench_ret.index)
    if len(common) == 0:
        return np.nan

    excess = eq_ret.loc[common] - bench_ret.loc[common]
    hits = (excess > 0).sum()

    return float(hits / len(common))


def build_benchmark_comparison_table(
    equity_curve: pd.DataFrame, benchmark_df: pd.DataFrame
) -> tuple[pd.DataFrame, dict]:
    if equity_curve.empty:
        return pd.DataFrame(), {}

    aligned_df = align_equity_and_benchmarks(equity_curve, benchmark_df)

    benchmarks_to_check = [
        "bench_usdtry_index",
        "bench_gold_usd_index",
        "bench_gold_try_index",
        "bench_equal_commodity_index",
        "bench_equal_fx_index",
        "bench_tr_cpi_index",
        "bench_us_cpi_index",
    ]

    summary = {}

    eq_col = "equity"
    for b_col in benchmarks_to_check:
        if b_col in aligned_df.columns:
            valid_df = aligned_df[[eq_col, b_col]].dropna()

            if len(valid_df) > 2:
                total_ret_vs = float(
                    calculate_benchmark_relative_return(valid_df, eq_col, b_col).iloc[
                        -1
                    ]
                )
                alpha = calculate_alpha_vs_benchmark(valid_df, eq_col, b_col)
                te = calculate_tracking_error(valid_df, eq_col, b_col)
                ir = calculate_information_ratio(valid_df, eq_col, b_col)
                hr = calculate_benchmark_hit_rate(valid_df, eq_col, b_col)

                prefix = b_col.replace("bench_", "")

                summary[f"{prefix}_total_return_vs"] = total_ret_vs
                summary[f"{prefix}_alpha"] = float(alpha) if pd.notna(alpha) else None
                summary[f"{prefix}_tracking_error"] = (
                    float(te) if pd.notna(te) else None
                )
                summary[f"{prefix}_information_ratio"] = (
                    float(ir) if pd.notna(ir) else None
                )
                summary[f"{prefix}_hit_rate"] = float(hr) if pd.notna(hr) else None
                summary[f"outperformed_{prefix}"] = total_ret_vs > 0

    return aligned_df, summary
