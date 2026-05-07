import pandas as pd


def build_equity_curve(trades_df: pd.DataFrame, initial_equity: float) -> pd.DataFrame:
    if trades_df.empty:
        return pd.DataFrame()

    # Sort by exit timestamp to simulate realization of PnL
    df = trades_df.copy()
    df = df.dropna(subset=["exit_timestamp"])
    df["exit_timestamp"] = pd.to_datetime(df["exit_timestamp"])
    df = df.sort_values("exit_timestamp")

    records = []
    current_equity = initial_equity
    cumulative_pnl = 0.0

    for i, row in df.iterrows():
        pnl = row.get("net_pnl", 0.0)
        current_equity += pnl
        cumulative_pnl += pnl

        records.append(
            {
                "timestamp": row["exit_timestamp"],
                "equity": current_equity,
                "cumulative_pnl": cumulative_pnl,
                "trade_count_cumulative": i + 1,
            }
        )

    eq_df = pd.DataFrame(records)
    if not eq_df.empty:
        eq_df = calculate_drawdown(eq_df)
    return eq_df


def calculate_drawdown(equity_curve: pd.DataFrame) -> pd.DataFrame:
    df = equity_curve.copy()
    df["peak_equity"] = df["equity"].cummax()
    df["drawdown"] = df["peak_equity"] - df["equity"]
    df["drawdown_pct"] = df["drawdown"] / df["peak_equity"]
    return df


def calculate_equity_metrics(equity_curve: pd.DataFrame) -> dict:
    if equity_curve.empty:
        return {}

    return {
        "final_equity": equity_curve["equity"].iloc[-1],
        "max_drawdown_pct": equity_curve["drawdown_pct"].max(),
        "total_trades": equity_curve["trade_count_cumulative"].iloc[-1],
    }
