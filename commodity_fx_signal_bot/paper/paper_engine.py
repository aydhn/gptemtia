import pandas as pd
from config.symbols import SymbolSpec
from paper.paper_config import PaperTradingProfile
from paper.paper_lifecycle import PaperLifecycleEngine
from paper.virtual_order_book import VirtualOrderBook
from paper.virtual_portfolio import VirtualPortfolio
from paper.paper_ledger import PaperLedger
from paper.paper_signal_adapter import build_virtual_order_candidates

class PaperTradingEngine:
    def __init__(
        self,
        profile: PaperTradingProfile,
        lifecycle_engine: PaperLifecycleEngine | None = None,
    ):
        self.profile = profile
        self.lifecycle_engine = lifecycle_engine or PaperLifecycleEngine(profile)

    def run_symbol_paper(
        self,
        spec: SymbolSpec,
        timeframe: str,
        price_df: pd.DataFrame,
        level_df: pd.DataFrame,
        sizing_df: pd.DataFrame | None = None,
        risk_df: pd.DataFrame | None = None,
        context_frames: dict[str, pd.DataFrame] | None = None,
    ) -> tuple[dict, dict]:

        warnings = []

        orders, build_warnings = build_virtual_order_candidates(level_df, sizing_df, risk_df, self.profile)
        if build_warnings:
            warnings.append(str(build_warnings))

        order_book = VirtualOrderBook()
        portfolio = VirtualPortfolio(self.profile.initial_equity, self.profile.base_currency)
        ledger = PaperLedger()

        if not orders:
            warnings.append("No valid virtual order candidates found.")
            summary = self._build_empty_summary(spec, timeframe)
            summary["warnings"] = warnings
            return {"summary": summary}, {}

        order_map = {}
        for o in orders:
            order_map.setdefault(o.created_timestamp, []).append(o)

        for timestamp, row in price_df.iterrows():
            ts_str = str(timestamp)
            new_orders = order_map.get(ts_str, [])

            for no in new_orders:
                ledger.add_order_event(no, "virtual_order_created", ts_str)

            lifecycle_events = self.lifecycle_engine.process_timestamp(
                timestamp, price_df, new_orders, order_book, portfolio
            )

        pb_summary = portfolio.summarize()
        ob_summary = order_book.summarize()

        summary = {
            "symbol": spec.symbol,
            "timeframe": timeframe,
            "profile": self.profile.name,
            "input_level_candidates": len(level_df),
            "virtual_order_count": ob_summary.get("total_orders", 0),
            "filled_order_count": ob_summary.get("filled_orders", 0),
            "rejected_order_count": ob_summary.get("rejected_orders", 0),
            "expired_order_count": ob_summary.get("expired_orders", 0),
            "opened_position_count": pb_summary.get("open_positions", 0) + pb_summary.get("closed_positions", 0),
            "closed_position_count": pb_summary.get("closed_positions", 0),
            "final_virtual_equity": pb_summary.get("current_equity", self.profile.initial_equity),
            "total_virtual_return_pct": (pb_summary.get("current_equity", self.profile.initial_equity) / self.profile.initial_equity) - 1.0,
            "virtual_win_rate": pb_summary.get("win_rate", 0.0),
            "max_virtual_drawdown_pct": pb_summary.get("max_drawdown_pct", 0.0),
            "warnings": warnings
        }

        artifacts = {
            "orders": order_book.to_dataframe(),
            "positions": portfolio.to_positions_dataframe(),
            "portfolio": portfolio.to_equity_curve_dataframe(),
            "ledger": ledger.to_dataframe(),
            "summary": summary
        }

        return artifacts, summary

    def _build_empty_summary(self, spec: SymbolSpec, timeframe: str) -> dict:
        return {
            "symbol": spec.symbol,
            "timeframe": timeframe,
            "profile": self.profile.name,
            "input_level_candidates": 0,
            "virtual_order_count": 0,
            "filled_order_count": 0,
            "rejected_order_count": 0,
            "expired_order_count": 0,
            "opened_position_count": 0,
            "closed_position_count": 0,
            "final_virtual_equity": self.profile.initial_equity,
            "total_virtual_return_pct": 0.0,
            "virtual_win_rate": 0.0,
            "max_virtual_drawdown_pct": 0.0,
            "warnings": []
        }
