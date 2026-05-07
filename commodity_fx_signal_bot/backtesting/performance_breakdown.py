import pandas as pd
import numpy as np
from config.symbols import SymbolSpec
from backtesting.advanced_metrics import calculate_profit_factor


def _aggregate_breakdown(trades_df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    if trades_df.empty or group_col not in trades_df.columns:
        return pd.DataFrame()

    def _agg(group):
        wins = group[group["net_pnl"] > 0]
        losses = group[group["net_pnl"] < 0]
        gross_profit = wins["net_pnl"].sum()
        gross_loss = abs(losses["net_pnl"].sum())

        profit_factor = (
            np.inf
            if gross_loss == 0 and gross_profit > 0
            else (0.0 if gross_loss == 0 else float(gross_profit / gross_loss))
        )

        return pd.Series(
            {
                "trade_count": len(group),
                "win_rate": len(wins) / len(group) if len(group) > 0 else 0.0,
                "total_net_pnl": (
                    group["net_pnl"].sum() if "net_pnl" in group.columns else 0.0
                ),
                "avg_return_pct": (
                    group["return_pct"].mean() if "return_pct" in group.columns else 0.0
                ),
                "median_return_pct": (
                    group["return_pct"].median()
                    if "return_pct" in group.columns
                    else 0.0
                ),
                "profit_factor": profit_factor,
                "avg_holding_bars": (
                    group["holding_bars"].mean()
                    if "holding_bars" in group.columns
                    else 0.0
                ),
                "best_trade": (
                    group["return_pct"].max() if "return_pct" in group.columns else 0.0
                ),
                "worst_trade": (
                    group["return_pct"].min() if "return_pct" in group.columns else 0.0
                ),
            }
        )

    res = trades_df.groupby(group_col).apply(_agg).reset_index()
    res.rename(columns={group_col: "group"}, inplace=True)
    return res


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
    col = (
        "strategy_family" if "strategy_family" in trades_df.columns else "strategy_name"
    )
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
        "symbol_breakdown": build_symbol_performance_breakdown(trades_df).to_dict(
            orient="records"
        ),
        "asset_class_breakdown": build_asset_class_performance_breakdown(
            trades_df, symbol_specs
        ).to_dict(orient="records"),
        "strategy_family_breakdown": build_strategy_family_performance_breakdown(
            trades_df
        ).to_dict(orient="records"),
        "directional_bias_breakdown": build_directional_bias_performance_breakdown(
            trades_df
        ).to_dict(orient="records"),
        "exit_reason_breakdown": build_exit_reason_performance_breakdown(
            trades_df
        ).to_dict(orient="records"),
        "result_label_breakdown": build_result_label_performance_breakdown(
            trades_df
        ).to_dict(orient="records"),
    }
