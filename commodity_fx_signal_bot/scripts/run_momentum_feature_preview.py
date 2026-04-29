import argparse
import logging

from config.paths import LAKE_DIR
from config.settings import settings
from config.symbols import get_symbol_spec
from data.storage.data_lake import DataLake
from indicators.momentum_feature_set import MomentumFeatureSetBuilder
from reports.report_builder import build_momentum_feature_preview_report

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(description="Preview Momentum Features")
    parser.add_argument("--symbol", type=str, required=True, help="Symbol to analyze")
    parser.add_argument(
        "--timeframe", type=str, default="1d", help="Timeframe (e.g., 1d, 4h)"
    )
    parser.add_argument(
        "--last", type=int, default=10, help="Number of recent rows to show"
    )
    parser.add_argument(
        "--full", action="store_true", help="Build full feature set instead of compact"
    )
    parser.add_argument("--no-events", action="store_true", help="Skip event columns")
    parser.add_argument(
        "--use-processed",
        action="store_true",
        default=True,
        help="Use processed data if available",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    spec = get_symbol_spec(args.symbol)
    if not spec:
        logger.error(f"Symbol {args.symbol} not found in config.")
        return
    lake = DataLake(LAKE_DIR)
    df = None
    if args.use_processed and lake.has_processed_ohlcv(spec, args.timeframe):
        df = lake.load_processed_ohlcv(spec, args.timeframe)
        logger.info(f"Loaded PROCESSED data for {args.symbol} {args.timeframe}")
    elif lake.has_ohlcv(spec, args.timeframe):
        df = lake.load_ohlcv(spec, args.timeframe)
        logger.info(f"Loaded RAW data for {args.symbol} {args.timeframe}")
    else:
        logger.error(f"No OHLCV data found for {args.symbol} {args.timeframe}")
        return
    if df is None or df.empty:
        logger.error("Dataframe is empty.")
        return
    builder = MomentumFeatureSetBuilder()
    include_events = not args.no_events
    if args.full:
        logger.info("Building full momentum feature set...")
        features, summary = builder.build_momentum_features(
            df, include_events=include_events
        )
    else:
        logger.info("Building compact momentum feature set...")
        features, summary = builder.build_compact_momentum_features(
            df, include_events=include_events
        )
    tail_df = features.tail(args.last)
    report_str = build_momentum_feature_preview_report(
        args.symbol, args.timeframe, summary, tail_df
    )

    from config.paths import MOMENTUM_REPORTS_DIR

    out_file = (
        MOMENTUM_REPORTS_DIR
        / f"momentum_feature_preview_{args.symbol}_{args.timeframe}.txt"
    )
    out_file.parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, "w") as f:
        f.write(report_str)
    print(report_str)
    logger.info(f"Report saved to {out_file}")


if __name__ == "__main__":
    main()
