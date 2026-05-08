import argparse
import sys
import logging
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
import reports.report_builder as report_builder
from ml.model_registry import ModelRegistry

def main():
    paths = ProjectPaths()
    data_lake = DataLake(paths)
    registry = ModelRegistry(data_lake.paths.ml_model_registry)


    df = registry.list_entries()

    summary = {
        "count": len(df) if not df.empty else 0
    }

    report = report_builder.build_ml_model_registry_status_report(df, summary)
    print(report)

    out_path_txt = paths.ml_training_reports / "ml_model_registry_status_report.txt"
    with open(out_path_txt, "w") as f:
        f.write(report)

    if not df.empty:
        out_path_csv = paths.ml_training_reports / "ml_model_registry_status.csv"
        df.to_csv(out_path_csv, index=False)

if __name__ == "__main__":
    main()
