import argparse
import logging

from config.paths import LAKE_DIR, TREND_REPORTS_DIR
from config.settings import settings
from config.symbols import get_symbol_spec
from data.storage.data_lake import DataLake
from indicators.trend_events import build_trend_event_frame
from indicators.trend_feature_set import TrendFeatureSetBuilder
from reports.report_builder import build_trend_event_preview_report
from ml.feature_store import FeatureStore

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(description="Preview Trend Events")
    parser.add_argument("--symbol", type=str, required=True, help="Symbol to analyze")
    parser.add_argument(
        "--timeframe", type=str, default="1d", help="Timeframe (e.g., 1d, 4h)"
    )
    parser.add_argument(
        "--last", type=int, default=20, help="Number of recent rows to show"
    )
    parser.add_argument(
        "--use-saved-features",
        action="store_true",
        help="Use saved features if available",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    spec = get_symbol_spec(args.symbol)
    if not spec:
        logger.error(f"Symbol {args.symbol} not found in config.")
        return

    lake = DataLake(LAKE_DIR)
    fs = FeatureStore(lake)

    events_df = None
    summary = {}

    if args.use_saved_features:
        try:
            features = fs.load_trend_features(spec, args.timeframe)
            if not features.empty:
                logger.info(
                    f"Loaded saved trend features for {args.symbol} {args.timeframe}"
                )
                events_df, summary = build_trend_event_frame(features)
        except Exception as e:
            logger.warning(f"Failed to load saved features: {e}")

    if events_df is None or events_df.empty:
        df = None
        if lake.has_processed_ohlcv(spec, args.timeframe):
            df = lake.load_processed_ohlcv(spec, args.timeframe)
            logger.info("Using processed OHLCV to build features...")
        elif lake.has_ohlcv(spec, args.timeframe):
            df = lake.load_ohlcv(spec, args.timeframe)
            logger.info("Using raw OHLCV to build features...")
        else:
            logger.error("No OHLCV data found.")
            return

        if df is None or df.empty:
            logger.error("Dataframe is empty.")
            return

        builder = TrendFeatureSetBuilder()
        features, _ = builder.build_compact_trend_features(df, include_events=False)
        events_df, summary = build_trend_event_frame(features)

    tail_df = events_df.tail(args.last)
    report_str = build_trend_event_preview_report(
        args.symbol, args.timeframe, summary, tail_df
    )

    out_file = (
        TREND_REPORTS_DIR / f"trend_event_preview_{args.symbol}_{args.timeframe}.txt"
    )
    out_file.parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, "w") as f:
        f.write(report_str)

    print(report_str)
    logger.info(f"Report saved to {out_file}")


if __name__ == "__main__":
    main()
