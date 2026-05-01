import argparse
import logging
from pprint import pprint

from config.paths import PRICE_ACTION_REPORTS_DIR
from config.symbols import get_symbol_spec
from data.storage.data_lake import DataLake
from indicators.price_action_events import build_price_action_event_frame
from indicators.price_action_feature_set import PriceActionFeatureSetBuilder
from ml.feature_store import FeatureStore
from reports.report_builder import build_price_action_event_preview_report

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Preview price action events for a single symbol."
    )
    parser.add_argument(
        "--symbol", type=str, required=True, help="Symbol name (e.g. GC=F)"
    )
    parser.add_argument(
        "--timeframe", type=str, default="1d", help="Timeframe (e.g. 1d, 4h)"
    )
    parser.add_argument(
        "--last", type=int, default=20, help="Number of recent rows to show"
    )
    parser.add_argument(
        "--use-saved-features",
        action="store_true",
        default=False,
        help="Use saved features from data lake",
    )
    args = parser.parse_args()

    spec = get_symbol_spec(args.symbol)
    if not spec:
        logger.error(f"Symbol {args.symbol} not found in configuration.")
        return

    lake = DataLake()
    store = FeatureStore(lake)

    features = None

    if args.use_saved_features:
        features = store.load_price_action_features(spec, args.timeframe)
        if features.empty:
            logger.warning(
                f"No saved features found for {spec.name} {args.timeframe}. Falling back to generating."
            )
            features = None

    if features is None:
        if lake.has_processed_ohlcv(spec, args.timeframe):
            df = lake.load_processed_ohlcv(spec, args.timeframe)
        elif lake.has_ohlcv(spec, args.timeframe):
            df = lake.load_ohlcv(spec, args.timeframe)
        else:
            logger.error(f"No data found for {spec.name} {args.timeframe}")
            return

        builder = PriceActionFeatureSetBuilder()
        features, _ = builder.build_compact_price_action_features(
            df, include_events=False
        )

    if features.empty:
        logger.error("Failed to get features.")
        return

    event_df, summary = build_price_action_event_frame(features)

    logger.info("=== Event Summary ===")
    pprint(summary)

    tail_df = event_df.tail(args.last)

    # Filter to only rows that have at least one event
    active_rows = tail_df[(tail_df > 0).any(axis=1)]

    logger.info(f"\n=== Active Events in Last {args.last} Rows ===")
    if active_rows.empty:
        logger.info("No active events found.")
    else:
        for idx, row in active_rows.iterrows():
            active = row[row > 0].index.tolist()
            print(f"{idx}: {active}")

    report_text = build_price_action_event_preview_report(
        spec.name, args.timeframe, summary, tail_df
    )

    report_path = (
        PRICE_ACTION_REPORTS_DIR
        / f"price_action_event_preview_{spec.name}_{args.timeframe}.txt"
    )
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w") as f:
        f.write(report_text)

    logger.info(f"Report saved to {report_path}")


if __name__ == "__main__":
    main()
