import pandas as pd
import numpy as np
from backtesting.advanced_metrics import calculate_total_return


def calculate_relative_equity_curve(
    equity_curve: pd.DataFrame, benchmark_series: pd.Series, benchmark_name: str
) -> pd.DataFrame:
    if (
        equity_curve.empty
        or benchmark_series.empty
        or "equity" not in equity_curve.columns
    ):
        return pd.DataFrame()

    bench_aligned = benchmark_series.reindex(equity_curve.index, method="ffill")
    valid_idx = bench_aligned.dropna().index.intersection(
        equity_curve.dropna(subset=["equity"]).index
    )

    if len(valid_idx) == 0:
        return pd.DataFrame()

    eq_valid = equity_curve.loc[valid_idx, "equity"]
    bench_valid = bench_aligned.loc[valid_idx]

    if bench_valid.iloc[0] <= 0:
        return pd.DataFrame()

    bench_normalized = bench_valid / bench_valid.iloc[0]
    eq_normalized = eq_valid / eq_valid.iloc[0]

    df = pd.DataFrame(index=valid_idx)
    df["nominal_equity"] = eq_valid
    df[f"{benchmark_name}_index"] = bench_normalized
    df[f"relative_to_{benchmark_name}"] = eq_normalized / bench_normalized

    return df


def calculate_relative_strength_of_strategy(
    equity_curve: pd.DataFrame, benchmark_df: pd.DataFrame
) -> pd.DataFrame:
    return pd.DataFrame()


def calculate_strategy_vs_usdtry(
    equity_curve: pd.DataFrame, benchmark_df: pd.DataFrame
) -> dict:
    col = (
        "bench_usdtry_index"
        if "bench_usdtry_index" in benchmark_df.columns
        else "usdtry" if "usdtry" in benchmark_df.columns else None
    )
    if not col:
        return {}

    df = calculate_relative_equity_curve(equity_curve, benchmark_df[col], "usdtry")
    if df.empty:
        return {}

    total_rel_ret = float(df["relative_to_usdtry"].iloc[-1] - 1.0)

    return {
        "outperformed_usdtry": total_rel_ret > 0,
        "relative_return_vs_usdtry": total_rel_ret,
    }


def calculate_strategy_vs_gold(
    equity_curve: pd.DataFrame, benchmark_df: pd.DataFrame
) -> dict:
    col_usd = (
        "bench_gold_usd_index"
        if "bench_gold_usd_index" in benchmark_df.columns
        else None
    )
    col_try = (
        "bench_gold_try_index"
        if "bench_gold_try_index" in benchmark_df.columns
        else None
    )

    res = {}
    if col_usd:
        df_usd = calculate_relative_equity_curve(
            equity_curve, benchmark_df[col_usd], "gold_usd"
        )
        if not df_usd.empty:
            total_rel_usd = float(df_usd["relative_to_gold_usd"].iloc[-1] - 1.0)
            res["outperformed_gold_usd"] = total_rel_usd > 0
            res["relative_return_vs_gold_usd"] = total_rel_usd

    if col_try:
        df_try = calculate_relative_equity_curve(
            equity_curve, benchmark_df[col_try], "gold_try"
        )
        if not df_try.empty:
            total_rel_try = float(df_try["relative_to_gold_try"].iloc[-1] - 1.0)
            res["outperformed_gold_try"] = total_rel_try > 0
            res["relative_return_vs_gold_try"] = total_rel_try

    return res


def calculate_strategy_vs_commodity_basket(
    equity_curve: pd.DataFrame, benchmark_df: pd.DataFrame
) -> dict:
    col = (
        "bench_equal_commodity_index"
        if "bench_equal_commodity_index" in benchmark_df.columns
        else None
    )
    if not col:
        return {}

    df = calculate_relative_equity_curve(
        equity_curve, benchmark_df[col], "commodity_basket"
    )
    if df.empty:
        return {}

    total_rel_ret = float(df["relative_to_commodity_basket"].iloc[-1] - 1.0)

    return {
        "outperformed_commodity_basket": total_rel_ret > 0,
        "relative_return_vs_commodity_basket": total_rel_ret,
    }


def build_relative_performance_report(
    equity_curve: pd.DataFrame, benchmark_df: pd.DataFrame
) -> dict:
    if equity_curve.empty or benchmark_df.empty:
        return {}

    res_usdtry = calculate_strategy_vs_usdtry(equity_curve, benchmark_df)
    res_gold = calculate_strategy_vs_gold(equity_curve, benchmark_df)
    res_comm = calculate_strategy_vs_commodity_basket(equity_curve, benchmark_df)

    report = {**res_usdtry, **res_gold, **res_comm}

    return report
