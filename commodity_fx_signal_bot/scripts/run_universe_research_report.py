import argparse
import sys
import logging
from config.settings import settings
from config.symbols import get_enabled_symbols
from data.storage.data_lake import DataLake
from research_reports.research_pipeline import ResearchReportPipeline
from research_reports.research_config import get_research_report_profile

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Generate Universe Research Report")
    parser.add_argument("--asset-class", type=str, help="Filter by asset class")
    parser.add_argument("--symbol", type=str, help="Filter by single symbol (overrides limit)")
    parser.add_argument("--limit", type=int, help="Limit number of symbols processed")
    parser.add_argument("--timeframe", type=str, default=settings.default_research_report_timeframe, help="Timeframe (e.g. 1d)")
    parser.add_argument("--profile", type=str, default=settings.default_research_report_profile, help="Research report profile name")
    parser.add_argument("--no-save", action="store_true", help="Do not save the report outputs")

    args = parser.parse_args()

    if not settings.research_reports_enabled:
        logger.warning("Research reports are disabled in settings. Exiting.")
        sys.exit(0)

    try:
        profile = get_research_report_profile(args.profile)
    except Exception as e:
        logger.error(f"Invalid profile: {e}")
        sys.exit(1)

    universe = get_enabled_symbols()
    specs = [s for s in universe if s.enabled]

    if args.symbol:
        specs = [s for s in specs if s.symbol == args.symbol]
    elif args.asset_class:
        specs = [s for s in specs if s.asset_class == args.asset_class]

    if not specs:
        logger.error("No symbols found matching criteria.")
        sys.exit(1)

    data_lake = DataLake()
    pipeline = ResearchReportPipeline(data_lake, settings, profile)

    logger.info(f"Generating universe research report for {len(specs)} symbols using profile {args.profile} on timeframe {args.timeframe}...")

    report, quality = pipeline.build_universe_report(
        specs=specs,
        timeframe=args.timeframe,
        profile=profile,
        limit=args.limit,
        save=not args.no_save
    )

    logger.info(f"Universe report generated. Ranked {report.summary.get('total_symbols_ranked')} symbols.")
    logger.info(f"Quality status passed: {quality.get('passed')}")
    if quality.get('warnings'):
        for warning in quality['warnings']:
             logger.warning(f"Quality Warning: {warning}")

    logger.info("NOTE: Bu çıktı offline araştırma/simülasyon raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir.")
    sys.exit(0)

if __name__ == "__main__":
    main()
