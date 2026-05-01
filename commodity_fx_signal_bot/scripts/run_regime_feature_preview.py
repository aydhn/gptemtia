"""
Script to generate and preview regime features.
"""

import argparse
import logging
from pathlib import Path

from config.symbols import get_symbol_spec
from config.settings import settings
from config.paths import REGIME_REPORTS_DIR
from data.storage.data_lake import DataLake
from regimes.regime_config import get_regime_profile
from regimes.regime_pipeline import RegimePipeline
from reports.report_builder import build_regime_feature_preview_report, save_text_report

logger = logging.getLogger(__name__)

def parse_args():
    parser = argparse.ArgumentParser(description="Preview regime features for a symbol.")
    parser.add_argument("--symbol", type=str, required=True, help="Symbol to analyze")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe (e.g., 1d, 4h)")
    parser.add_argument("--profile", type=str, default="balanced_regime", help="Regime profile name")
    parser.add_argument("--last", type=int, default=10, help="Number of recent rows to show")
    parser.add_argument("--no-events", action="store_true", help="Do not generate events")
    parser.add_argument("--save", action="store_true", help="Save the generated features to Data Lake")
    return parser.parse_args()

def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    args = parse_args()

    try:
        spec = get_symbol_spec(args.symbol)
    except Exception as e:
        logger.error(f"Symbol error: {e}")
        return

    try:
        profile = get_regime_profile(args.profile)
    except Exception as e:
        logger.error(f"Profile error: {e}")
        return

    lake = DataLake()
    pipeline = RegimePipeline(lake, settings, profile)

    logger.info(f"Generating regimes for {spec.symbol} {args.timeframe} using profile {profile.name}")

    df, summary = pipeline.build_for_symbol_timeframe(
        spec=spec,
        timeframe=args.timeframe,
        profile=profile,
        save=args.save,
        include_events=not args.no_events
    )

    if df.empty:
        logger.warning(f"No regime data generated. Status: {summary.get('status')}")
        return

    tail_df = df.tail(args.last)
    report = build_regime_feature_preview_report(spec.symbol, args.timeframe, profile.name, summary, tail_df)

    print(report)

    report_path = REGIME_REPORTS_DIR / f"regime_feature_preview_{spec.symbol}_{args.timeframe}_{profile.name}.txt"
    save_text_report(report, report_path)
    logger.info(f"Report saved to {report_path}")

if __name__ == "__main__":
    main()
