import argparse
import pandas as pd
from config.settings import Settings
from config.paths import PROJECT_ROOT
from data.storage.data_lake import DataLake
from local_readiness.readiness_config import get_local_readiness_profile
from local_readiness.readiness_pipeline import LocalReadinessPipeline
from local_readiness.readiness_validation import build_readiness_validation_report
from reports.report_builder import build_readiness_quality_text_report

def main():
    parser = argparse.ArgumentParser(description="Run readiness quality report.")
    parser.add_argument("--profile", type=str, default="balanced_local_readiness")
    parser.add_argument("--save", type=str, default="true")
    args = parser.parse_args()

    settings = Settings()
    data_lake = DataLake(PROJECT_ROOT / "data")
    profile = get_local_readiness_profile(args.profile)
    save = args.save.lower() == "true"

    pipeline = LocalReadinessPipeline(data_lake, settings, PROJECT_ROOT, profile)
    quality_dict, summary = pipeline.build_readiness_quality_report(save=save)

    val_df, _ = build_readiness_validation_report({}, profile)

    if save:
        import json
        from config.paths import REPORTS_LOCAL_READINESS_CSV_DIR, REPORTS_LOCAL_READINESS_MD_DIR, REPORTS_LOCAL_READINESS_TXT_DIR, REPORTS_LOCAL_READINESS_JSON_DIR
        REPORTS_LOCAL_READINESS_CSV_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS_LOCAL_READINESS_MD_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS_LOCAL_READINESS_TXT_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS_LOCAL_READINESS_JSON_DIR.mkdir(parents=True, exist_ok=True)

        val_df.to_csv(REPORTS_LOCAL_READINESS_CSV_DIR / "readiness_validation_report.csv", index=False)

        with open(REPORTS_LOCAL_READINESS_JSON_DIR / "readiness_quality_report.json", "w") as f:
            json.dump(quality_dict, f, indent=2)

        from local_readiness.readiness_report_builder import build_readiness_quality_markdown_report
        md = build_readiness_quality_markdown_report(summary, quality_dict)
        with open(REPORTS_LOCAL_READINESS_MD_DIR / "readiness_quality_report.md", "w") as f:
            f.write(md)

        txt = build_readiness_quality_text_report(summary, quality_dict)
        with open(REPORTS_LOCAL_READINESS_TXT_DIR / "readiness_quality_report.txt", "w") as f:
            f.write(txt)

if __name__ == "__main__":
    main()
