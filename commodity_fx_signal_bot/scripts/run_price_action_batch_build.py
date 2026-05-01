import argparse
import logging

import pandas as pd

from config.paths import PRICE_ACTION_REPORTS_DIR
from config.settings import settings
from config.symbols import get_enabled_symbols
from data.storage.data_lake import DataLake
from indicators.feature_builder import FeatureBuilder
from indicators.indicator_pipeline import IndicatorPipeline
from reports.report_builder import build_price_action_batch_report

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s"
)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Batch build price action features for multiple symbols."
    )
    parser.add_argument("--limit", type=int, help="Limit number of symbols to process")
    parser.add_argument(
        "--asset-class", type=str, help="Filter by asset class (e.g., metals, forex)"
    )
    parser.add_argument("--symbol", type=str, help="Process single symbol")
    parser.add_argument("--timeframe", type=str, help="Specific timeframe to build")
    parser.add_argument(
        "--profile",
        type=str,
        default=settings.default_scan_profile,
        help="Scan profile to determine timeframes",
    )
    parser.add_argument(
        "--full", action="store_true", help="Generate full price action feature set"
    )
    parser.add_argument(
        "--no-events", action="store_true", help="Skip generating event columns"
    )
    parser.add_argument(
        "--no-save", action="store_true", help="Do not save features to data lake"
    )
    parser.add_argument(
        "--use-processed", action="store_true", default=True, help="Use processed data"
    )
    args = parser.parse_args()

    lake = DataLake()
    builder = FeatureBuilder(settings)
    pipeline = IndicatorPipeline(lake, builder, settings)

    specs = get_enabled_symbols()
    if args.asset_class:
        specs = [s for s in specs if s.asset_class == args.asset_class]
    if args.symbol:
        specs = [s for s in specs if s.name == args.symbol]

    # Calculate allowed timeframes (simplified logic for now)
    timeframes_by_symbol = {}
    default_tf = [args.timeframe] if args.timeframe else ["1d", "4h", "1h"]

    for spec in specs:
        if spec.symbol_type in ["macro", "synthetic"]:
            continue
        timeframes_by_symbol[spec.name] = default_tf

    logger.info(f"Starting price action batch build for {len(specs)} symbols...")

    results = pipeline.build_price_action_for_universe(
        specs,
        timeframes_by_symbol,
        limit=args.limit,
        use_processed=args.use_processed,
        save=not args.no_save,
        compact=not args.full,
        include_events=not args.no_events,
    )

    report_text = build_price_action_batch_report(results)

    report_path = PRICE_ACTION_REPORTS_DIR / "price_action_batch_summary.txt"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w") as f:
        f.write(report_text)

    logger.info(f"Batch report saved to {report_path}")

    # Save CSV
    rows = []
    for sym, tfs in results.items():
        if isinstance(tfs, dict):
            for tf, res in tfs.items():
                row = {"symbol": sym, "timeframe": tf}
                row.update(res)
                rows.append(row)

    if rows:
        df = pd.DataFrame(rows)
        csv_path = PRICE_ACTION_REPORTS_DIR / "price_action_batch_summary.csv"
        df.to_csv(csv_path, index=False)
        logger.info(f"Batch CSV saved to {csv_path}")


if __name__ == "__main__":
    main()
