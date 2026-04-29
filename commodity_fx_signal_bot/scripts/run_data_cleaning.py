import argparse
from pathlib import Path

import pandas as pd

from config.settings import settings
from config.symbols import get_enabled_symbols
from config.timeframes import list_timeframes
from core.logger import get_logger
from data.cleaning.cleaning_report import (
    build_cleaning_report,
    save_cleaning_report_json,
)
from data.cleaning.integrity_checks import run_integrity_checks
from data.cleaning.missing_data import (
    detect_timestamp_gaps,
    fill_small_price_gaps,
    summarize_gaps,
)
from data.cleaning.ohlcv_cleaner import CleaningOptions, OHLCVCleaner
from data.cleaning.outlier_detector import build_outlier_report
from data.cleaning.quality_scoring import calculate_quality_score
from data.storage.data_lake import DataLake
from reports.report_builder import build_data_cleaning_report

logger = get_logger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Clean Data Lake OHLCV data.")
    parser.add_argument("--limit", type=int, help="Limit number of symbols to clean.")
    parser.add_argument("--asset-class", type=str, help="Filter by asset class.")
    parser.add_argument("--symbol", type=str, help="Clean a specific symbol.")
    parser.add_argument("--timeframe", type=str, help="Filter by timeframe.")
    parser.add_argument(
        "--dry-run", action="store_true", help="Do not save processed data."
    )
    parser.add_argument(
        "--forward-fill-small-gaps", action="store_true", help="Enable forward filling."
    )
    parser.add_argument(
        "--max-forward-fill-gap", type=int, default=2, help="Max gap to fill."
    )

    args = parser.parse_args()

    logger.info("Starting Data Cleaning Process")

    lake_dir = Path("data/lake")
    data_lake = DataLake(lake_dir)

    symbols = get_enabled_symbols()
    if args.asset_class:
        symbols = [
            s for s in symbols if s.asset_class.lower() == args.asset_class.lower()
        ]
    if args.symbol:
        symbols = [s for s in symbols if s.symbol == args.symbol]
    if args.limit:
        symbols = symbols[: args.limit]

    timeframes_by_symbol = {
        s.symbol: tuple(t.name for t in list_timeframes()) for s in symbols
    }

    # Configure Cleaner
    cleaning_opts = CleaningOptions(
        forward_fill_small_gaps=args.forward_fill_small_gaps
        or settings.allow_forward_fill_small_gaps,
        max_forward_fill_gap=args.max_forward_fill_gap,
    )
    cleaner = OHLCVCleaner(cleaning_opts)

    results = []

    for spec in symbols:
        allowed_tfs = timeframes_by_symbol.get(spec.symbol, tuple())
        if args.timeframe:
            if args.timeframe not in allowed_tfs:
                continue
            allowed_tfs = (args.timeframe,)

        for tf in allowed_tfs:
            try:
                if not data_lake.has_ohlcv(spec, tf):
                    continue

                logger.info(f"Cleaning {spec.symbol} {tf}...")
                raw_df = data_lake.load_ohlcv(spec, tf)

                # Quality Before
                score_before = calculate_quality_score(spec.symbol, tf, raw_df)
                integrity_before = run_integrity_checks(raw_df)

                # Clean Basic
                cleaned_df, cleaning_summary = cleaner.clean(raw_df)

                # Fill gaps if requested
                if cleaning_opts.forward_fill_small_gaps:
                    cleaned_df, filled_counts = fill_small_price_gaps(
                        cleaned_df, cleaning_opts.max_forward_fill_gap
                    )
                    cleaning_summary["filled_gaps"] = filled_counts

                # Analyze Gaps (Post clean)
                gaps_df = detect_timestamp_gaps(cleaned_df, tf)
                gap_summary = summarize_gaps(gaps_df)

                # Outlier Detection
                outlier_summary = build_outlier_report(cleaned_df)

                # Quality After
                score_after = calculate_quality_score(spec.symbol, tf, cleaned_df)
                integrity_after = run_integrity_checks(cleaned_df)

                # Build Report
                report = build_cleaning_report(
                    symbol=spec.symbol,
                    timeframe=tf,
                    raw_df=raw_df,
                    cleaned_df=cleaned_df,
                    cleaning_summary=cleaning_summary,
                    quality_score_before=score_before,
                    quality_score_after=score_after,
                    gap_summary=gap_summary,
                    outlier_summary=outlier_summary,
                    integrity_before=integrity_before,
                    integrity_after=integrity_after,
                )

                if not args.dry_run:
                    # Save Processed Data
                    data_lake.save_processed_ohlcv(spec, tf, cleaned_df)

                    # Save Reports
                    save_cleaning_report_json(
                        report,
                        data_lake.root_dir
                        / "processed"
                        / "cleaning_reports"
                        / f"{data_lake.safe_symbol_name(spec.symbol)}_{tf}_cleaning.json",
                    )

                results.append(
                    {
                        "Symbol": spec.symbol,
                        "Timeframe": tf,
                        "Grade Before": score_before.grade,
                        "Grade After": score_after.grade,
                        "Score Change": score_after.score - score_before.score,
                        "Raw Rows": len(raw_df),
                        "Cleaned Rows": len(cleaned_df),
                        "Dupe Removed": cleaning_summary.get(
                            "duplicate_rows_removed", 0
                        ),
                    }
                )

            except Exception as e:
                logger.error(f"Error cleaning {spec.symbol} {tf}: {e}")

    if not results:
        logger.warning("No data found to clean.")
        return

    summary_df = pd.DataFrame(results)

    # Save CSV
    output_dir = Path("reports/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    summary_df.to_csv(output_dir / "data_cleaning_summary.csv", index=False)

    # Generate Text Report
    summary_stats = {
        "total_cleaned": len(results),
        "improved": sum(1 for r in results if r["Score Change"] > 0),
        "degraded": sum(1 for r in results if r["Score Change"] < 0),
        "avg_improvement": (
            sum(r["Score Change"] for r in results) / len(results) if results else 0
        ),
        "total_dupes_removed": sum(r["Dupe Removed"] for r in results),
    }

    report_text = build_data_cleaning_report(summary_df, summary_stats)
    with open(output_dir / "data_cleaning_report.txt", "w", encoding="utf-8") as f:
        f.write(report_text)

    logger.info("Data Cleaning complete.")
    if args.dry_run:
        logger.info("DRY RUN: No data was saved.")


if __name__ == "__main__":
    main()
