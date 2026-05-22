import argparse
import sys
import logging
import pandas as pd
from pathlib import Path

# Fix python path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import settings
from data.storage.data_lake import DataLake
from config.symbols import DEFAULT_SYMBOL_UNIVERSE
from factor_research.factor_pipeline import FactorResearchPipeline
from factor_research.factor_config import get_factor_research_profile

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Run factor score report")
    parser.add_argument("--asset-class", type=str, help="Filter by asset class")
    parser.add_argument("--limit", type=int, help="Limit number of symbols")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe")
    parser.add_argument("--profile", type=str, default="balanced_factor_research", help="Profile")
    args = parser.parse_args()

    # Placeholder for running just score portion
    logger.info("Running factor score report...")
    logger.info("This is typically handled in the main factor research pipeline.")

if __name__ == "__main__":
    main()
