import argparse
import sys
import logging
import pandas as pd
from config.settings import settings
from config.symbols import get_enabled_symbols
from data.storage.data_lake import DataLake
from research_reports.research_pipeline import ResearchReportPipeline
from research_reports.research_config import get_research_report_profile
from reports.report_builder import build_research_ranking_text_report

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Generate Research Ranking Report")
    parser.add_argument("--asset-class", type=str, help="Filter by asset class")
    parser.add_argument("--limit", type=int, help="Limit number of symbols processed")
    parser.add_argument("--timeframe", type=str, default=settings.default_research_report_timeframe, help="Timeframe (e.g. 1d)")
    parser.add_argument("--profile", type=str, default=settings.default_research_report_profile, help="Research report profile name")

    args = parser.parse_args()

    if not settings.research_reports_enabled:
        logger.warning("Research reports are disabled in settings. Exiting.")
        sys.exit(0)

    try:
        profile = get_research_report_profile(args.profile)
    except Exception as e:
        logger.error(f"Invalid profile: {e}")
        sys.exit(1)

    data_lake = DataLake()

    universe = get_enabled_symbols()
    specs = [s for s in universe if s.enabled]
    if args.asset_class:
        specs = [s for s in specs if s.asset_class == args.asset_class]

    pipeline = ResearchReportPipeline(data_lake, settings, profile)
    report, _ = pipeline.build_universe_report(specs, args.timeframe, profile, args.limit, save=True)

    ranking_df = report.tables.get('ranking', pd.DataFrame())

    text_report = build_research_ranking_text_report(ranking_df, report.summary)

    from config.paths import REPORTS_RESEARCH_REPORTS_TXT_DIR
    txt_path = REPORTS_RESEARCH_REPORTS_TXT_DIR / f"research_ranking_report_{args.timeframe}_{args.profile}.txt"
    txt_path.write_text(text_report, encoding='utf-8')

    logger.info(f"Research ranking report generated and saved to {txt_path}")
    logger.info("NOTE: Bu çıktı offline araştırma/simülasyon raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir.")
    sys.exit(0)

if __name__ == "__main__":
    main()
