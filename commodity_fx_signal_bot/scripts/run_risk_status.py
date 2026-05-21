"""
Risk Status Report
"""

from pathlib import Path
import pandas as pd

from config.paths import (
    ensure_project_directories,
    REPORTS_RISK_REPORTS_DIR,
    LAKE_FEATURES_RISK_CANDIDATES_DIR,
    LAKE_FEATURES_RISK_POOL_DIR,
)
from reports.report_builder import build_risk_status_report
from core.logger import get_logger

logger = get_logger(__name__)


def main():
    ensure_project_directories()

    cand_files = list(LAKE_FEATURES_RISK_CANDIDATES_DIR.rglob("*.parquet"))
    pool_files = list(LAKE_FEATURES_RISK_POOL_DIR.rglob("*.parquet"))

    data = []
    for f in cand_files:
        # e.g., symbol/1d.parquet
        parts = f.parts
        symbol = parts[-2]
        timeframe = f.stem
        df = pd.read_parquet(f)

        passed = (
            df["passed_risk_precheck"].sum()
            if not df.empty and "passed_risk_precheck" in df.columns
            else 0
        )

        data.append(
            {
                "symbol": symbol,
                "timeframe": timeframe,
                "candidates": len(df),
                "passed": passed,
            }
        )

    status_df = pd.DataFrame(data)

    summary = {"processed_symbols": len(status_df), "pool_files": len(pool_files)}

    report = build_risk_status_report(status_df, summary)
    print("\n" + report + "\n")

    report_file = REPORTS_RISK_REPORTS_DIR / "risk_status_report.txt"
    report_file.write_text(report)

    csv_file = REPORTS_RISK_REPORTS_DIR / "risk_status.csv"
    if not status_df.empty:
        status_df.to_csv(csv_file, index=False)

    logger.info("Saved status reports")


if __name__ == "__main__":
    main()
