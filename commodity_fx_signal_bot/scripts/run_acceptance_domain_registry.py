import argparse
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import Settings
from data.storage.data_lake import DataLake
from local_acceptance.acceptance_pipeline import LocalAcceptancePipeline
from local_acceptance.acceptance_config import get_local_acceptance_profile
from local_acceptance.acceptance_report_builder import build_acceptance_domain_registry_markdown_report
from reports.report_builder import ReportBuilder

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_acceptance")
    parser.add_argument("--save", type=bool, default=True)
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    settings = Settings()
    data_lake = DataLake(settings.paths if hasattr(settings, 'paths') else str(Path(__file__).resolve().parent.parent / 'data' / 'lake'))
    report_builder = ReportBuilder(settings, data_lake)
    profile = get_local_acceptance_profile(args.profile)

    pipeline = LocalAcceptancePipeline(data_lake, settings, project_root, profile)
    dfs, summary = pipeline.build_acceptance_domain_registry(save=args.save)
    
    if args.save:
        md = build_acceptance_domain_registry_markdown_report(summary["domain"], dfs["domain"])
        txt = report_builder.build_acceptance_domain_registry_text_report(summary["domain"], dfs["domain"])
        
        md_path = settings.paths["output_local_acceptance_markdown"] / "acceptance_domain_registry_report.md"
        txt_path = settings.paths["output_local_acceptance_txt"] / "acceptance_domain_registry_report.txt"
        
        md_path.parent.mkdir(parents=True, exist_ok=True)
        txt_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(md_path, "w", encoding="utf-8") as f: f.write(md)
        with open(txt_path, "w", encoding="utf-8") as f: f.write(txt)
        
        csv_dir = settings.paths["output_local_acceptance_csv"]
        csv_dir.mkdir(parents=True, exist_ok=True)
        dfs["domain"].to_csv(csv_dir / "acceptance_domain_registry.csv", index=False)
        dfs["criteria"].to_csv(csv_dir / "acceptance_criteria_registry.csv", index=False)
        dfs["no_go"].to_csv(csv_dir / "acceptance_no_go_register.csv", index=False)
        dfs["safe_go"].to_csv(csv_dir / "acceptance_safe_go_register.csv", index=False)
        
        print("Acceptance domain registry saved.")

if __name__ == "__main__":
    main()
