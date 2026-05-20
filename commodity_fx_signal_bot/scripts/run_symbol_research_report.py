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
    parser = argparse.ArgumentParser(description="Generate Research Report for a symbol")
    parser.add_argument("--symbol", type=str, required=True, help="Symbol to generate report for")
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
    spec = next((s for s in universe if s.symbol == args.symbol), None)

    if not spec:
        logger.error(f"Symbol {args.symbol} not found in universe.")
        sys.exit(1)

    data_lake = DataLake()
    pipeline = ResearchReportPipeline(data_lake, settings, profile)

    logger.info(f"Generating research report for {args.symbol} using profile {args.profile} on timeframe {args.timeframe}...")

    report, quality = pipeline.build_symbol_report(
        spec=spec,
        timeframe=args.timeframe,
        profile=profile,
        save=not args.no_save
    )

    logger.info(f"Report generated with status: {report.summary.get('research_status')}")
    logger.info(f"Quality score: {quality.get('report_quality_score', 0)}")
    if quality.get('warnings'):
        for warning in quality['warnings']:
             logger.warning(f"Quality Warning: {warning}")

    logger.info("NOTE: Bu çıktı offline araştırma/simülasyon raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir.")
    sys.exit(0)

if __name__ == "__main__":
    main()
