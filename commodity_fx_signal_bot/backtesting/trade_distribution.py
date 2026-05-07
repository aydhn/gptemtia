import pandas as pd
import numpy as np


def calculate_trade_return_distribution(trades_df: pd.DataFrame) -> dict:
    if trades_df.empty or "return_pct" not in trades_df.columns:
        return {
            "mean_return": 0.0,
            "median_return": 0.0,
            "std_return": 0.0,
            "skew_return": 0.0,
            "kurtosis_return": 0.0,
            "best_trade": 0.0,
            "worst_trade": 0.0,
        }

    returns = trades_df["return_pct"]
    return {
        "mean_return": float(returns.mean()) if pd.notna(returns.mean()) else 0.0,
        "median_return": float(returns.median()) if pd.notna(returns.median()) else 0.0,
        "std_return": float(returns.std()) if pd.notna(returns.std()) else 0.0,
        "skew_return": float(returns.skew()) if pd.notna(returns.skew()) else 0.0,
        "kurtosis_return": (
            float(returns.kurtosis()) if pd.notna(returns.kurtosis()) else 0.0
        ),
        "best_trade": float(returns.max()) if pd.notna(returns.max()) else 0.0,
        "worst_trade": float(returns.min()) if pd.notna(returns.min()) else 0.0,
    }


def calculate_trade_pnl_distribution(trades_df: pd.DataFrame) -> dict:
    if trades_df.empty or "net_pnl" not in trades_df.columns:
        return {
            "mean_pnl": 0.0,
            "median_pnl": 0.0,
            "best_pnl": 0.0,
            "worst_pnl": 0.0,
        }

    pnl = trades_df["net_pnl"]
    return {
        "mean_pnl": float(pnl.mean()) if pd.notna(pnl.mean()) else 0.0,
        "median_pnl": float(pnl.median()) if pd.notna(pnl.median()) else 0.0,
        "best_pnl": float(pnl.max()) if pd.notna(pnl.max()) else 0.0,
        "worst_pnl": float(pnl.min()) if pd.notna(pnl.min()) else 0.0,
    }


def calculate_holding_period_distribution(trades_df: pd.DataFrame) -> dict:
    if trades_df.empty or "holding_bars" not in trades_df.columns:
        return {
            "avg_holding_bars": 0.0,
            "median_holding_bars": 0.0,
            "max_holding_bars": 0.0,
            "min_holding_bars": 0.0,
        }

    bars = trades_df["holding_bars"]
    return {
        "avg_holding_bars": float(bars.mean()) if pd.notna(bars.mean()) else 0.0,
        "median_holding_bars": float(bars.median()) if pd.notna(bars.median()) else 0.0,
        "max_holding_bars": float(bars.max()) if pd.notna(bars.max()) else 0.0,
        "min_holding_bars": float(bars.min()) if pd.notna(bars.min()) else 0.0,
    }


def calculate_exit_reason_distribution(trades_df: pd.DataFrame) -> pd.DataFrame:
    if trades_df.empty or "exit_reason" not in trades_df.columns:
        return pd.DataFrame()

    counts = trades_df["exit_reason"].value_counts().reset_index()
    counts.columns = ["exit_reason", "count"]
    counts["pct"] = counts["count"] / len(trades_df)
    return counts


def calculate_result_label_distribution(trades_df: pd.DataFrame) -> pd.DataFrame:
    if trades_df.empty or "result_label" not in trades_df.columns:
        return pd.DataFrame()

    counts = trades_df["result_label"].value_counts().reset_index()
    counts.columns = ["result_label", "count"]
    counts["pct"] = counts["count"] / len(trades_df)
    return counts


def calculate_trade_streaks(trades_df: pd.DataFrame) -> dict:
    if trades_df.empty or "net_pnl" not in trades_df.columns:
        return {"max_win_streak": 0, "max_loss_streak": 0}

    is_win = (trades_df["net_pnl"] > 0).astype(int)
    is_loss = (trades_df["net_pnl"] < 0).astype(int)

    win_groups = (is_win != is_win.shift()).cumsum()
    loss_groups = (is_loss != is_loss.shift()).cumsum()

    win_streaks = is_win.groupby(win_groups).sum()
    loss_streaks = is_loss.groupby(loss_groups).sum()

    max_win_streak = int(win_streaks.max()) if not win_streaks.empty else 0
    max_loss_streak = int(loss_streaks.max()) if not loss_streaks.empty else 0

    return {"max_win_streak": max_win_streak, "max_loss_streak": max_loss_streak}


def build_trade_distribution_report(trades_df: pd.DataFrame) -> dict:
    ret_dist = calculate_trade_return_distribution(trades_df)
    pnl_dist = calculate_trade_pnl_distribution(trades_df)
    hold_dist = calculate_holding_period_distribution(trades_df)
    streaks = calculate_trade_streaks(trades_df)

    exit_dist = calculate_exit_reason_distribution(trades_df)
    result_dist = calculate_result_label_distribution(trades_df)

    report = {
        **ret_dist,
        **pnl_dist,
        **hold_dist,
        **streaks,
    }

    if not exit_dist.empty:
        report["exit_reason_distribution"] = exit_dist.to_dict(orient="records")
    else:
        report["exit_reason_distribution"] = []

    if not result_dist.empty:
        report["result_label_distribution"] = result_dist.to_dict(orient="records")
    else:
        report["result_label_distribution"] = []

    return report
