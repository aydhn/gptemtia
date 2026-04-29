import argparse
from pathlib import Path

import pandas as pd

from config.symbols import get_enabled_symbols
from config.timeframes import list_timeframes
from core.logger import get_logger
from data.storage.data_lake import DataLake
from reports.report_builder import build_processed_data_status_report

logger = get_logger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Check the status of Processed Data Lake."
    )
    args = parser.parse_args()

    logger.info("Checking Processed Data Status...")

    lake_dir = Path("data/lake")
    data_lake = DataLake(lake_dir)

    symbols = get_enabled_symbols()

    timeframes_by_symbol = {
        s.symbol: tuple(t.name for t in list_timeframes()) for s in symbols
    }

    results = []

    for spec in symbols:
        allowed_tfs = timeframes_by_symbol.get(spec.symbol, tuple())
        for tf in allowed_tfs:
            has_raw = data_lake.has_ohlcv(spec, tf)
            has_processed = data_lake.has_processed_ohlcv(spec, tf)

            if not has_raw and not has_processed:
                continue

            raw_rows = len(data_lake.load_ohlcv(spec, tf)) if has_raw else 0
            processed_rows = (
                len(data_lake.load_processed_ohlcv(spec, tf)) if has_processed else 0
            )

            # Try to load cleaning report
            cleaning_report = data_lake.load_cleaning_report(spec, tf)
            quality_after = (
                cleaning_report.get("quality_after", "N/A")
                if cleaning_report
                else "N/A"
            )
            score_after = (
                cleaning_report.get("score_after", 0.0) if cleaning_report else 0.0
            )

            results.append(
                {
                    "Symbol": spec.symbol,
                    "Timeframe": tf,
                    "Has Raw": has_raw,
                    "Has Processed": has_processed,
                    "Raw Rows": raw_rows,
                    "Processed Rows": processed_rows,
                    "Processed Grade": quality_after,
                    "Processed Score": score_after,
                }
            )

    if not results:
        logger.warning("No data found in lake.")
        return

    status_df = pd.DataFrame(results)

    output_dir = Path("reports/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    status_df.to_csv(output_dir / "processed_data_status.csv", index=False)

    summary = {
        "total_combinations": len(results),
        "missing_processed": sum(
            1 for r in results if r["Has Raw"] and not r["Has Processed"]
        ),
        "fully_processed": sum(1 for r in results if r["Has Processed"]),
        "processed_grades": status_df[status_df["Has Processed"]]["Processed Grade"]
        .value_counts()
        .to_dict(),
    }

    report_text = build_processed_data_status_report(status_df, summary)
    with open(
        output_dir / "processed_data_status_report.txt", "w", encoding="utf-8"
    ) as f:
        f.write(report_text)

    logger.info("Processed Data Status check complete.")
    logger.info(f"Missing processed data for {summary['missing_processed']} items.")


if __name__ == "__main__":
    main()
