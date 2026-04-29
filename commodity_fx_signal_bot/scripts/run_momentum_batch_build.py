import argparse
import logging

from config.paths import LAKE_DIR
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
from reports.report_builder import build_momentum_batch_report

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(description="Batch build Momentum features")
    parser.add_argument(
        "--limit", type=int, help="Limit number of symbol/timeframe combos"
    )
    parser.add_argument("--asset-class", type=str, help="Filter by asset class")
    parser.add_argument("--symbol", type=str, help="Specific symbol to build")
    parser.add_argument("--timeframe", type=str, help="Specific timeframe to build")
    parser.add_argument(
        "--profile",
        type=str,
        default=settings.default_scan_profile,
        help="Scan profile name",
    )
    parser.add_argument("--full", action="store_true", help="Build full feature set")
    parser.add_argument("--no-events", action="store_true", help="Skip events")
    parser.add_argument(
        "--save", action="store_true", default=True, help="Save to data lake"
    )
    parser.add_argument(
        "--use-processed", action="store_true", default=True, help="Use processed data"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    lake = DataLake(LAKE_DIR)
    fb = FeatureBuilder()
    pipeline = IndicatorPipeline(lake, fb, settings)
    specs = []
    if args.symbol:
        spec = get_symbol_spec(args.symbol)
        if spec:
            specs.append(spec)
    else:
        specs = (
            get_symbols_by_asset_class(args.asset_class)
            if args.asset_class
            else get_enabled_symbols()
        )
    timeframes_by_symbol = {}
    for s in specs:
        if args.timeframe:
            timeframes_by_symbol[s.symbol] = (args.timeframe,)
        else:
            timeframes_by_symbol[s.symbol] = get_allowed_timeframes_for_symbol(s)
    compact = not args.full
    include_events = not args.no_events
    logger.info(f"Starting batch momentum build. Target: {len(specs)} symbols.")
    results = pipeline.build_momentum_for_universe(
        specs=specs,
        timeframes_by_symbol=timeframes_by_symbol,
        limit=args.limit,
        use_processed=args.use_processed,
        save=args.save,
        compact=compact,
        include_events=include_events,
    )
    report_str = build_momentum_batch_report(results)

    from config.paths import MOMENTUM_REPORTS_DIR

    out_txt = MOMENTUM_REPORTS_DIR / "momentum_batch_summary.txt"
    out_txt.parent.mkdir(parents=True, exist_ok=True)
    with open(out_txt, "w") as f:
        f.write(report_str)
    logger.info(f"Batch completed. Saved text report to {out_txt}")
    import pandas as pd

    df_res = pd.DataFrame(results.get("details", []))
    if not df_res.empty:
        out_csv = MOMENTUM_REPORTS_DIR / "momentum_batch_summary.csv"
        df_res.to_csv(out_csv, index=False)
        logger.info(f"Saved CSV report to {out_csv}")


if __name__ == "__main__":
    main()
