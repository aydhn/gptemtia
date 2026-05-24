import argparse
import sys
from pathlib import Path

from config.settings import settings
from data.storage.data_lake import DataLake
from core.logger import get_logger
from knowledge_base.kb_pipeline import KnowledgeBasePipeline
from knowledge_base.kb_config import get_knowledge_base_profile

logger = get_logger(__name__)

def parse_args():
    parser = argparse.ArgumentParser(description="Run Research Query")
    parser.add_argument("--query", type=str, required=True, help="Search query")
    parser.add_argument("--symbol", type=str, help="Filter by symbol")
    parser.add_argument("--module", type=str, help="Filter by module")
    parser.add_argument("--document-type", type=str, help="Filter by document type")
    parser.add_argument("--top-k", type=int, default=10, help="Number of results")
    parser.add_argument("--profile", type=str, default="balanced_local_knowledge_base")
    parser.add_argument("--save", action="store_true", default=True, help="Save outputs")
    parser.add_argument("--no-save", dest="save", action="store_false")
    return parser.parse_args()

def main():
    args = parse_args()

    if not settings.knowledge_base_enabled:
        logger.warning("Knowledge Base is disabled in settings.")
        sys.exit(0)

    try:
        profile = get_knowledge_base_profile(args.profile)
    except Exception as e:
        logger.error(f"Error loading profile: {e}")
        sys.exit(1)

    project_root = Path(__file__).parent.parent
    data_lake = DataLake(project_root)

    pipeline = KnowledgeBasePipeline(
        data_lake=data_lake,
        settings=settings,
        project_root=project_root,
        profile=profile
    )

    # Check if index exists by trying to load it (or just run pipeline which builds it)
    logger.info(f"Running research query: '{args.query}'")

    # We use query engine via pipeline
    df, summary = pipeline.run_research_query(
        query_text=args.query,
        symbol=args.symbol,
        module_name=args.module,
        document_type=args.document_type,
        save=args.save
    )

    logger.info(f"Query returned {summary.get('matches', 0)} matches.")
    if not df.empty:
        for idx, row in df.head(3).iterrows():
            print(f"Match {idx+1}: {row.get('title', 'Unknown')} (Score: {row.get('final_score', 0):.2f})")

if __name__ == "__main__":
    main()
