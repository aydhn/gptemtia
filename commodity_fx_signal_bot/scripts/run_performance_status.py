import argparse
import sys
import logging
import pandas as pd
from pathlib import Path

from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
import reports.report_builder as builder

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Check the status of generated performance reports."
    )
    args = parser.parse_args()

    logger.info("Checking performance reports status...")

    p = ProjectPaths()
    data_lake = DataLake(str(p.lake_dir))

    if hasattr(data_lake, "list_performance_reports"):
        reports_df = data_lake.list_performance_reports()
    else:
        logger.error("list_performance_reports not found on DataLake.")
        sys.exit(1)

    if reports_df.empty:
        logger.warning("No performance reports found.")
        sys.exit(0)

    status_records = []

    for _, row in reports_df.iterrows():
        sym = row["symbol"]
        tf = row["timeframe"]
        prof = row["profile"]

        summary = data_lake.load_backtest_performance_summary(sym, tf, prof)
        if not summary:
            continue

        adv = summary.get("advanced_metrics", {})
        qual = summary.get("quality_report", {})

        has_bench_file = False
        if hasattr(data_lake.paths, "backtest_benchmark_comparisons"):
            bench_path = (
                data_lake.paths.backtest_benchmark_comparisons
                / f"{sym}_{tf}_{prof}_benchmark.parquet"
            )
            has_bench_file = bench_path.exists()

        status_records.append(
            {
                "symbol": sym,
                "timeframe": tf,
                "profile": prof,
                "trade_count": summary.get("trade_count", 0),
                "total_return_pct": adv.get("total_return_pct", 0.0),
                "sharpe_ratio": adv.get("sharpe_ratio", 0.0),
                "max_drawdown_pct": adv.get("max_drawdown_pct", 0.0),
                "has_benchmark_comparison": has_bench_file,
                "quality_passed": qual.get("passed", False),
            }
        )

    status_df = pd.DataFrame(status_records)

    if hasattr(builder, "build_performance_status_report"):
        report = builder.build_performance_status_report(status_df, {})
    else:
        report = "Performance Status:\n" + status_df.to_string()

    print(report)

    out_dir = (
        p.performance_reports
        if hasattr(p, "performance_reports")
        else p.reports_dir / "performance_reports"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    txt_file = out_dir / "performance_status_report.txt"
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(report)

    csv_file = out_dir / "performance_status.csv"
    status_df.to_csv(csv_file, index=False)

    logger.info(f"Status report saved to {out_dir}")


if __name__ == "__main__":
    main()
