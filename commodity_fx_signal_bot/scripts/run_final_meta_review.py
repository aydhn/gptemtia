
import argparse
from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from local_closure.closure_pipeline import LocalClosurePipeline
from local_closure.closure_config import get_local_closure_profile
from local_closure.closure_report_builder import build_final_meta_review_markdown_report
from reports.report_builder import ReportBuilder

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="meta_review_focus")
    parser.add_argument("--save", type=bool, default=True)
    args = parser.parse_args()

    settings = Settings()
    data_lake = DataLake('data/lake')
    report_builder = ReportBuilder(data_lake, None, settings) # type: ignore
    project_root = Path.cwd()
    
    profile = get_local_closure_profile(args.profile)
    pipeline = LocalClosurePipeline(data_lake, settings, project_root, profile)
    
    text, summary = pipeline.build_final_meta_review(save=args.save)
    
    if args.save:
        md = build_final_meta_review_markdown_report(summary, text)
        txt = report_builder.build_final_meta_review_text_report(summary, text)
        with open(settings.paths.OUTPUT_CLOSURE_MARKDOWN / "final_meta_review_report.md", "w", encoding="utf-8") as f:
            f.write(md)
        with open(settings.paths.OUTPUT_CLOSURE_TXT / "final_meta_review_report.txt", "w", encoding="utf-8") as f:
            f.write(txt)
        with open(settings.paths.DOCS_LOCAL_CLOSURE / "FINAL_PROJECT_META_REVIEW_REPORT.md", "w", encoding="utf-8") as f:
            f.write(md)
            
    print("Final meta review completed.")

if __name__ == "__main__":
    main()
