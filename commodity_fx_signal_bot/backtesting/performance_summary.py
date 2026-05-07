import pandas as pd


def calculate_win_rate(trades_df: pd.DataFrame) -> float:
    if trades_df.empty:
        return 0.0
    wins = len(trades_df[trades_df["result_label"] == "win"])
    total_closed = len(
        trades_df[trades_df["result_label"].isin(["win", "loss", "breakeven"])]
    )
    return wins / total_closed if total_closed > 0 else 0.0


def calculate_profit_factor(trades_df: pd.DataFrame) -> float:
    if trades_df.empty:
        return 0.0
    gross_profits = trades_df[trades_df["net_pnl"] > 0]["net_pnl"].sum()
    gross_losses = abs(trades_df[trades_df["net_pnl"] < 0]["net_pnl"].sum())
    return gross_profits / gross_losses if gross_losses > 0 else float("inf")


def calculate_average_trade_return(trades_df: pd.DataFrame) -> float:
    if trades_df.empty or "return_pct" not in trades_df.columns:
        return 0.0
    return trades_df["return_pct"].mean()


def calculate_expectancy(trades_df: pd.DataFrame) -> float:
    if trades_df.empty:
        return 0.0
    win_rate = calculate_win_rate(trades_df)
    avg_win = trades_df[trades_df["result_label"] == "win"]["net_pnl"].mean()
    avg_loss = abs(trades_df[trades_df["result_label"] == "loss"]["net_pnl"].mean())
    if pd.isna(avg_win):
        avg_win = 0.0
    if pd.isna(avg_loss):
        avg_loss = 0.0

    return (win_rate * avg_win) - ((1 - win_rate) * avg_loss)


def calculate_basic_performance_summary(
    trades_df: pd.DataFrame, equity_curve: pd.DataFrame, initial_equity: float
) -> dict:
    if trades_df.empty:
        return {}

    win_rate = calculate_win_rate(trades_df)
    profit_factor = calculate_profit_factor(trades_df)
    expectancy = calculate_expectancy(trades_df)

    total_net_pnl = trades_df["net_pnl"].sum()
    final_equity = initial_equity + total_net_pnl

    max_dd = equity_curve["drawdown_pct"].max() if not equity_curve.empty else 0.0

    return {
        "trade_count": len(trades_df),
        "win_rate": win_rate,
        "total_return_pct": (
            total_net_pnl / initial_equity if initial_equity > 0 else 0.0
        ),
        "net_pnl": total_net_pnl,
        "gross_pnl": trades_df["gross_pnl"].sum(),
        "profit_factor": profit_factor,
        "expectancy": expectancy,
        "avg_win": (
            trades_df[trades_df["result_label"] == "win"]["net_pnl"].mean()
            if not trades_df[trades_df["result_label"] == "win"].empty
            else 0.0
        ),
        "avg_loss": (
            trades_df[trades_df["result_label"] == "loss"]["net_pnl"].mean()
            if not trades_df[trades_df["result_label"] == "loss"].empty
            else 0.0
        ),
        "avg_holding_bars": trades_df["holding_bars"].mean(),
        "max_drawdown_pct": max_dd,
    }


def build_symbol_performance_table(trades_df: pd.DataFrame) -> pd.DataFrame:
    if trades_df.empty:
        return pd.DataFrame()

    summary = []
    for sym, group in trades_df.groupby("symbol"):
        wr = calculate_win_rate(group)
        pf = calculate_profit_factor(group)
        net_pnl = group["net_pnl"].sum()
        summary.append(
            {
                "symbol": sym,
                "trade_count": len(group),
                "win_rate": wr,
                "profit_factor": pf,
                "net_pnl": net_pnl,
            }
        )
    return pd.DataFrame(summary)


def build_strategy_family_performance_table(trades_df: pd.DataFrame) -> pd.DataFrame:
    if trades_df.empty:
        return pd.DataFrame()

    summary = []
    for fam, group in trades_df.groupby("strategy_family"):
        wr = calculate_win_rate(group)
        pf = calculate_profit_factor(group)
        net_pnl = group["net_pnl"].sum()
        summary.append(
            {
                "strategy_family": fam,
                "trade_count": len(group),
                "win_rate": wr,
                "profit_factor": pf,
                "net_pnl": net_pnl,
            }
        )
    return pd.DataFrame(summary)
