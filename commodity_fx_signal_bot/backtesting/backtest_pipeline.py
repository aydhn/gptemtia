import pandas as pd
import logging
from config.symbols import SymbolSpec
from config.settings import Settings
from data.storage.data_lake import DataLake
from backtesting.backtest_config import BacktestProfile, get_default_backtest_profile
from backtesting.data_adapter import BacktestDataAdapter
from backtesting.backtest_engine import BacktestEngine
from backtesting.equity_curve import build_equity_curve
from backtesting.performance_summary import calculate_basic_performance_summary
from backtesting.backtest_quality import build_backtest_quality_report
from backtesting.backtest_models import BacktestRunSummary, build_backtest_run_id

logger = logging.getLogger(__name__)


class BacktestPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        profile: BacktestProfile | None = None,
    ):
        self.lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_backtest_profile()
        self.data_adapter = BacktestDataAdapter(self.lake)
        self.engine = BacktestEngine(self.profile)

    def build_for_symbol_timeframe(
        self,
        spec: SymbolSpec,
        timeframe: str = "1d",
        profile: BacktestProfile | None = None,
        save: bool = True,
    ) -> tuple[pd.DataFrame, dict]:

        prof = profile or self.profile

        # 1. Load data
        price_df, p_status = self.data_adapter.load_price_frame(spec, timeframe)
        if price_df.empty:
            logger.warning(f"No price data for {spec.symbol} {timeframe}")
            return pd.DataFrame(), {"error": "no_price_data"}

        level_df, l_status = self.data_adapter.load_level_candidates(spec, timeframe)
        if level_df.empty:
            logger.warning(f"No level candidates for {spec.symbol} {timeframe}")

        # 2. Run Engine
        trades_df, run_summary = self.engine.run_symbol_backtest(
            spec, timeframe, price_df, level_df
        )

        # 3. Post-process
        eq_curve = build_equity_curve(trades_df, prof.initial_equity)
        perf_summary = calculate_basic_performance_summary(
            trades_df, eq_curve, prof.initial_equity
        )

        qual_report = build_backtest_quality_report(
            trades_df, run_summary, run_summary.get("lookahead_audit", {})
        )

        final_summary = {
            "symbol": spec.symbol,
            "timeframe": timeframe,
            "profile": prof.name,
            "run_summary": run_summary,
            "performance": perf_summary,
            "quality": qual_report,
        }

        if (
            save
            and self.settings.save_backtest_trades
            and hasattr(self.lake, "save_backtest_trades")
            and not trades_df.empty
        ):
            self.lake.save_backtest_trades(spec.symbol, timeframe, prof.name, trades_df)

        if (
            save
            and self.settings.save_backtest_equity_curve
            and hasattr(self.lake, "save_backtest_equity_curve")
            and not eq_curve.empty
        ):
            self.lake.save_backtest_equity_curve(
                spec.symbol, timeframe, prof.name, eq_curve
            )

        if (
            save
            and self.settings.save_backtest_results
            and hasattr(self.lake, "save_backtest_summary")
        ):
            self.lake.save_backtest_summary(
                spec.symbol, timeframe, prof.name, final_summary
            )

        return trades_df, final_summary

    def build_for_universe(
        self,
        specs: list[SymbolSpec],
        timeframe: str = "1d",
        profile: BacktestProfile | None = None,
        limit: int | None = None,
        save: bool = True,
    ) -> dict:

        prof = profile or self.profile
        symbols_run = []
        all_trades = []

        count = 0
        for spec in specs:
            if spec.symbol.startswith("^"):  # simple check for benchmark/synthetic
                continue

            try:
                trades_df, sym_summary = self.build_for_symbol_timeframe(
                    spec, timeframe, prof, save
                )
                if not trades_df.empty:
                    all_trades.append(trades_df)
                symbols_run.append(spec.symbol)

                count += 1
                if limit and count >= limit:
                    break
            except Exception as e:
                logger.error(f"Error backtesting {spec.symbol}: {e}")

        if all_trades:
            final_df = pd.concat(all_trades, ignore_index=True)
        else:
            final_df = pd.DataFrame()

        eq_curve = build_equity_curve(final_df, prof.initial_equity)
        perf_summary = calculate_basic_performance_summary(
            final_df, eq_curve, prof.initial_equity
        )

        run_id = build_backtest_run_id(prof.name, timeframe, symbols_run)

        batch_summary = {
            "run_id": run_id,
            "profile": prof.name,
            "timeframe": timeframe,
            "symbols_processed": len(symbols_run),
            "total_trades": len(final_df),
            "performance": perf_summary,
        }

        if save and hasattr(self.lake, "save_backtest_summary"):
            self.lake.save_backtest_summary(
                "BATCH_UNIVERSE", timeframe, prof.name, batch_summary
            )

        return batch_summary
