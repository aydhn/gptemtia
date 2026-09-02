import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import Settings
from data.storage.data_lake import DataLake
from local_acceptance.acceptance_pipeline import LocalAcceptancePipeline
from local_acceptance.acceptance_config import get_local_acceptance_profile
from local_acceptance.acceptance_report_builder import build_acceptance_evidence_trail_markdown_report
from reports.report_builder import ReportBuilder

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="evidence_trail_focus")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    settings = Settings()
    data_lake = DataLake(settings.paths if hasattr(settings, 'paths') else str(Path(__file__).resolve().parent.parent / 'data' / 'lake'))
    report_builder = ReportBuilder(settings, data_lake)
    profile = get_local_acceptance_profile(args.profile)
    pipeline = LocalAcceptancePipeline(data_lake, settings, project_root, profile)

    dfs, summary = pipeline.build_acceptance_evidence_trail(save=True)
    
    md = build_acceptance_evidence_trail_markdown_report(summary["evidence"], dfs["evidence"])
    txt = report_builder.build_acceptance_evidence_trail_text_report(summary["evidence"], dfs["evidence"])
    
    md_path = settings.paths["output_local_acceptance_markdown"] / "acceptance_evidence_trail_report.md"
    txt_path = settings.paths["output_local_acceptance_txt"] / "acceptance_evidence_trail_report.txt"
    
    md_path.parent.mkdir(parents=True, exist_ok=True)
    txt_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(md_path, "w", encoding="utf-8") as f: f.write(md)
    with open(txt_path, "w", encoding="utf-8") as f: f.write(txt)
    
    csv_dir = settings.paths["output_local_acceptance_csv"]
    csv_dir.mkdir(parents=True, exist_ok=True)
    dfs["evidence"].to_csv(csv_dir / "audit_style_local_evidence_trail.csv", index=False)
    dfs["output_trace"].to_csv(csv_dir / "evidence_output_trace_matrix.csv", index=False)
    dfs["test_trace"].to_csv(csv_dir / "evidence_test_trace_matrix.csv", index=False)
    dfs["doc_trace"].to_csv(csv_dir / "evidence_doc_trace_matrix.csv", index=False)
    dfs["safety_trace"].to_csv(csv_dir / "evidence_safety_boundary_trace_matrix.csv", index=False)
    
    print("Acceptance evidence trail saved.")

if __name__ == "__main__":
    main()
