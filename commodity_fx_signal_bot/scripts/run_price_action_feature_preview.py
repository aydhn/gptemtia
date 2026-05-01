import argparse
import logging
from pprint import pprint

from config.paths import PRICE_ACTION_REPORTS_DIR
from config.symbols import get_symbol_spec
from data.storage.data_lake import DataLake
from indicators.price_action_feature_set import PriceActionFeatureSetBuilder
from reports.report_builder import build_price_action_feature_preview_report

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Preview price action features for a single symbol."
    )
    parser.add_argument(
        "--symbol", type=str, required=True, help="Symbol name (e.g. GC=F)"
    )
    parser.add_argument(
        "--timeframe", type=str, default="1d", help="Timeframe (e.g. 1d, 4h)"
    )
    parser.add_argument(
        "--last", type=int, default=10, help="Number of recent rows to show"
    )
    parser.add_argument(
        "--full", action="store_true", help="Generate full price action feature set"
    )
    parser.add_argument(
        "--no-events", action="store_true", help="Skip generating event columns"
    )
    parser.add_argument(
        "--use-processed", action="store_true", default=True, help="Use processed data"
    )
    args = parser.parse_args()

    spec = get_symbol_spec(args.symbol)
    if not spec:
        logger.error(f"Symbol {args.symbol} not found in configuration.")
        return

    lake = DataLake()

    if args.use_processed and lake.has_processed_ohlcv(spec, args.timeframe):
        df = lake.load_processed_ohlcv(spec, args.timeframe)
        logger.info(
            f"Loaded processed data for {spec.name} ({args.timeframe}): {len(df)} rows"
        )
    elif lake.has_ohlcv(spec, args.timeframe):
        df = lake.load_ohlcv(spec, args.timeframe)
        logger.info(
            f"Loaded raw data for {spec.name} ({args.timeframe}): {len(df)} rows"
        )
    else:
        logger.error(f"No data found for {spec.name} {args.timeframe}")
        return

    builder = PriceActionFeatureSetBuilder()

    if args.full:
        features, summary = builder.build_price_action_features(
            df, include_events=not args.no_events
        )
    else:
        features, summary = builder.build_compact_price_action_features(
            df, include_events=not args.no_events
        )

    if features.empty:
        logger.error("Failed to build price action features.")
        if "warnings" in summary:
            for w in summary["warnings"]:
                logger.error(f"Warning: {w}")
        return

    logger.info("=== Build Summary ===")
    pprint(summary)

    tail_df = features.tail(args.last)
    logger.info(f"\n=== Last {args.last} Rows of Price Action Features ===")
    print(tail_df.to_string())

    report_text = build_price_action_feature_preview_report(
        spec.name, args.timeframe, summary, tail_df
    )

    report_path = (
        PRICE_ACTION_REPORTS_DIR
        / f"price_action_feature_preview_{spec.name}_{args.timeframe}.txt"
    )
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w") as f:
        f.write(report_text)

    logger.info(f"Report saved to {report_path}")


if __name__ == "__main__":
    main()
