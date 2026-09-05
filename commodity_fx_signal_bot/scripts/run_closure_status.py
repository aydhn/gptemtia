
import argparse
from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from local_closure.closure_pipeline import LocalClosurePipeline
from local_closure.closure_config import get_local_closure_profile
from local_closure.closure_report_builder import build_closure_status_markdown_report
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
    
    df, summary = pipeline.build_closure_status(save=args.save)
    
    if args.save:
        md = build_closure_status_markdown_report(summary, df)
        txt = report_builder.build_closure_status_report(df, summary)
        df.to_csv(settings.paths.OUTPUT_CLOSURE_CSV / "closure_status.csv", index=False)
        with open(settings.paths.OUTPUT_CLOSURE_TXT / "closure_status_report.txt", "w", encoding="utf-8") as f:
            f.write(txt)
            
    print("Closure status completed.")

if __name__ == "__main__":
    main()
