import argparse
import logging
import sys

import pandas as pd

from config.symbols import get_symbol_spec
from data.storage.data_lake import DataLake
from config.paths import PROJECT_ROOT
from indicators.volume_feature_set import VolumeFeatureSetBuilder
from indicators.volume_events import build_volume_event_frame, VolumeEventConfig
from reports.report_builder import build_volume_event_preview_report

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", type=str, required=True)
    parser.add_argument("--timeframe", type=str, default="1d")
    parser.add_argument("--last", type=int, default=20)
    parser.add_argument("--use-saved-features", action="store_true", default=False)
    parser.add_argument("--allow-unusable-volume-events", action="store_true")
    return parser.parse_args()


def main():
    args = parse_args()
    spec = get_symbol_spec(args.symbol)
    if not spec:
        logger.error(f"Symbol {args.symbol} not found.")
        sys.exit(1)

    lake = DataLake(PROJECT_ROOT / "data" / "lake")

    df = pd.DataFrame()
    if args.use_saved_features:
        # Pseudo load for volume features
        if lake.has_features(spec, args.timeframe, feature_set_name="volume"):
            df = lake.load_features(spec, args.timeframe, feature_set_name="volume")

    if df.empty:
        if (
            lake.has_processed_ohlcv(spec, args.timeframe)
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
        logger.error(f"No data found for {args.symbol} {args.timeframe}")
        sys.exit(1)

    builder = VolumeFeatureSetBuilder()
    features, _ = builder.build_compact_volume_features(df, include_events=False)

    cfg = VolumeEventConfig(
        disable_events_if_volume_unusable=not args.allow_unusable_volume_events
    )
    events, summary = build_volume_event_frame(features, cfg)

    tail = events.tail(args.last)

    from config.paths import REPORTS_DIR

    VOL_REPORTS_DIR = REPORTS_DIR / "volume_reports"
    VOL_REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    report = build_volume_event_preview_report(
        args.symbol, args.timeframe, summary, tail
    )

    path = VOL_REPORTS_DIR / f"volume_event_preview_{args.symbol}_{args.timeframe}.txt"
    with open(path, "w") as f:
        f.write(report)

    print(report)


if __name__ == "__main__":
    main()
