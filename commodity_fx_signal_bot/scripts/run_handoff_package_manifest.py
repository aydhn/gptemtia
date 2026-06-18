import argparse
from config.settings import Settings
from config.paths import PROJECT_ROOT
from data.storage.data_lake import DataLake
from local_readiness.readiness_config import get_local_readiness_profile
from local_readiness.readiness_pipeline import LocalReadinessPipeline
from reports.report_builder import build_handoff_package_manifest_text_report
from local_readiness.go_no_go_registry import build_no_go_condition_registry, build_safe_go_condition_registry
from local_readiness.readiness_scoring import build_readiness_score_report
from local_readiness.risk_summary import build_pre_handoff_risk_summary
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description="Run handoff package manifest.")
    parser.add_argument("--profile", type=str, default="balanced_local_readiness")
    parser.add_argument("--save", type=str, default="true")
    args = parser.parse_args()

    settings = Settings()
    data_lake = DataLake(PROJECT_ROOT / "data")
    profile = get_local_readiness_profile(args.profile)
    save = args.save.lower() == "true"

    pipeline = LocalReadinessPipeline(data_lake, settings, PROJECT_ROOT, profile)
    out, summary = pipeline.build_handoff_package_manifest(save=save)
    manifest_dict = out["handoff_manifest"].to_dict("records")[0] if not out["handoff_manifest"].empty else {}

    no_go_df, _ = build_no_go_condition_registry(profile)
    safe_go_df, _ = build_safe_go_condition_registry(profile)
    score_df, _ = build_readiness_score_report(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), profile)
    risk_df, _ = build_pre_handoff_risk_summary(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), profile)

    idx_df = pd.DataFrame([{"manifest_index": "test"}])

    if save:
        from config.paths import REPORTS_LOCAL_READINESS_CSV_DIR, REPORTS_LOCAL_READINESS_MD_DIR, REPORTS_LOCAL_READINESS_TXT_DIR, REPORTS_LOCAL_READINESS_JSON_DIR
        import json
        REPORTS_LOCAL_READINESS_CSV_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS_LOCAL_READINESS_MD_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS_LOCAL_READINESS_TXT_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS_LOCAL_READINESS_JSON_DIR.mkdir(parents=True, exist_ok=True)

        no_go_df.to_csv(REPORTS_LOCAL_READINESS_CSV_DIR / "no_go_condition_registry.csv", index=False)
        safe_go_df.to_csv(REPORTS_LOCAL_READINESS_CSV_DIR / "safe_go_condition_registry.csv", index=False)
        score_df.to_csv(REPORTS_LOCAL_READINESS_CSV_DIR / "readiness_score_report.csv", index=False)
        risk_df.to_csv(REPORTS_LOCAL_READINESS_CSV_DIR / "pre_handoff_risk_summary.csv", index=False)
        idx_df.to_csv(REPORTS_LOCAL_READINESS_CSV_DIR / "handoff_manifest_index.csv", index=False)

        with open(REPORTS_LOCAL_READINESS_JSON_DIR / "handoff_package_manifest.json", "w") as f:
            json.dump(manifest_dict, f, indent=2)

        from local_readiness.readiness_report_builder import build_handoff_package_manifest_markdown_report
        md = build_handoff_package_manifest_markdown_report(summary, manifest_dict)
        with open(REPORTS_LOCAL_READINESS_MD_DIR / "handoff_package_manifest_report.md", "w") as f:
            f.write(md)

        txt = build_handoff_package_manifest_text_report(summary, manifest_dict)
        with open(REPORTS_LOCAL_READINESS_TXT_DIR / "handoff_package_manifest_report.txt", "w") as f:
            f.write(txt)

if __name__ == "__main__":
    main()
