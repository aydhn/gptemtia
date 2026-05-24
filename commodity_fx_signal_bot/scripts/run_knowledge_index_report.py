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
    parser = argparse.ArgumentParser(description="Run Knowledge Index Report")
    parser.add_argument("--profile", type=str, default="balanced_local_knowledge_base", help="Knowledge base profile name")
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

    logger.info(f"Running Knowledge Index Report with profile '{args.profile}'...")
    data, summary = pipeline.build_knowledge_index_report(save=args.save)

    logger.info("Knowledge Index Run Complete.")
    logger.info(f"Summary: {summary.get('index', {})}")
    if args.save:
        logger.info("Reports saved to data/lake/knowledge_base and reports/output/knowledge_base")

if __name__ == "__main__":
    main()
