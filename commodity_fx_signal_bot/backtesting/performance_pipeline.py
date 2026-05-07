import pandas as pd
import numpy as np
from pathlib import Path
import logging

from config.settings import Settings
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake

from backtesting.advanced_metrics import build_advanced_performance_metrics
from backtesting.drawdown_metrics import build_drawdown_analysis
from backtesting.rolling_metrics import build_rolling_metrics_frame
from backtesting.trade_distribution import build_trade_distribution_report
from backtesting.benchmark_comparison import build_benchmark_comparison_table
from backtesting.inflation_adjusted import build_inflation_adjusted_performance
from backtesting.relative_performance import build_relative_performance_report
from backtesting.performance_breakdown import build_full_performance_breakdown
from backtesting.performance_quality import build_performance_quality_report

logger = logging.getLogger(__name__)


class PerformanceAnalysisPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        profile_name: str = "balanced_candidate_backtest",
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.profile_name = profile_name
        self.performance_profile = settings.default_performance_profile

    def load_backtest_outputs(
        self, spec: SymbolSpec, timeframe: str, backtest_profile_name: str
    ) -> tuple[pd.DataFrame, pd.DataFrame]:
        try:
            trades_df = self.data_lake.load_backtest_trades(
                spec.symbol, timeframe, backtest_profile_name
            )
            equity_curve = self.data_lake.load_backtest_equity_curve(
                spec.symbol, timeframe, backtest_profile_name
            )
            return trades_df, equity_curve
        except Exception as e:
            logger.warning(f"Failed to load backtest outputs for {spec.symbol}: {e}")
            return pd.DataFrame(), pd.DataFrame()

    def load_benchmark_inputs(self, timeframe: str) -> pd.DataFrame:
        try:
            if hasattr(self.data_lake, "load_macro_features"):
                return self.data_lake.load_macro_features(timeframe)
            return pd.DataFrame()
        except Exception as e:
            logger.warning(f"Failed to load benchmark inputs: {e}")
            return pd.DataFrame()

    def analyze_symbol_performance(
        self,
        spec: SymbolSpec,
        timeframe: str = "1d",
        backtest_profile_name: str = "balanced_candidate_backtest",
        save: bool = True,
    ) -> tuple[dict, dict]:

        trades_df, equity_curve = self.load_backtest_outputs(
            spec, timeframe, backtest_profile_name
        )
        if equity_curve.empty:
            logger.warning(f"Empty equity curve for {spec.symbol}. Skipping.")
            return {}, {}

        initial_equity = (
            equity_curve["equity"].iloc[0] if not equity_curve.empty else 100000.0
        )

        adv_metrics = build_advanced_performance_metrics(
            trades_df, equity_curve, initial_equity
        )
        dd_df, dd_summary = build_drawdown_analysis(equity_curve)

        windows = self.settings.performance_rolling_windows
        roll_df, roll_summary = build_rolling_metrics_frame(equity_curve, windows)

        dist_summary = build_trade_distribution_report(trades_df)

        benchmark_df = self.load_benchmark_inputs(timeframe)
        bench_df, bench_summary = build_benchmark_comparison_table(
            equity_curve, benchmark_df
        )
        infl_df, infl_summary = build_inflation_adjusted_performance(
            equity_curve, benchmark_df
        )
        rel_summary = build_relative_performance_report(equity_curve, benchmark_df)

        breakdown_summary = build_full_performance_breakdown(trades_df, [spec])

        all_metrics = {**adv_metrics, **dd_summary, **roll_summary}

        min_trades = self.settings.performance_min_trades_for_summary
        quality_report = build_performance_quality_report(
            trades_df, equity_curve, all_metrics, bench_summary, min_trades
        )

        summary = {
            "symbol": spec.symbol,
            "timeframe": timeframe,
            "backtest_profile": backtest_profile_name,
            "performance_profile": self.performance_profile,
            "trade_count": len(trades_df),
            "advanced_metrics": adv_metrics,
            "drawdown_summary": dd_summary,
            "rolling_summary": roll_summary,
            "trade_distribution": dist_summary,
            "benchmark_summary": bench_summary,
            "inflation_adjusted_summary": infl_summary,
            "relative_performance_summary": rel_summary,
            "performance_breakdown": breakdown_summary,
            "quality_report": quality_report,
            "warnings": quality_report.get("warnings", []),
        }

        if save and self.settings.save_performance_reports:
            self.data_lake.save_backtest_performance_summary(
                spec.symbol, timeframe, self.performance_profile, summary
            )
            if not bench_df.empty:
                self.data_lake.save_benchmark_comparison(
                    spec.symbol, timeframe, self.performance_profile, bench_df
                )
            if not roll_df.empty:
                self.data_lake.save_rolling_metrics(
                    spec.symbol, timeframe, self.performance_profile, roll_df
                )
            if not dd_df.empty:
                self.data_lake.save_drawdown_analysis(
                    spec.symbol, timeframe, self.performance_profile, dd_df
                )

        return summary, all_metrics

    def analyze_universe_performance(
        self,
        specs: list[SymbolSpec],
        timeframe: str = "1d",
        backtest_profile_name: str = "balanced_candidate_backtest",
        limit: int | None = None,
        save: bool = True,
    ) -> dict:

        if limit:
            specs = specs[:limit]

        results = []
        for spec in specs:
            try:
                summary, _ = self.analyze_symbol_performance(
                    spec, timeframe, backtest_profile_name, save
                )
                if summary:
                    results.append(summary)
            except Exception as e:
                logger.error(f"Error analyzing performance for {spec.symbol}: {e}")

        ranking = []
        for r in results:
            adv = r.get("advanced_metrics", {})
            bench = r.get("benchmark_summary", {})
            infl = r.get("inflation_adjusted_summary", {})
            rel = r.get("relative_performance_summary", {})
            qual = r.get("quality_report", {})

            ranking.append(
                {
                    "symbol": r.get("symbol"),
                    "trade_count": r.get("trade_count", 0),
                    "total_return_pct": adv.get("total_return_pct", 0.0),
                    "sharpe_ratio": adv.get("sharpe_ratio", 0.0),
                    "max_drawdown_pct": adv.get("max_drawdown_pct", 0.0),
                    "profit_factor": adv.get("profit_factor", 0.0),
                    "win_rate": adv.get("win_rate", 0.0),
                    "outperformed_usdtry": rel.get("outperformed_usdtry", False),
                    "outperformed_tr_cpi": infl.get("outperformed_tr_inflation", False),
                    "quality_passed": qual.get("passed", False),
                }
            )

        return {"results": results, "ranking": ranking}
