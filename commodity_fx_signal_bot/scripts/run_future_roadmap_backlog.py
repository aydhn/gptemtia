
import argparse
from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from local_closure.closure_pipeline import LocalClosurePipeline
from local_closure.closure_config import get_local_closure_profile
from local_closure.closure_report_builder import build_future_roadmap_markdown_report
from reports.report_builder import ReportBuilder

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="roadmap_focus")
    parser.add_argument("--save", type=bool, default=True)
    args = parser.parse_args()

    settings = Settings()
    data_lake = DataLake(settings)
    report_builder = ReportBuilder(data_lake, None, settings) # type: ignore
    project_root = Path.cwd()
    
    profile = get_local_closure_profile(args.profile)
    pipeline = LocalClosurePipeline(data_lake, settings, project_root, profile)
    
    res, summary = pipeline.build_future_roadmap_backlog(save=args.save)
    df = res.get("roadmap_backlog")
    
    if args.save and df is not None:
        md = build_future_roadmap_markdown_report(summary, df)
        txt = report_builder.build_future_roadmap_text_report(summary, df)
        with open(settings.paths.OUTPUT_CLOSURE_MARKDOWN / "future_roadmap_backlog.md", "w", encoding="utf-8") as f:
            f.write(md)
        with open(settings.paths.OUTPUT_CLOSURE_TXT / "future_roadmap_backlog.txt", "w", encoding="utf-8") as f:
            f.write(txt)
        with open(settings.paths.DOCS_LOCAL_CLOSURE / "FUTURE_ROADMAP_BACKLOG.md", "w", encoding="utf-8") as f:
            f.write(md)
            
    print("Future roadmap backlog completed.")

if __name__ == "__main__":
    main()
