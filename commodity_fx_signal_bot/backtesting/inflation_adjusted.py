import pandas as pd
import numpy as np
from backtesting.advanced_metrics import calculate_cagr, calculate_total_return
from backtesting.drawdown_metrics import calculate_max_drawdown


def align_equity_with_inflation(
    equity_curve: pd.DataFrame, macro_df: pd.DataFrame
) -> pd.DataFrame:
    if equity_curve.empty or macro_df.empty:
        return equity_curve.copy() if not equity_curve.empty else pd.DataFrame()

    df = equity_curve.copy()
    macro_aligned = macro_df.reindex(df.index, method="ffill")

    for col in [
        "tr_cpi_index",
        "us_cpi_index",
        "bench_tr_cpi_index",
        "bench_us_cpi_index",
    ]:
        if col in macro_aligned.columns:
            df[col] = macro_aligned[col]

    return df


def calculate_real_equity_curve(
    equity_curve: pd.DataFrame, inflation_index: pd.Series
) -> pd.DataFrame:
    if (
        equity_curve.empty
        or inflation_index.empty
        or "equity" not in equity_curve.columns
    ):
        return pd.DataFrame()

    infl = inflation_index.reindex(equity_curve.index, method="ffill")
    valid_idx = infl.dropna().index.intersection(
        equity_curve.dropna(subset=["equity"]).index
    )
    if len(valid_idx) == 0:
        return pd.DataFrame()

    eq_valid = equity_curve.loc[valid_idx, "equity"]
    infl_valid = infl.loc[valid_idx]

    if infl_valid.iloc[0] <= 0:
        return pd.DataFrame()

    infl_normalized = infl_valid / infl_valid.iloc[0]

    df = pd.DataFrame(index=valid_idx)
    df["nominal_equity"] = eq_valid
    df["inflation_index"] = infl_normalized
    df["real_equity"] = df["nominal_equity"] / df["inflation_index"]

    return df


def calculate_real_return_metrics(real_equity_curve: pd.DataFrame) -> dict:
    if real_equity_curve.empty or "real_equity" not in real_equity_curve.columns:
        return {}

    eq_df = pd.DataFrame({"equity": real_equity_curve["real_equity"]})

    total_real_ret = calculate_total_return(eq_df)
    real_cagr = calculate_cagr(eq_df)
    real_dd = calculate_max_drawdown(eq_df)

    return {
        "real_total_return": float(total_real_ret),
        "real_cagr": float(real_cagr) if pd.notna(real_cagr) else None,
        "real_max_drawdown_pct": float(real_dd.get("max_drawdown_pct", 0.0)),
    }


def calculate_inflation_outperformance(
    equity_curve: pd.DataFrame, inflation_index: pd.Series
) -> dict:
    real_df = calculate_real_equity_curve(equity_curve, inflation_index)
    if real_df.empty:
        return {"outperformed_inflation": False}

    total_real_ret = calculate_total_return(
        pd.DataFrame({"equity": real_df["real_equity"]})
    )

    return {
        "outperformed_inflation": total_real_ret > 0,
        "real_total_return": float(total_real_ret),
    }


def build_inflation_adjusted_performance(
    equity_curve: pd.DataFrame, macro_df: pd.DataFrame
) -> tuple[pd.DataFrame, dict]:
    if equity_curve.empty:
        return pd.DataFrame(), {}

    aligned_df = align_equity_with_inflation(equity_curve, macro_df)
    summary = {}

    summary["nominal_total_return"] = float(calculate_total_return(equity_curve))

    tr_col = (
        "bench_tr_cpi_index"
        if "bench_tr_cpi_index" in aligned_df.columns
        else "tr_cpi_index" if "tr_cpi_index" in aligned_df.columns else None
    )
    us_col = (
        "bench_us_cpi_index"
        if "bench_us_cpi_index" in aligned_df.columns
        else "us_cpi_index" if "us_cpi_index" in aligned_df.columns else None
    )

    if tr_col:
        real_tr = calculate_real_equity_curve(equity_curve, aligned_df[tr_col])
        if not real_tr.empty:
            aligned_df["real_equity_vs_tr_cpi"] = real_tr["real_equity"]
            tr_metrics = calculate_real_return_metrics(real_tr)
            summary["real_total_return_tr_cpi"] = tr_metrics.get(
                "real_total_return", 0.0
            )
            summary["outperformed_tr_inflation"] = (
                summary["real_total_return_tr_cpi"] > 0
            )
            summary["real_cagr_tr_cpi"] = tr_metrics.get("real_cagr")
            summary["real_max_drawdown_pct_tr"] = tr_metrics.get(
                "real_max_drawdown_pct", 0.0
            )

    if us_col:
        real_us = calculate_real_equity_curve(equity_curve, aligned_df[us_col])
        if not real_us.empty:
            aligned_df["real_equity_vs_us_cpi"] = real_us["real_equity"]
            us_metrics = calculate_real_return_metrics(real_us)
            summary["real_total_return_us_cpi"] = us_metrics.get(
                "real_total_return", 0.0
            )
            summary["outperformed_us_inflation"] = (
                summary["real_total_return_us_cpi"] > 0
            )
            summary["real_cagr_us_cpi"] = us_metrics.get("real_cagr")
            summary["real_max_drawdown_pct_us"] = us_metrics.get(
                "real_max_drawdown_pct", 0.0
            )

    return aligned_df, summary
