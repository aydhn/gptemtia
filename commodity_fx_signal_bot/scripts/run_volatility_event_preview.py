import argparse
import logging
import sys

from config.paths import VOLATILITY_REPORTS_DIR
from config.symbols import get_enabled_symbols, get_symbol_spec
from data.storage.data_lake import DataLake
from indicators.volatility_events import build_volatility_event_frame
from indicators.volatility_feature_set import VolatilityFeatureSetBuilder
from ml.feature_store import FeatureStore
from reports.report_builder import build_volatility_event_preview_report

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

def parse_args():
    parser = argparse.ArgumentParser(description="Preview volatility events for a symbol.")
    parser.add_argument("--symbol", type=str, required=True, help="Symbol (e.g., GC=F)")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe (e.g., 1d, 4h)")
    parser.add_argument("--last", type=int, default=20, help="Number of rows to show")
    parser.add_argument("--use-saved-features", action="store_true", help="Try loading pre-built features from lake")
    return parser.parse_args()

def main():
    args = parse_args()


    spec = get_symbol_spec(args.symbol)

    if not spec:
        logger.error(f"Symbol '{args.symbol}' not found in universe.")
        sys.exit(1)

    from config.paths import DATA_DIR
    lake = DataLake(DATA_DIR)
    feature_store = FeatureStore(lake)

    features = None

    if args.use_saved_features:
        try:
            features = feature_store.load_volatility_features(spec, args.timeframe)
            if not features.empty:
                logger.info(f"Loaded saved volatility features for {args.symbol} {args.timeframe}")
        except Exception as e:
            logger.warning(f"Could not load saved features: {e}")

    if features is None or features.empty:
        logger.info(f"Building features dynamically for {args.symbol} {args.timeframe}")
        df = None
        if lake.has_processed_ohlcv(spec, args.timeframe):
            df = lake.load_processed_ohlcv(spec, args.timeframe)
            logger.info("Using processed OHLCV")
        elif lake.has_ohlcv(spec, args.timeframe):
            df = lake.load_ohlcv(spec, args.timeframe)
            logger.info("Using raw OHLCV")
        else:
            logger.error(f"No OHLCV data found for {args.symbol}")
            sys.exit(1)

        builder = VolatilityFeatureSetBuilder()
        # Build compact features without events
        features, _ = builder.build_compact_volatility_features(df, include_events=False)

    if features.empty:
        logger.error("Feature dataframe is empty.")
        sys.exit(1)

    logger.info("Detecting volatility events...")
    event_frame, summary = build_volatility_event_frame(features)

    if event_frame.empty:
        logger.warning("No volatility events detected.")

    event_tail_df = event_frame.tail(args.last)

    report = build_volatility_event_preview_report(args.symbol, args.timeframe, summary, event_tail_df)

    VOLATILITY_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_file = VOLATILITY_REPORTS_DIR / f"volatility_event_preview_{args.symbol}_{args.timeframe}.txt"

    with open(report_file, "w", encoding="utf-8") as f:
        f.write(report)

    print(report)
    print(f"\nReport saved to: {report_file}")

if __name__ == "__main__":
    main()
