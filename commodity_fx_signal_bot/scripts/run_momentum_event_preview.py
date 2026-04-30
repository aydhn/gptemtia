import argparse
import logging

from config.symbols import get_symbol_spec
from data.storage.data_lake import DataLake
from indicators.momentum_feature_set import MomentumFeatureSetBuilder
from reports.report_builder import build_momentum_event_preview_report

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(description="Preview Momentum Events")
    parser.add_argument("--symbol", type=str, required=True, help="Symbol to analyze")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe")
    parser.add_argument(
        "--last", type=int, default=20, help="Number of recent rows to show"
    )
    parser.add_argument(
        "--use-saved-features",
        action="store_true",
        default=False,
        help="Use already saved momentum features",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    spec = get_symbol_spec(args.symbol)
    if not spec:
        logger.error(f"Symbol {args.symbol} not found.")
        return
    lake = DataLake()
    features = None
    summary = {}
    if args.use_saved_features and lake.has_features(spec, args.timeframe, "momentum"):
        features = lake.load_features(spec, args.timeframe, "momentum")
        logger.info("Loaded pre-calculated momentum features.")
        from indicators.momentum_events import build_momentum_event_frame

        event_df, ev_summary = build_momentum_event_frame(features)
        summary = ev_summary
        summary["input_rows"] = len(features)
        event_tail = event_df.tail(args.last)
    else:
        if lake.has_processed_ohlcv(spec, args.timeframe):
            df = lake.load_processed_ohlcv(spec, args.timeframe)
        elif lake.has_ohlcv(spec, args.timeframe):
            df = lake.load_ohlcv(spec, args.timeframe)
        else:
            logger.error("No OHLCV data found.")
            return
        builder = MomentumFeatureSetBuilder()
        _, fs_summary = builder.build_compact_momentum_features(df, include_events=True)
        summary = fs_summary.get("event_summary", {})
        features_only, _ = builder.build_compact_momentum_features(
            df, include_events=False
        )
        from indicators.momentum_events import build_momentum_event_frame

        event_df, _ = build_momentum_event_frame(features_only)
        event_tail = event_df.tail(args.last)
    report_str = build_momentum_event_preview_report(
        args.symbol, args.timeframe, summary, event_tail
    )

    from config.paths import MOMENTUM_REPORTS_DIR

    out_file = (
        MOMENTUM_REPORTS_DIR
        / f"momentum_event_preview_{args.symbol}_{args.timeframe}.txt"
    )
    out_file.parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, "w") as f:
        f.write(report_str)
    print(report_str)
    logger.info(f"Report saved to {out_file}")


if __name__ == "__main__":
    main()
