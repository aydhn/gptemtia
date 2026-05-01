"""
Script to preview regime events for a symbol.
"""

import argparse
import logging

from config.symbols import get_symbol_spec
from config.settings import settings
from config.paths import REGIME_REPORTS_DIR
from data.storage.data_lake import DataLake
from regimes.regime_config import get_regime_profile
from regimes.regime_pipeline import RegimePipeline
from regimes.regime_events import build_regime_event_frame
from reports.report_builder import build_regime_event_preview_report, save_text_report

logger = logging.getLogger(__name__)

def parse_args():
    parser = argparse.ArgumentParser(description="Preview regime events for a symbol.")
    parser.add_argument("--symbol", type=str, required=True, help="Symbol to analyze")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe")
    parser.add_argument("--profile", type=str, default="balanced_regime", help="Regime profile")
    parser.add_argument("--last", type=int, default=20, help="Number of rows to show")
    parser.add_argument("--use-saved-features", action="store_true", help="Try to use saved features first")
    return parser.parse_args()

def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    args = parse_args()

    try:
        spec = get_symbol_spec(args.symbol)
        profile = get_regime_profile(args.profile)
    except Exception as e:
        logger.error(str(e))
        return

    lake = DataLake()

    regime_df = None
    if args.use_saved_features and lake.has_features(spec, args.timeframe, "regime"):
        logger.info("Loading saved regime features")
        regime_df = lake.load_features(spec, args.timeframe, "regime")
        summary_info = {"status": "loaded from saved"}

    if regime_df is None or regime_df.empty:
        logger.info("Building regime features dynamically")
        pipeline = RegimePipeline(lake, settings, profile)
        regime_df, sum_info = pipeline.build_for_symbol_timeframe(
            spec, args.timeframe, profile, save=False, include_events=False
        )
        summary_info = sum_info

    if regime_df.empty:
        logger.warning("Could not obtain regime data.")
        return

    logger.info("Building regime events")
    event_df, event_summary = build_regime_event_frame(regime_df)

    # Combine some metadata
    event_summary["status"] = summary_info.get("status", "unknown")
    event_summary["warnings"].extend(summary_info.get("warnings", []))

    tail_df = event_df.tail(args.last)
    report = build_regime_event_preview_report(spec.symbol, args.timeframe, profile.name, event_summary, tail_df)

    print(report)

    report_path = REGIME_REPORTS_DIR / f"regime_event_preview_{spec.symbol}_{args.timeframe}_{profile.name}.txt"
    save_text_report(report, report_path)
    logger.info(f"Report saved to {report_path}")

if __name__ == "__main__":
    main()
