import argparse
import sys
import logging
import pandas as pd
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
import reports.report_builder as report_builder
from ml.model_registry import ModelRegistry

def main():
    paths = ProjectPaths()
    data_lake = DataLake(paths)
    registry = ModelRegistry(data_lake.paths.ml_model_registry)


    df = registry.list_entries()

    results = []

    if not df.empty:
        for _, row in df.iterrows():
            model_id = row.get("model_id")
            paths_dict = row.get("artifact_paths", {})

            res = {
                "model_id": model_id,
                "model_family": row.get("model_family"),
                "has_model": False,
                "has_preprocessor": False,
                "has_metadata": False,
                "has_feature_schema": False,
                "has_target_schema": False
            }

            if paths_dict:
                from pathlib import Path
                res["has_model"] = Path(paths_dict.get("model_path", "")).exists()
                res["has_preprocessor"] = Path(paths_dict.get("preprocessor_path", "")).exists()
                res["has_metadata"] = Path(paths_dict.get("metadata_path", "")).exists()
                res["has_feature_schema"] = Path(paths_dict.get("feature_schema_path", "")).exists()
                res["has_target_schema"] = Path(paths_dict.get("target_schema_path", "")).exists()

            results.append(res)

    res_df = pd.DataFrame(results)

    summary = {
        "count": len(res_df) if not res_df.empty else 0
    }

    report = report_builder.build_ml_model_artifact_status_report(res_df, summary)
    print(report)

    out_path_txt = paths.ml_training_reports / "ml_model_artifact_status_report.txt"
    with open(out_path_txt, "w") as f:
        f.write(report)

    if not res_df.empty:
        out_path_csv = paths.ml_training_reports / "ml_model_artifact_status.csv"
        res_df.to_csv(out_path_csv, index=False)

if __name__ == "__main__":
    main()
