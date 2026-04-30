import argparse
import logging
import sys

from config.paths import ensure_project_directories
from config.settings import settings
from config.symbols import get_symbol_spec
from data.storage.data_lake import DataLake
from indicators.feature_builder import FeatureBuilder
from reports.report_builder import (
    build_mean_reversion_event_preview_report,
    save_text_report,
)

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(description="Preview Mean Reversion Events")
    parser.add_argument(
        "--symbol", type=str, required=True, help="Symbol code (e.g. GC=F)"
    )
    parser.add_argument(
        "--timeframe", type=str, default="1d", help="Timeframe (default: 1d)"
    )
    parser.add_argument(
        "--last", type=int, default=20, help="Number of recent rows to show"
    )
    parser.add_argument(
        "--use-saved-features",
        action="store_true",
        help="Load saved features instead of calculating",
    )
    return parser.parse_args()


def main():
    ensure_project_directories()
    args = parse_args()

    try:
        spec = get_symbol_spec(args.symbol)
    except ValueError as e:
        logger.error(str(e))
        sys.exit(1)

    lake = DataLake()

    event_df = None
    summary = {}

    if args.use_saved_features and lake.has_features(
        spec, args.timeframe, "mean_reversion_events"
    ):
        logger.info("Loading saved mean reversion events...")
        event_df = lake.load_features(spec, args.timeframe, "mean_reversion_events")

        event_counts = event_df.sum().to_dict()
        active_last = []
        if not event_df.empty:
            last_row = event_df.iloc[-1]
            active_last = last_row[last_row > 0].index.tolist()

        summary = {
            "input_rows": len(event_df),
            "event_columns": event_df.columns.tolist(),
            "total_event_count": int(sum(event_counts.values())),
            "event_count_by_column": event_counts,
            "active_last_row_events": active_last,
            "notes": "Loaded from saved features. These events are candidates, not direct buy/sell signals.",
        }
    else:
        logger.info("Building features and events from data...")
        df = None
        if lake.has_processed_ohlcv(spec, args.timeframe):
            df = lake.load_processed_ohlcv(spec, args.timeframe)
        elif lake.has_ohlcv(spec, args.timeframe):
            df = lake.load_ohlcv(spec, args.timeframe)
        else:
            logger.error("No OHLCV data found.")
            sys.exit(1)

        builder = FeatureBuilder()
        features, f_summary = builder.build_mean_reversion_feature_set(
            df, compact=True, include_events=True
        )

        event_cols = f_summary.get("event_columns", [])
        if not event_cols:
            logger.error("No events generated.")
            sys.exit(1)

        event_df = features[event_cols]
        summary = f_summary

    tail_df = event_df.tail(args.last)

    report_text = build_mean_reversion_event_preview_report(
        args.symbol, args.timeframe, summary, tail_df
    )

    print("\n" + report_text)

    from config.paths import MEAN_REVERSION_REPORTS_DIR

    MEAN_REVERSION_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_path = (
        MEAN_REVERSION_REPORTS_DIR
        / f"mean_reversion_event_preview_{spec.symbol.replace('=','_')}_{args.timeframe}.txt"
    )
    save_text_report(report_text, report_path)
    logger.info(f"Saved event preview report to {report_path}")


if __name__ == "__main__":
    main()
