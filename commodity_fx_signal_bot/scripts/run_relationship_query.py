import argparse
from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from config.settings import settings
from data.storage.data_lake import DataLake
from local_knowledge_graph.graph_config import get_local_knowledge_graph_profile
from local_knowledge_graph.graph_pipeline import LocalKnowledgeGraphPipeline
from reports.report_builder import build_relationship_query_text_report
from config.paths import REPORTS_LOCAL_KNOWLEDGE_GRAPH_TXT_DIR, REPORTS_LOCAL_KNOWLEDGE_GRAPH_MARKDOWN_DIR
from local_knowledge_graph.graph_report_builder import build_relationship_query_markdown_report

def main():
    parser = argparse.ArgumentParser(description="Run Relationship Query")
    parser.add_argument("--query", type=str, required=True, help="Query string")
    parser.add_argument("--profile", type=str, default="balanced_local_graph")
    parser.add_argument("--save", type=bool, default=True)
    args = parser.parse_args()

    data_lake = DataLake(PROJECT_ROOT / "data")
    profile = get_local_knowledge_graph_profile(args.profile)
    pipeline = LocalKnowledgeGraphPipeline(data_lake, settings, project_root, profile)

    print(f"Running Relationship Query '{args.query}' with profile: {profile.name}")
    results_df, summary = pipeline.build_relationship_query_report(query_text=args.query, save=args.save)

    if args.save:
        md_content = build_relationship_query_markdown_report(summary, results_df)
        txt_content = build_relationship_query_text_report(summary, results_df)

        md_path = REPORTS_LOCAL_KNOWLEDGE_GRAPH_MARKDOWN_DIR / "relationship_query_report.md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)

        txt_path = REPORTS_LOCAL_KNOWLEDGE_GRAPH_TXT_DIR / "relationship_query_report.txt"
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(txt_content)

    print("Done.")

if __name__ == "__main__":
    main()
