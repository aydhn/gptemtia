import argparse
from pathlib import Path
from config.settings import Settings
from config.paths import PROJECT_ROOT
from data.storage.data_lake import DataLake
from local_readiness.readiness_config import get_local_readiness_profile
from local_readiness.readiness_pipeline import LocalReadinessPipeline
from local_readiness.acceptance_criteria import build_milestone_acceptance_criteria, map_acceptance_criteria_to_evidence
from reports.report_builder import build_readiness_gate_registry_text_report

def main():
    parser = argparse.ArgumentParser(description="Run readiness gate registry.")
    parser.add_argument("--profile", type=str, default="balanced_local_readiness")
    parser.add_argument("--save", type=str, default="true")
    args = parser.parse_args()

    settings = Settings()
    data_lake = DataLake(PROJECT_ROOT / "data")
    profile = get_local_readiness_profile(args.profile)
    save = args.save.lower() == "true"

    pipeline = LocalReadinessPipeline(data_lake, settings, PROJECT_ROOT, profile)

    # Gates
    gates_out, summary = pipeline.build_readiness_gate_registry(save=save)

    # Acceptance
    crit_df, crit_summ = build_milestone_acceptance_criteria(profile)
    mapped_df, _ = map_acceptance_criteria_to_evidence(crit_df, PROJECT_ROOT)
    if save:
        data_lake.save_milestone_acceptance_criteria(mapped_df, crit_summ)

    # Phase Evidence Index
    from local_readiness.phase_evidence_binder import build_phase_evidence_index
    idx_df, idx_summ = build_phase_evidence_index(PROJECT_ROOT, profile)

    if save:
        from config.paths import REPORTS_LOCAL_READINESS_CSV_DIR, REPORTS_LOCAL_READINESS_MD_DIR, REPORTS_LOCAL_READINESS_TXT_DIR
        REPORTS_LOCAL_READINESS_CSV_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS_LOCAL_READINESS_MD_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS_LOCAL_READINESS_TXT_DIR.mkdir(parents=True, exist_ok=True)

        # Save additional CSVs
        mapped_df.to_csv(REPORTS_LOCAL_READINESS_CSV_DIR / "milestone_acceptance_criteria.csv", index=False)
        idx_df.to_csv(REPORTS_LOCAL_READINESS_CSV_DIR / "phase_evidence_index.csv", index=False)
        gates_out["gate_registry"].to_csv(REPORTS_LOCAL_READINESS_CSV_DIR / "readiness_gate_registry.csv", index=False)

        # Markdown
        from local_readiness.readiness_report_builder import build_readiness_gate_registry_markdown_report
        md = build_readiness_gate_registry_markdown_report(summary, gates_out["gate_registry"])
        with open(REPORTS_LOCAL_READINESS_MD_DIR / "readiness_gate_registry_report.md", "w") as f:
            f.write(md)

        # Text
        txt = build_readiness_gate_registry_text_report(summary, gates_out["gate_registry"])
        with open(REPORTS_LOCAL_READINESS_TXT_DIR / "readiness_gate_registry_report.txt", "w") as f:
            f.write(txt)

if __name__ == "__main__":
    main()
