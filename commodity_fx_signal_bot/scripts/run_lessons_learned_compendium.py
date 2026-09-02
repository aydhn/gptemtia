
import argparse
from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from local_closure.closure_pipeline import LocalClosurePipeline
from local_closure.closure_config import get_local_closure_profile
from local_closure.closure_report_builder import build_lessons_learned_markdown_report
from reports.report_builder import ReportBuilder

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_closure")
    parser.add_argument("--save", type=bool, default=True)
    args = parser.parse_args()

    settings = Settings()
    data_lake = DataLake(settings)
    report_builder = ReportBuilder(data_lake, None, settings) # type: ignore
    project_root = Path.cwd()
    
    profile = get_local_closure_profile(args.profile)
    pipeline = LocalClosurePipeline(data_lake, settings, project_root, profile)
    
    res, summary = pipeline.build_lessons_learned_compendium(save=args.save)
    df = res.get("lessons_learned")
    
    if args.save and df is not None:
        md = build_lessons_learned_markdown_report(summary, df)
        txt = report_builder.build_lessons_learned_text_report(summary, df)
        with open(settings.paths.OUTPUT_CLOSURE_MARKDOWN / "lessons_learned_compendium.md", "w", encoding="utf-8") as f:
            f.write(md)
        with open(settings.paths.OUTPUT_CLOSURE_TXT / "lessons_learned_compendium.txt", "w", encoding="utf-8") as f:
            f.write(txt)
        with open(settings.paths.DOCS_LOCAL_CLOSURE / "LESSONS_LEARNED_COMPENDIUM.md", "w", encoding="utf-8") as f:
            f.write(md)
            
    print("Lessons learned compendium completed.")

if __name__ == "__main__":
    main()
