import argparse
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import Settings
from data.storage.data_lake import DataLake
from local_acceptance.acceptance_pipeline import LocalAcceptancePipeline
from local_acceptance.acceptance_config import get_local_acceptance_profile
from local_acceptance.acceptance_report_builder import build_acceptance_quality_markdown_report
from reports.report_builder import ReportBuilder

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="strict_acceptance_safety")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    settings = Settings()
    data_lake = DataLake(settings.paths if hasattr(settings, 'paths') else str(Path(__file__).resolve().parent.parent / 'data' / 'lake'))
    report_builder = ReportBuilder(settings, data_lake)
    profile = get_local_acceptance_profile(args.profile)
    pipeline = LocalAcceptancePipeline(data_lake, settings, project_root, profile)

    q, s = pipeline.build_acceptance_quality_report(save=True)
    
    md = build_acceptance_quality_markdown_report(s, q)
    txt = report_builder.build_acceptance_quality_text_report(s, q)
    
    md_path = settings.paths["output_local_acceptance_markdown"] / "acceptance_quality_report.md"
    txt_path = settings.paths["output_local_acceptance_txt"] / "acceptance_quality_report.txt"
    json_path = settings.paths["output_local_acceptance_json"] / "acceptance_quality_report.json"
    
    md_path.parent.mkdir(parents=True, exist_ok=True)
    txt_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(md_path, "w", encoding="utf-8") as f: f.write(md)
    with open(txt_path, "w", encoding="utf-8") as f: f.write(txt)
    with open(json_path, "w", encoding="utf-8") as f: json.dump(q, f, indent=2)
    
    print("Acceptance quality report saved.")

if __name__ == "__main__":
    main()
