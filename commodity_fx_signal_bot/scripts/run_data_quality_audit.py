import argparse
from pathlib import Path

import pandas as pd

from config.settings import settings
from config.symbols import get_enabled_symbols
from config.timeframes import list_timeframes
from core.logger import get_logger
from data.cleaning.quality_scoring import DataQualityScore, calculate_quality_score
from data.storage.data_lake import DataLake
from reports.report_builder import build_data_quality_audit_report

logger = get_logger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Audit data quality of local Data Lake."
    )
    parser.add_argument("--limit", type=int, help="Limit number of symbols to audit.")
    parser.add_argument(
        "--asset-class", type=str, help="Filter by asset class (e.g., metals)."
    )
    parser.add_argument("--symbol", type=str, help="Audit a specific symbol.")
    parser.add_argument("--timeframe", type=str, help="Filter by timeframe (e.g., 1d).")
    parser.add_argument(
        "--use-processed",
        action="store_true",
        help="Audit processed data instead of raw.",
    )

    args = parser.parse_args()

    logger.info("Starting Data Quality Audit")

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

    results = []

    for spec in symbols:
        allowed_tfs = timeframes_by_symbol.get(spec.symbol, tuple())
        if args.timeframe:
            if args.timeframe not in allowed_tfs:
                logger.warning(
                    f"Timeframe {args.timeframe} not allowed for {spec.symbol}"
                )
                continue
            allowed_tfs = (args.timeframe,)

        for tf in allowed_tfs:
            try:
                if args.use_processed:
                    if not data_lake.has_processed_ohlcv(spec, tf):
                        continue
                    df = data_lake.load_processed_ohlcv(spec, tf)
                else:
                    if not data_lake.has_ohlcv(spec, tf):
                        continue
                    df = data_lake.load_ohlcv(spec, tf)

                score: DataQualityScore = calculate_quality_score(
                    symbol=spec.symbol,
                    timeframe=tf,
                    df=df,
                    min_rows=settings.min_ohlcv_rows,
                )

                # Save quality report if auditing raw
                if not args.use_processed:
                    report_dict = {
                        "symbol": spec.symbol,
                        "timeframe": tf,
                        "rows": score.rows,
                        "score": score.score,
                        "grade": score.grade,
                        "report_builder = ReportBuilder()ed": score.report_builder = ReportBuilder()ed,
                        "errors": score.errors,
                        "warnings": score.warnings,
                        "missing_ratio": score.missing_ratio,
                        "outlier_count": score.outlier_count,
                        "gap_count": score.gap_count,
                        "duplicate_count": score.duplicate_count,
                        "notes": score.notes,
                    }
                    data_lake.save_quality_report(spec, tf, report_dict)

                results.append(
                    {
                        "Symbol": spec.symbol,
                        "Asset Class": spec.asset_class,
                        "Timeframe": tf,
                        "Grade": score.grade,
                        "Score": score.score,
                        "Rows": score.rows,
                        "Missing Close": f"{score.missing_ratio:.1%}",
                        "Gaps": score.gap_count,
                        "Outliers": score.outlier_count,
                        "Duplicates": score.duplicate_count,
                        "Errors": len(score.errors),
                        "Warnings": len(score.warnings),
                    }
                )

                logger.info(
                    f"Audited {spec.symbol} {tf}: {score.grade} ({score.score:.1f})"
                )

            except Exception as e:
                logger.error(f"Error auditing {spec.symbol} {tf}: {e}")

    if not results:
        logger.warning("No data found to audit.")
        return

    audit_df = pd.DataFrame(results)

    # Save CSV
    output_dir = Path("reports/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    prefix = "processed_" if args.use_processed else ""
    csv_path = output_dir / f"{prefix}data_quality_audit.csv"
    audit_df.to_csv(csv_path, index=False)

    # Generate Summary
    summary = {
        "total_files": len(results),
        "grades": audit_df["Grade"].value_counts().to_dict(),
        "avg_score": audit_df["Score"].mean(),
        "total_errors": audit_df["Errors"].sum(),
    }

    report_text = build_data_quality_audit_report(audit_df, summary)
    txt_path = output_dir / f"{prefix}data_quality_audit_report.txt"
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(report_text)

    logger.info(f"Data Quality Audit complete. Results saved to {output_dir}")


if __name__ == "__main__":
    main()
