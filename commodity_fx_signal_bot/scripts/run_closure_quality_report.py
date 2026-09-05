
import argparse
import json
from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from local_closure.closure_pipeline import LocalClosurePipeline
from local_closure.closure_config import get_local_closure_profile
from local_closure.closure_report_builder import build_closure_quality_markdown_report
from reports.report_builder import ReportBuilder

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="strict_closure_safety")
    parser.add_argument("--save", type=bool, default=True)
    args = parser.parse_args()

    settings = Settings()
    data_lake = DataLake('data/lake')
    report_builder = ReportBuilder(data_lake, None, settings) # type: ignore
    project_root = Path.cwd()
    
    profile = get_local_closure_profile(args.profile)
    pipeline = LocalClosurePipeline(data_lake, settings, project_root, profile)
    
    quality, summary = pipeline.build_closure_quality_report(save=args.save)
    
    if args.save:
        md = build_closure_quality_markdown_report(summary, quality)
        txt = report_builder.build_closure_quality_text_report(summary, quality)
        with open(settings.paths.OUTPUT_CLOSURE_MARKDOWN / "closure_quality_report.md", "w", encoding="utf-8") as f:
            f.write(md)
        with open(settings.paths.OUTPUT_CLOSURE_TXT / "closure_quality_report.txt", "w", encoding="utf-8") as f:
            f.write(txt)
        with open(settings.paths.OUTPUT_CLOSURE_JSON / "closure_quality_report.json", "w", encoding="utf-8") as f:
            json.dump(quality, f, indent=2)
            
    print("Closure quality report completed.")

if __name__ == "__main__":
    main()
