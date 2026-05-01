import argparse
import logging
from pathlib import Path
import pandas as pd

from config.paths import ensure_project_directories, DIVERGENCE_REPORTS_DIR
from config.symbols import get_symbol_spec
from indicators.indicator_pipeline import IndicatorPipeline
from reports.report_builder import build_divergence_feature_preview_report
from data.storage.data_lake import DataLake
from ml.feature_store import FeatureStore

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.INFO)
    ensure_project_directories()

    parser = argparse.ArgumentParser(
        description="Preview divergence features for a specific symbol."
    )
    parser.add_argument(
        "--symbol", type=str, required=True, help="Symbol to analyze (e.g., GC=F)"
    )
    parser.add_argument(
        "--timeframe", type=str, default="1d", help="Timeframe (default: 1d)"
    )
    parser.add_argument("--last", type=int, default=10, help="Number of rows to show")
    parser.add_argument(
        "--full",
        action="store_true",
        help="Generate full feature set instead of compact",
    )
    parser.add_argument(
        "--no-events", action="store_true", help="Do not include event columns"
    )
    parser.add_argument(
        "--use-processed", action="store_true", default=True, help="Use processed data"
    )
    parser.add_argument(
        "--merge-saved-features",
        action="store_true",
        default=True,
        help="Merge with saved features",
    )

    args = parser.parse_args()

    spec = get_symbol_spec(args.symbol)
    if not spec:
        logger.error(f"Symbol {args.symbol} not found.")
        return

    logger.info(f"Generating divergence features for {args.symbol} {args.timeframe}")

    pipeline = IndicatorPipeline()

    # In a more robust implementation, we would load existing features and join them
    # For this phase, IndicatorPipeline handles basic loading of processed data.
    # To truly support merge-saved-features, we could do it here or within pipeline.
    # But pipeline._load_data already handles processed/raw.
    # For now, we'll let pipeline do its standard thing.

    df, summary = pipeline.build_divergence_for_symbol_timeframe(
        spec,
        args.timeframe,
        use_processed=args.use_processed,
        save=False,  # Just a preview
        compact=not args.full,
        include_events=not args.no_events,
    )

    if df.empty:
        logger.error("No data generated.")
        return

    tail_df = df.tail(args.last)

    report_text = build_divergence_feature_preview_report(
        args.symbol, args.timeframe, summary, tail_df
    )

    print(report_text)

    DIVERGENCE_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_file = (
        DIVERGENCE_REPORTS_DIR
        / f"divergence_feature_preview_{spec.symbol.replace('=', '_')}_{args.timeframe}.txt"
    )

    with open(report_file, "w") as f:
        f.write(report_text)

    logger.info(f"Report saved to {report_file}")


if __name__ == "__main__":
    main()
