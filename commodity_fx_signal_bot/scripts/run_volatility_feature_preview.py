import argparse
import logging
import sys

from config.paths import VOLATILITY_REPORTS_DIR
from config.symbols import get_enabled_symbols, get_symbol_spec
from data.storage.data_lake import DataLake
from indicators.volatility_feature_set import VolatilityFeatureSetBuilder
from reports.report_builder import build_volatility_feature_preview_report

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

def parse_args():
    parser = argparse.ArgumentParser(description="Preview volatility features for a specific symbol.")
    parser.add_argument("--symbol", type=str, required=True, help="Symbol to build features for (e.g., GC=F)")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe (e.g., 1d, 4h)")
    parser.add_argument("--last", type=int, default=10, help="Number of latest rows to show")
    parser.add_argument("--full", action="store_true", help="Build full volatility feature set instead of compact")
    parser.add_argument("--no-events", action="store_true", help="Skip event columns")
    parser.add_argument("--no-use-processed", action="store_true", help="Do not use processed data")
    return parser.parse_args()

def main():
    args = parse_args()


    spec = get_symbol_spec(args.symbol)

    if not spec:
        logger.error(f"Symbol '{args.symbol}' not found in universe.")
        sys.exit(1)

    from config.paths import DATA_DIR
    lake = DataLake(DATA_DIR)

    df = None
    use_processed = not args.no_use_processed
    if use_processed and lake.has_processed_ohlcv(spec, args.timeframe):
        df = lake.load_processed_ohlcv(spec, args.timeframe)
        logger.info(f"Loaded PROCESSED data for {args.symbol} {args.timeframe}")
    elif lake.has_ohlcv(spec, args.timeframe):
        df = lake.load_ohlcv(spec, args.timeframe)
        logger.info(f"Loaded RAW data for {args.symbol} {args.timeframe}")
    else:
        logger.error(f"No OHLCV data found for {args.symbol} {args.timeframe}")
        sys.exit(1)

    builder = VolatilityFeatureSetBuilder()

    compact = not args.full
    include_events = not args.no_events

    logger.info(f"Building {'compact' if compact else 'full'} volatility features...")

    if compact:
        features, summary = builder.build_compact_volatility_features(df, include_events=include_events)
    else:
        features, summary = builder.build_volatility_features(df, include_events=include_events)

    if "error" in summary:
        logger.error(f"Feature build failed: {summary['error']}")
        sys.exit(1)

    tail_df = features.tail(args.last)

    report = build_volatility_feature_preview_report(args.symbol, args.timeframe, summary, tail_df)

    VOLATILITY_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_file = VOLATILITY_REPORTS_DIR / f"volatility_feature_preview_{args.symbol}_{args.timeframe}.txt"

    with open(report_file, "w", encoding="utf-8") as f:
        f.write(report)

    print(report)
    print(f"\nReport saved to: {report_file}")

if __name__ == "__main__":
    main()
