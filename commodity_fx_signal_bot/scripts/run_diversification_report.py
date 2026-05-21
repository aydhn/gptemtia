#!/usr/bin/env python3
import argparse
import sys
import logging
from pathlib import Path

# Fix python path
sys.path.append(str(Path(__file__).parent.parent))

from config.settings import settings
from data.storage.data_lake import DataLake
from config.symbols import SymbolSpec
from portfolio_research.portfolio_config import get_portfolio_research_profile
from portfolio_research.portfolio_pipeline import PortfolioResearchPipeline

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def parse_args():
    parser = argparse.ArgumentParser(description="Run Diversification Report")
    parser.add_argument("--asset-class", type=str, help="Filter by asset class")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe")
    parser.add_argument("--limit", type=int, help="Limit number of symbols")
    return parser.parse_args()

def main():
    args = parse_args()
    data_lake = DataLake()
    profile = get_portfolio_research_profile("balanced_portfolio_research")
    specs = []

    pipeline = PortfolioResearchPipeline(data_lake, settings, profile)
    logger.info("Diversification report stub executed. Run run_portfolio_research_report.py for the full suite.")

if __name__ == "__main__":
    main()
