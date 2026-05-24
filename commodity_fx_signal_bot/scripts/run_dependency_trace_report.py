import argparse
import sys
import os
from pathlib import Path

# Fix python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.settings import Settings
from config.paths import ProjectPaths, ensure_project_directories
from data.storage.data_lake import DataLake
from governance.governance_pipeline import GovernancePipeline
from governance.governance_config import get_governance_profile
import reports.report_builder as rb

def parse_args():
    parser = argparse.ArgumentParser(description="Run Dependency Trace Report")
    parser.add_argument("--artifact-id", type=str, default=None)
    parser.add_argument("--symbol", type=str, default=None)
    parser.add_argument("--module-name", type=str, default=None)
    parser.add_argument("--direction", type=str, choices=["upstream", "downstream"], default="upstream")
    parser.add_argument("--max-depth", type=int, default=8)
    parser.add_argument("--profile", type=str, default="balanced_research_governance")
    parser.add_argument("--save", type=bool, default=True)
    return parser.parse_args()

def main():
    args = parse_args()

    settings = Settings()
    paths = ProjectPaths()
    ensure_project_directories()

    data_lake = DataLake(paths)
    profile = get_governance_profile(args.profile)

    pipeline = GovernancePipeline(data_lake=data_lake, settings=settings, project_root=paths.project_root, profile=profile)

    df, summary = pipeline.build_dependency_trace_report(
        artifact_id_or_node_id=args.artifact_id,
        symbol=args.symbol,
        module_name=args.module_name,
        direction=args.direction,
        save=args.save
    )


    txt_report = rb.build_dependency_trace_text_report(summary, df)

    if args.save:
        txt_path = paths.REPORTS_GOVERNANCE_TXT_DIR / "dependency_trace_report.txt"
        txt_path.parent.mkdir(parents=True, exist_ok=True)
        with open(txt_path, "w") as f:
            f.write(txt_report)

        csv_path = paths.REPORTS_GOVERNANCE_CSV_DIR / "dependency_trace.csv"
        csv_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(csv_path, index=False)

        print(f"Dependency trace report generated at {txt_path}")
    else:
        print(txt_report)

if __name__ == "__main__":
    main()
