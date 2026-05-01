import argparse
import logging

from config.paths import PROJECT_ROOT, REPORTS_DIR
from config.settings import settings
from config.symbols import (
    get_allowed_timeframes_for_symbol,
    get_enabled_symbols,
    get_symbol_spec,
    get_symbols_by_asset_class,
)
from data.storage.data_lake import DataLake
from indicators.feature_builder import FeatureBuilder
from indicators.indicator_pipeline import IndicatorPipeline
from reports.report_builder import build_volume_batch_report

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int)
    parser.add_argument("--asset-class", type=str)
    parser.add_argument("--symbol", type=str)
    parser.add_argument("--timeframe", type=str)
    parser.add_argument("--profile", type=str, default="balanced_swing")
    parser.add_argument("--full", action="store_true")
    parser.add_argument("--no-events", action="store_true")
    parser.add_argument("--allow-unusable-volume-events", action="store_true")
    parser.add_argument("--save", action="store_true", default=True)
    parser.add_argument("--use-processed", action="store_true", default=True)
    return parser.parse_args()


def main():
    args = parse_args()

    if args.symbol:
        specs = [get_symbol_spec(args.symbol)]
    else:
        specs = (
            get_symbols_by_asset_class(args.asset_class)
            if args.asset_class
            else get_enabled_symbols()
        )

    if args.limit:
        specs = specs[: args.limit]

    tfs_by_symbol = {}
    for spec in specs:
        if args.timeframe:
            tfs_by_symbol[spec.symbol] = (args.timeframe,)
        else:
            tfs_by_symbol[spec.symbol] = get_allowed_timeframes_for_symbol(spec)

    pipeline = IndicatorPipeline(
        DataLake(PROJECT_ROOT / "data" / "lake"), FeatureBuilder(), settings
    )

    res = pipeline.build_volume_for_universe(
        specs=specs,
        timeframes_by_symbol=tfs_by_symbol,
        limit=args.limit,
        use_processed=args.use_processed,
        save=args.save,
        compact=not args.full,
        include_events=not args.no_events,
        disable_events_if_volume_unusable=not args.allow_unusable_volume_events,
    )

    report = build_volume_batch_report(res)

    VOL_REPORTS_DIR = REPORTS_DIR / "volume_reports"
    VOL_REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    with open(VOL_REPORTS_DIR / "volume_batch_summary.txt", "w") as f:
        f.write(report)

    print(report)


if __name__ == "__main__":
    main()
