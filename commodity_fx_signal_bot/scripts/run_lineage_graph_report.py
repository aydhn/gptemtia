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
    parser = argparse.ArgumentParser(description="Run Lineage Graph Report")
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

    res, meta = pipeline.build_lineage_graph_report(save=args.save)
    nodes_df = res["nodes"]
    edges_df = res["edges"]


    txt_report = rb.build_lineage_graph_text_report(meta, nodes_df, edges_df)

    if args.save:
        txt_path = paths.REPORTS_GOVERNANCE_TXT_DIR / "lineage_graph_report.txt"
        txt_path.parent.mkdir(parents=True, exist_ok=True)
        with open(txt_path, "w") as f:
            f.write(txt_report)

        csv_n = paths.REPORTS_GOVERNANCE_CSV_DIR / "lineage_nodes.csv"
        csv_e = paths.REPORTS_GOVERNANCE_CSV_DIR / "lineage_edges.csv"
        csv_n.parent.mkdir(parents=True, exist_ok=True)
        nodes_df.to_csv(csv_n, index=False)
        edges_df.to_csv(csv_e, index=False)

        print(f"Lineage graph report generated at {txt_path}")
    else:
        print(txt_report)

if __name__ == "__main__":
    main()
