import argparse
import logging
from pathlib import Path
import pandas as pd

from config.paths import ensure_project_directories, DIVERGENCE_REPORTS_DIR
from config.symbols import get_symbol_spec
from indicators.indicator_pipeline import IndicatorPipeline
from reports.report_builder import build_divergence_event_preview_report
from data.storage.data_lake import DataLake
from ml.feature_store import FeatureStore

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.INFO)
    ensure_project_directories()

    parser = argparse.ArgumentParser(
        description="Preview divergence events for a specific symbol."
    )
    parser.add_argument("--symbol", type=str, required=True)
    parser.add_argument("--timeframe", type=str, default="1d")
    parser.add_argument("--last", type=int, default=20)
    parser.add_argument("--use-saved-features", action="store_true", default=False)
    parser.add_argument("--merge-saved-features", action="store_true", default=True)

    args = parser.parse_args()

    spec = get_symbol_spec(args.symbol)
    if not spec:
        logger.error(f"Symbol {args.symbol} not found.")
        return

    logger.info(f"Generating divergence events for {args.symbol} {args.timeframe}")

    pipeline = IndicatorPipeline()

    if args.use_saved_features:
        # Currently the pipeline doesn't natively pull just "saved features" directly
        # and skip build entirely if we want to run through the whole chain.
        # But `build_divergence_for_symbol_timeframe` does everything we need.
        report_builder = ReportBuilder()

    df, summary = pipeline.build_divergence_for_symbol_timeframe(
        spec,
        args.timeframe,
        use_processed=True,
        save=False,
        compact=False,  # Full to ensure we get events from all base cols
        include_events=True,
    )

    if df.empty:
        logger.error("No data generated.")
        return

    event_cols = summary.get("event_columns", [])
    if not event_cols:
        logger.error("No event columns generated.")
        return

    # Extract event dataframe
    event_df = df[event_cols]

    # Filter to only rows that have at least one event
    active_rows = event_df[(event_df > 0).any(axis=1)]
    tail_df = event_df.tail(args.last)

    # Rebuild summary for event specific view
    event_summary = {
        "input_rows": len(df),
        "event_columns": event_cols,
        "total_event_count": int(event_df.sum().sum()),
        "event_count_by_column": {col: int(event_df[col].sum()) for col in event_cols},
        "active_last_row_events": [
            col
            for col in event_cols
            if len(event_df) > 0 and event_df[col].iloc[-1] > 0
        ],
        "notes": summary.get("notes", []) + summary.get("warnings", []),
    }

    report_text = build_divergence_event_preview_report(
        args.symbol, args.timeframe, event_summary, tail_df
    )

    print(report_text)

    DIVERGENCE_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_file = (
        DIVERGENCE_REPORTS_DIR
        / f"divergence_event_preview_{spec.symbol.replace('=', '_')}_{args.timeframe}.txt"
    )

    with open(report_file, "w") as f:
        f.write(report_text)

    logger.info(f"Report saved to {report_file}")


if __name__ == "__main__":
    main()
