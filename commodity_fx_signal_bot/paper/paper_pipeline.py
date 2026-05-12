import pandas as pd
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from config.settings import Settings
from paper.paper_config import PaperTradingProfile, get_default_paper_trading_profile
from paper.paper_engine import PaperTradingEngine
from paper.paper_data_adapter import PaperDataAdapter
from paper.paper_quality import build_paper_quality_report

class PaperTradingPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        profile: PaperTradingProfile | None = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_paper_trading_profile()
        self.data_adapter = PaperDataAdapter(self.data_lake)
        self.engine = PaperTradingEngine(self.profile)

    def build_for_symbol_timeframe(
        self,
        spec: SymbolSpec,
        timeframe: str = "1d",
        profile: PaperTradingProfile | None = None,
        save: bool = True,
    ) -> tuple[dict, dict]:

        if spec.asset_class in ["macro", "synthetic", "benchmark"]:
            return {}, {"warning": f"Skipping {spec.asset_class} symbol."}

        current_profile = profile or self.profile
        self.engine.profile = current_profile

        price_df, w1 = self.data_adapter.load_price_frame(spec, timeframe)
        if price_df.empty:
            return {}, {"error": f"No price data for {spec.symbol}."}

        frames, w2 = self.data_adapter.load_paper_context_frames(spec, timeframe)

        level_df = frames.get("level_candidates", pd.DataFrame())
        sizing_df = frames.get("sizing_candidates", pd.DataFrame())
        risk_df = frames.get("risk_candidates", pd.DataFrame())

        artifacts, summary = self.engine.run_symbol_paper(
            spec, timeframe, price_df, level_df, sizing_df, risk_df, frames
        )

        if save and "orders" in artifacts:
            self.data_lake.save_paper_orders(spec.symbol, timeframe, current_profile.name, artifacts["orders"])
            self.data_lake.save_paper_positions(spec.symbol, timeframe, current_profile.name, artifacts["positions"])
            self.data_lake.save_paper_portfolio(spec.symbol, timeframe, current_profile.name, artifacts["portfolio"])
            self.data_lake.save_paper_ledger(spec.symbol, timeframe, current_profile.name, artifacts["ledger"])
            self.data_lake.save_paper_summary(spec.symbol, timeframe, current_profile.name, artifacts["summary"])

            quality_report = build_paper_quality_report(
                artifacts["summary"], artifacts["orders"], artifacts["positions"], artifacts["ledger"]
            )
            self.data_lake.save_paper_quality(spec.symbol, timeframe, current_profile.name, quality_report)

        return artifacts, summary

    def build_for_universe(
        self,
        specs: list[SymbolSpec],
        timeframe: str = "1d",
        profile: PaperTradingProfile | None = None,
        limit: int | None = None,
        save: bool = True,
    ) -> dict:

        batch_results = []
        count = 0

        for spec in specs:
            if limit and count >= limit:
                break

            try:
                _, summary = self.build_for_symbol_timeframe(spec, timeframe, profile, save)
                if summary and "error" not in summary and "warning" not in summary:
                    batch_results.append(summary)
                    count += 1
            except Exception as e:
                print(f"Error processing {spec.symbol}: {e}")

        if not batch_results:
            return {}

        df = pd.DataFrame(batch_results)
        return {
            "processed_count": len(batch_results),
            "summary_df": df
        }
