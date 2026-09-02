import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import Settings
from data.storage.data_lake import DataLake
from local_acceptance.acceptance_pipeline import LocalAcceptancePipeline
from local_acceptance.acceptance_config import get_local_acceptance_profile
from local_acceptance.acceptance_report_builder import build_independent_reviewer_pack_markdown_report
from reports.report_builder import ReportBuilder

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="independent_reviewer_focus")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    settings = Settings()
    data_lake = DataLake(settings.paths if hasattr(settings, 'paths') else str(Path(__file__).resolve().parent.parent / 'data' / 'lake'))
    report_builder = ReportBuilder(settings, data_lake)
    profile = get_local_acceptance_profile(args.profile)
    pipeline = LocalAcceptancePipeline(data_lake, settings, project_root, profile)

    text, summary = pipeline.build_independent_reviewer_pack(save=True)
    
    md = build_independent_reviewer_pack_markdown_report(summary, text)
    txt = report_builder.build_independent_reviewer_pack_text_report(summary, text)
    
    md_path = settings.paths["output_local_acceptance_markdown"] / "independent_reviewer_pack.md"
    txt_path = settings.paths["output_local_acceptance_txt"] / "independent_reviewer_pack.txt"
    
    md_path.parent.mkdir(parents=True, exist_ok=True)
    txt_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(md_path, "w", encoding="utf-8") as f: f.write(md)
    with open(txt_path, "w", encoding="utf-8") as f: f.write(txt)
    
    docs_dir = settings.paths["docs_generated_local_acceptance"]
    docs_dir.mkdir(parents=True, exist_ok=True)
    with open(docs_dir / "INDEPENDENT_REVIEWER_PACK.md", "w", encoding="utf-8") as f: f.write(md)
    
    print("Independent reviewer pack saved.")

if __name__ == "__main__":
    main()
