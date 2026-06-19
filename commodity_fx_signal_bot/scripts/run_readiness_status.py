import argparse
import pandas as pd
from config.settings import Settings
from config.paths import PROJECT_ROOT
from data.storage.data_lake import DataLake
from local_readiness.readiness_config import get_local_readiness_profile
from local_readiness.readiness_pipeline import LocalReadinessPipeline
from reports.report_builder import build_readiness_status_report

def main():
    parser = argparse.ArgumentParser(description="Run readiness status report.")
    parser.add_argument("--profile", type=str, default="balanced_local_readiness")
    parser.add_argument("--save", type=str, default="true")
    args = parser.parse_args()

    settings = Settings()
    data_lake = DataLake(PROJECT_ROOT / "data")
    profile = get_local_readiness_profile(args.profile)
    save = args.save.lower() == "true"

    pipeline = LocalReadinessPipeline(data_lake, settings, PROJECT_ROOT, profile)
    df, summary = pipeline.build_readiness_status(save=save)

    if save:
        from config.paths import REPORTS_LOCAL_READINESS_CSV_DIR, REPORTS_LOCAL_READINESS_TXT_DIR
        REPORTS_LOCAL_READINESS_CSV_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS_LOCAL_READINESS_TXT_DIR.mkdir(parents=True, exist_ok=True)

        df.to_csv(REPORTS_LOCAL_READINESS_CSV_DIR / "readiness_status.csv", index=False)

        txt = build_readiness_status_report(df, summary)
        with open(REPORTS_LOCAL_READINESS_TXT_DIR / "readiness_status_report.txt", "w") as f:
            f.write(txt)

if __name__ == "__main__":
    main()
