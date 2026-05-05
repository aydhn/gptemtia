import argparse
import sys
from pathlib import Path
import logging

from config.symbols import get_symbol_spec
from config.settings import settings
from data.storage.data_lake import DataLake
from decisions import DecisionPipeline, get_decision_profile
from reports.report_builder import build_decision_candidate_preview_report

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Preview decision candidates for a symbol"
    )
    parser.add_argument("--symbol", required=True, help="Symbol code (e.g., GC=F)")
    parser.add_argument("--timeframe", default="1d", help="Timeframe (e.g., 1d, 1h)")
    parser.add_argument(
        "--profile", default="balanced_directional_decision", help="Decision profile"
    )
    parser.add_argument(
        "--last", type=int, default=10, help="Number of recent candidates to show"
    )
    parser.add_argument(
        "--save", action="store_true", help="Save candidates to data lake"
    )

    args = parser.parse_args()

    try:
        spec = get_symbol_spec(args.symbol)
    except Exception as e:
        logger.error(f"Error getting symbol spec: {e}")
        return

    try:
        profile = get_decision_profile(args.profile)
    except Exception as e:
        logger.error(f"Error getting decision profile: {e}")
        return

    data_lake = DataLake()
    pipeline = DecisionPipeline(data_lake, settings, profile)

    df, summary = pipeline.build_for_symbol_timeframe(
        spec, args.timeframe, profile, save=args.save
    )

    if df.empty:
        logger.warning(
            f"No decision candidates found for {args.symbol} {args.timeframe}"
        )
        return

    tail_df = df.tail(args.last)
    report = build_decision_candidate_preview_report(
        args.symbol, args.timeframe, args.profile, summary, tail_df
    )

    print("\n" + report)

    # Save report
    from config.paths import DECISION_REPORTS_DIR

    DECISION_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_path = (
        DECISION_REPORTS_DIR
        / f"decision_candidate_preview_{spec.safe_symbol}_{args.timeframe}_{args.profile}.txt"
    )
    report_path.write_text(report, encoding="utf-8")
    logger.info(f"Report saved to {report_path}")


if __name__ == "__main__":
    main()
