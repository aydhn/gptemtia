import argparse
import pandas as pd
from data.storage.data_lake import DataLake
from config.paths import ProjectPaths
from reports.report_builder import ReportBuilder

def main():
    parser = argparse.ArgumentParser(description="Check ML Datasets Status")
    parser.parse_args()

    paths = ProjectPaths()
    data_lake = DataLake(paths)
    report_builder = ReportBuilder()

    status_df = data_lake.list_ml_datasets()

    summary = {}
    if not status_df.empty:
         summary = {
              "total_datasets": len(status_df),
              "symbols": status_df['symbol'].nunique() if 'symbol' in status_df.columns else 0
         }

    report = report_builder.build_ml_dataset_status_report(status_df, summary)
    print(report)

    paths.ml_reports.mkdir(parents=True, exist_ok=True)

    report_path = paths.ml_reports / "ml_dataset_status_report.txt"
    with open(report_path, "w", encoding="utf-8") as f:
         f.write(report)

    if not status_df.empty:
         csv_path = paths.ml_reports / "ml_dataset_status.csv"
         status_df.to_csv(csv_path, index=False)

if __name__ == "__main__":
    main()
