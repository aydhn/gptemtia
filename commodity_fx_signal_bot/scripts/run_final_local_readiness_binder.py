import argparse
from config.settings import Settings
from config.paths import PROJECT_ROOT, DOCS_GENERATED_LOCAL_READINESS_DIR
from data.storage.data_lake import DataLake
from local_readiness.readiness_config import get_local_readiness_profile
from local_readiness.readiness_pipeline import LocalReadinessPipeline
from reports.report_builder import build_final_local_readiness_binder_text_report

def main():
    parser = argparse.ArgumentParser(description="Run final local readiness binder.")
    parser.add_argument("--profile", type=str, default="balanced_local_readiness")
    parser.add_argument("--save", type=str, default="true")
    args = parser.parse_args()

    settings = Settings()
    data_lake = DataLake(PROJECT_ROOT / "data")
    profile = get_local_readiness_profile(args.profile)
    save = args.save.lower() == "true"

    pipeline = LocalReadinessPipeline(data_lake, settings, PROJECT_ROOT, profile)
    binder_text, summary = pipeline.build_final_local_readiness_binder(save=save)

    if save:
        from config.paths import REPORTS_LOCAL_READINESS_MD_DIR, REPORTS_LOCAL_READINESS_TXT_DIR
        REPORTS_LOCAL_READINESS_MD_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS_LOCAL_READINESS_TXT_DIR.mkdir(parents=True, exist_ok=True)
        DOCS_GENERATED_LOCAL_READINESS_DIR.mkdir(parents=True, exist_ok=True)

        with open(DOCS_GENERATED_LOCAL_READINESS_DIR / "FINAL_LOCAL_READINESS_BINDER.md", "w") as f:
            f.write(binder_text)

        with open(DOCS_GENERATED_LOCAL_READINESS_DIR / "PHASE_COMPLETION_EVIDENCE_BINDER.md", "w") as f:
            f.write(binder_text)

        from local_readiness.readiness_report_builder import build_final_local_readiness_binder_markdown_report
        md = build_final_local_readiness_binder_markdown_report(summary, binder_text)
        with open(REPORTS_LOCAL_READINESS_MD_DIR / "final_local_readiness_binder.md", "w") as f:
            f.write(md)

        txt = build_final_local_readiness_binder_text_report(summary, binder_text)
        with open(REPORTS_LOCAL_READINESS_TXT_DIR / "final_local_readiness_binder.txt", "w") as f:
            f.write(txt)

if __name__ == "__main__":
    main()
