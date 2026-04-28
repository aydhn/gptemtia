import sys
import argparse
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from core.logger import get_logger
from config.settings import settings
from config.symbols import get_enabled_symbols, get_symbols_by_asset_class
from data.storage.cache_manager import CacheManager
from data.data_pipeline import DataPipeline
from data.universe_analyzer import UniverseAnalyzer
from reports.report_builder import (
    build_reliability_report,
    save_text_report,
    save_dataframe_report,
)

logger = get_logger("run_symbol_reliability_scan")


def main():
    parser = argparse.ArgumentParser(description="Run Symbol Reliability Scan")
    parser.add_argument(
        "--limit", type=int, default=None, help="Limit number of symbols to scan"
    )
    parser.add_argument("--interval", type=str, default="1d", help="Data interval")
    parser.add_argument("--period", type=str, default="1y", help="Data period")
    parser.add_argument(
        "--asset-class", type=str, default=None, help="Filter by asset class"
    )
    parser.add_argument(
        "--refresh", action="store_true", help="Force refresh data from providers"
    )

    args = parser.parse_args()

    logger.info(
        f"Starting Symbol Reliability Scan. limit={args.limit}, interval={args.interval}, period={args.period}, asset-class={args.asset_class}"
    )

    if args.asset_class:
        symbols = get_symbols_by_asset_class(args.asset_class)
    else:
        symbols = get_enabled_symbols()

    if not symbols:
        logger.warning("No symbols found matching the criteria.")
        return

    cache_manager = CacheManager(cache_dir=Path("data/cache"))
    pipeline = DataPipeline(settings, cache_manager)
    analyzer = UniverseAnalyzer(pipeline, settings)

    results = analyzer.analyze_many(
        specs=symbols,
        interval=args.interval,
        period=args.period,
        limit=args.limit,
        refresh=args.refresh,
    )

    df_results = UniverseAnalyzer.results_to_dataframe(results)

    output_dir = Path("reports/output")

    csv_path = output_dir / "universe_reliability.csv"
    save_dataframe_report(df_results, csv_path)
    logger.info(f"Saved CSV report to {csv_path}")

    report_text = build_reliability_report(results)
    txt_path = output_dir / "universe_reliability_report.txt"
    save_text_report(report_text, txt_path)
    logger.info(f"Saved TXT report to {txt_path}")

    summary = UniverseAnalyzer.summarize_results(results)
    success_rate = (
        summary.get("success_count", 0) / summary.get("total_analyzed", 1)
    ) * 100

    logger.info(
        f"Scan Completed. Total Analyzed: {summary.get('total_analyzed')}, Success Rate: {success_rate:.1f}%"
    )
    print("\n" + report_text + "\n")


if __name__ == "__main__":
    main()
