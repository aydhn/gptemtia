import pandas as pd
import logging
from config.symbols import SymbolSpec
from backtesting.backtest_config import BacktestProfile
from backtesting.candidate_adapter import build_candidate_events
from backtesting.lifecycle_engine import TradeLifecycleEngine
from backtesting.trade_ledger import TradeLedger
from backtesting.lookahead_guard import LookaheadGuard

logger = logging.getLogger(__name__)


class BacktestEngine:
    def __init__(
        self,
        profile: BacktestProfile,
        lifecycle_engine: TradeLifecycleEngine | None = None,
        lookahead_guard: LookaheadGuard | None = None,
    ):
        self.profile = profile
        self.lifecycle_engine = lifecycle_engine or TradeLifecycleEngine(profile)
        self.lookahead_guard = lookahead_guard or LookaheadGuard()

    def run_symbol_backtest(
        self,
        spec: SymbolSpec,
        timeframe: str,
        price_df: pd.DataFrame,
        level_candidates_df: pd.DataFrame,
    ) -> tuple[pd.DataFrame, dict]:

        # 1. Filter eligible
        eligible_df, cand_summary = build_candidate_events(level_candidates_df)

        summary = {
            "symbol": spec.symbol,
            "timeframe": timeframe,
            "profile": self.profile.name,
            "input_candidate_count": cand_summary["input_count"],
            "eligible_candidate_count": cand_summary["eligible_count"],
            "simulated_trade_count": 0,
            "rejected_candidate_count": 0,
            "cancelled_candidate_count": 0,
            "lookahead_audit": {},
            "warnings": [],
        }

        if eligible_df.empty or price_df.empty:
            return pd.DataFrame(), summary

        ledger = TradeLedger()

        # Sort candidates chronologically
        eligible_df = eligible_df.sort_index()

        open_position_end_ts = None

        for ts, row in eligible_df.iterrows():
            # Apply single position per symbol block
            if (
                self.profile.single_position_per_symbol
                and open_position_end_ts is not None
            ):
                if ts <= open_position_end_ts:
                    summary["cancelled_candidate_count"] += 1
                    continue

            # Lookahead check
            la_res = self.lookahead_guard.validate_candidate_timestamp(ts, ts)
            if not la_res["passed"]:
                summary["warnings"].append(f"Lookahead violation at {ts}")
                continue

            trade, status = self.lifecycle_engine.simulate_candidate_lifecycle(
                symbol=spec.symbol,
                timeframe=timeframe,
                candidate_row=row,
                price_df=price_df,
            )

            if status["status"] == "success":
                ledger.add(trade)
                if self.profile.single_position_per_symbol:
                    # Update open position end timestamp
                    if trade.exit_timestamp:
                        open_position_end_ts = pd.to_datetime(trade.exit_timestamp)
            else:
                summary["rejected_candidate_count"] += 1

        trades_df = ledger.to_dataframe()
        summary["simulated_trade_count"] = len(trades_df)
        summary["lookahead_audit"] = self.lookahead_guard.audit_trade_ledger(trades_df)

        return trades_df, summary

    def run_universe_backtest(
        self,
        inputs: dict[str, dict],
        timeframe: str,
    ) -> tuple[pd.DataFrame, dict]:

        all_trades = []
        universe_summary = {
            "timeframe": timeframe,
            "profile": self.profile.name,
            "total_input_candidates": 0,
            "total_simulated_trades": 0,
            "symbols_processed": 0,
            "warnings": [],
        }

        for symbol, data in inputs.items():
            if "price_df" not in data or "level_df" not in data:
                continue

            spec = SymbolSpec(symbol, "unknown")  # Simplified for signature match
            trades_df, sum_dict = self.run_symbol_backtest(
                spec, timeframe, data["price_df"], data["level_df"]
            )

            universe_summary["total_input_candidates"] += sum_dict.get(
                "input_candidate_count", 0
            )
            universe_summary["total_simulated_trades"] += len(trades_df)
            universe_summary["symbols_processed"] += 1

            if not trades_df.empty:
                all_trades.append(trades_df)

        if all_trades:
            final_df = pd.concat(all_trades, ignore_index=True)
        else:
            final_df = pd.DataFrame()

        return final_df, universe_summary
