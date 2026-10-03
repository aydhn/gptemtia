import numpy as np
import pandas as pd

from config.symbols import SymbolSpec


def _aggregate_breakdown(trades_df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    if trades_df.empty or group_col not in trades_df.columns:
        return pd.DataFrame()

    has_net_pnl = "net_pnl" in trades_df.columns
    has_return_pct = "return_pct" in trades_df.columns
    has_holding_bars = "holding_bars" in trades_df.columns

    df = trades_df[[group_col]].copy()
    kwargs = {}

    if has_net_pnl:
        df["net_pnl"] = trades_df["net_pnl"]
        df["is_win"] = (df["net_pnl"] > 0).astype(int)
        df["win_pnl"] = np.where(df["net_pnl"] > 0, df["net_pnl"], 0.0)
        df["loss_pnl"] = np.where(df["net_pnl"] < 0, df["net_pnl"], 0.0)

        kwargs["trade_count"] = (group_col, "count")
        kwargs["total_net_pnl"] = ("net_pnl", "sum")
        kwargs["win_count"] = ("is_win", "sum")
        kwargs["gross_profit"] = ("win_pnl", "sum")
        kwargs["gross_loss"] = ("loss_pnl", "sum")
    else:
        kwargs["trade_count"] = (group_col, "count")

    if has_return_pct:
        df["return_pct"] = trades_df["return_pct"]
        kwargs["avg_return_pct"] = ("return_pct", "mean")
        kwargs["median_return_pct"] = ("return_pct", "median")
        kwargs["best_trade"] = ("return_pct", "max")
        kwargs["worst_trade"] = ("return_pct", "min")

    if has_holding_bars:
        df["holding_bars"] = trades_df["holding_bars"]
        kwargs["avg_holding_bars"] = ("holding_bars", "mean")

    res = df.groupby(group_col).agg(**kwargs).reset_index()
    res.rename(columns={group_col: "group"}, inplace=True)

    if has_net_pnl:
        res["win_rate"] = np.where(
            res["trade_count"] > 0, res["win_count"] / res["trade_count"], 0.0
        )
        res["gross_loss"] = res["gross_loss"].abs()

        conditions = [
            (res["gross_loss"] == 0) & (res["gross_profit"] > 0),
            (res["gross_loss"] == 0) & (res["gross_profit"] == 0),
        ]
        choices = [np.inf, 0.0]
        res["profit_factor"] = np.select(
            conditions, choices, default=res["gross_profit"] / res["gross_loss"]
        )
        res.drop(columns=["win_count", "gross_profit", "gross_loss"], inplace=True)
    else:
        res["win_rate"] = 0.0
        res["total_net_pnl"] = 0.0
        res["profit_factor"] = 0.0

    if not has_return_pct:
        res["avg_return_pct"] = 0.0
        res["median_return_pct"] = 0.0
        res["best_trade"] = 0.0
        res["worst_trade"] = 0.0

    if not has_holding_bars:
        res["avg_holding_bars"] = 0.0

    cols = [
        "group",
        "trade_count",
        "win_rate",
        "total_net_pnl",
        "avg_return_pct",
        "median_return_pct",
        "profit_factor",
        "avg_holding_bars",
        "best_trade",
        "worst_trade",
    ]
    return res[cols]


def build_symbol_performance_breakdown(trades_df: pd.DataFrame) -> pd.DataFrame:
    return _aggregate_breakdown(trades_df, "symbol")


def build_asset_class_performance_breakdown(
    trades_df: pd.DataFrame, symbol_specs: list[SymbolSpec] | None = None
) -> pd.DataFrame:
    if trades_df.empty or "symbol" not in trades_df.columns:
        return pd.DataFrame()

    df = trades_df.copy()
    if symbol_specs:
        class_map = {s.symbol: s.asset_class for s in symbol_specs}
        df["asset_class"] = df["symbol"].map(class_map).fillna("unknown")
    else:
        df["asset_class"] = "unknown"

    return _aggregate_breakdown(df, "asset_class")


def build_strategy_family_performance_breakdown(
    trades_df: pd.DataFrame,
) -> pd.DataFrame:
    if trades_df.empty:
        return pd.DataFrame()
    col = "strategy_family" if "strategy_family" in trades_df.columns else "strategy_name"
    if col not in trades_df.columns:
        return pd.DataFrame()
    return _aggregate_breakdown(trades_df, col)


def build_directional_bias_performance_breakdown(
    trades_df: pd.DataFrame,
) -> pd.DataFrame:
    return _aggregate_breakdown(trades_df, "direction")


def build_exit_reason_performance_breakdown(trades_df: pd.DataFrame) -> pd.DataFrame:
    return _aggregate_breakdown(trades_df, "exit_reason")


def build_result_label_performance_breakdown(trades_df: pd.DataFrame) -> pd.DataFrame:
    return _aggregate_breakdown(trades_df, "result_label")


def build_regime_performance_breakdown(
    trades_df: pd.DataFrame, regime_df: pd.DataFrame | None = None
) -> pd.DataFrame:
    if trades_df.empty:
        return pd.DataFrame()
    if "regime" not in trades_df.columns:
        return pd.DataFrame()
    return _aggregate_breakdown(trades_df, "regime")


def build_full_performance_breakdown(
    trades_df: pd.DataFrame, symbol_specs: list[SymbolSpec] | None = None
) -> dict:
    if trades_df.empty:
        return {}

    return {
        "symbol_breakdown": build_symbol_performance_breakdown(trades_df).to_dict(orient="records"),
        "asset_class_breakdown": build_asset_class_performance_breakdown(
            trades_df, symbol_specs
        ).to_dict(orient="records"),
        "strategy_family_breakdown": build_strategy_family_performance_breakdown(trades_df).to_dict(
            orient="records"
        ),
        "directional_bias_breakdown": build_directional_bias_performance_breakdown(
            trades_df
        ).to_dict(orient="records"),
        "exit_reason_breakdown": build_exit_reason_performance_breakdown(trades_df).to_dict(
            orient="records"
        ),
        "result_label_breakdown": build_result_label_performance_breakdown(trades_df).to_dict(
            orient="records"
        ),
    }
