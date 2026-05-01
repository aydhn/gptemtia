import argparse
import logging
import sys

import pandas as pd

from config.paths import PROJECT_ROOT
from config.symbols import get_symbol_spec
from data.storage.data_lake import DataLake
from indicators.volume_feature_set import VolumeFeatureSetBuilder
from reports.report_builder import build_volume_feature_preview_report

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", type=str, required=True)
    parser.add_argument("--timeframe", type=str, default="1d")
    parser.add_argument("--last", type=int, default=10)
    parser.add_argument("--full", action="store_true")
    parser.add_argument("--no-events", action="store_true")
    parser.add_argument("--allow-unusable-volume-events", action="store_true")
    parser.add_argument("--use-processed", action="store_true", default=True)
    return parser.parse_args()


def main():
    args = parse_args()
    spec = get_symbol_spec(args.symbol)
    if not spec:
        logger.error(f"Symbol {args.symbol} not found.")
        sys.exit(1)

    lake = DataLake(PROJECT_ROOT / "data" / "lake")
    df = pd.DataFrame()

    if (
        args.use_processed and lake.has_processed_ohlcv(spec, args.timeframe)
        if hasattr(lake, "has_processed_ohlcv")
        else lake.has_ohlcv(spec, args.timeframe)
    ):
        df = (
            lake.load_processed_ohlcv(spec, args.timeframe)
            if hasattr(lake, "load_processed_ohlcv")
            else lake.load_ohlcv(spec, args.timeframe)
        )
    elif lake.has_ohlcv(spec, args.timeframe):
        df = lake.load_ohlcv(spec, args.timeframe)

    if df.empty:
        logger.error(f"No OHLCV data found for {args.symbol} {args.timeframe}")
        sys.exit(1)

    builder = VolumeFeatureSetBuilder()
    include_events = not args.no_events
    disable_events = not args.allow_unusable_volume_events

    if args.full:
        features, summary = builder.build_volume_features(
            df,
            include_events=include_events,
            disable_events_if_volume_unusable=disable_events,
        )
    else:
        features, summary = builder.build_compact_volume_features(
            df,
            include_events=include_events,
            disable_events_if_volume_unusable=disable_events,
        )

    tail = features.tail(args.last)

    from config.paths import REPORTS_DIR

    VOL_REPORTS_DIR = REPORTS_DIR / "volume_reports"
    VOL_REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    report = build_volume_feature_preview_report(
        args.symbol, args.timeframe, summary, tail
    )

    path = (
        VOL_REPORTS_DIR / f"volume_feature_preview_{args.symbol}_{args.timeframe}.txt"
    )
    with open(path, "w") as f:
        f.write(report)

    print(report)


if __name__ == "__main__":
    main()
