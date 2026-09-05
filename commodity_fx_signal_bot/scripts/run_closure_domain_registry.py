
import argparse
from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from local_closure.closure_pipeline import LocalClosurePipeline
from local_closure.closure_config import get_local_closure_profile
from local_closure.closure_report_builder import build_closure_domain_registry_markdown_report
from reports.report_builder import ReportBuilder

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_closure")
    parser.add_argument("--save", type=bool, default=True)
    args = parser.parse_args()

    settings = Settings()
    data_lake = DataLake('data/lake')
    report_builder = ReportBuilder(data_lake, None, settings) # type: ignore
    project_root = Path.cwd()
    
    profile = get_local_closure_profile(args.profile)
    pipeline = LocalClosurePipeline(data_lake, settings, project_root, profile)
    
    res, summary = pipeline.build_closure_domain_registry(save=args.save)
    df = res.get("domain_registry")
    
    if args.save and df is not None:
        md = build_closure_domain_registry_markdown_report(summary, df)
        txt = report_builder.build_closure_domain_registry_text_report(summary, df)
        with open(settings.paths.OUTPUT_CLOSURE_MARKDOWN / "closure_domain_registry_report.md", "w", encoding="utf-8") as f:
            f.write(md)
        with open(settings.paths.OUTPUT_CLOSURE_TXT / "closure_domain_registry_report.txt", "w", encoding="utf-8") as f:
            f.write(txt)
            
    print("Closure domain registry completed.")

if __name__ == "__main__":
    main()
