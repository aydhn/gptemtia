#!/usr/bin/env python3
import argparse
import sys
import logging
from pathlib import Path

# Fix python path
sys.path.append(str(Path(__file__).parent.parent))

from config.settings import settings
from config.paths import DATA_DIR
from data.storage.data_lake import DataLake
from config.symbols import SymbolSpec
from portfolio_research.portfolio_config import get_portfolio_research_profile
from portfolio_research.portfolio_pipeline import PortfolioResearchPipeline

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def parse_args():
    parser = argparse.ArgumentParser(description="Run Correlation Analysis Report")
    parser.add_argument("--asset-class", type=str, help="Filter by asset class")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe (default: 1d)")
    parser.add_argument("--limit", type=int, help="Limit number of symbols")
    return parser.parse_args()

def main():
    args = parse_args()
    data_lake = DataLake(DATA_DIR / "lake")
    profile = get_portfolio_research_profile("balanced_portfolio_research")

    specs = [
        SymbolSpec(symbol="GC=F", asset_class="metals", base_currency="XAU", quote_currency="USD", currency="USD", name="Gold", sub_class="Precious"),
        SymbolSpec(symbol="SI=F", asset_class="metals", base_currency="XAG", quote_currency="USD", currency="USD", name="Silver", sub_class="Precious")
    ]

    pipeline = PortfolioResearchPipeline(data_lake, settings, profile)
    report, info = pipeline.build_correlation_report(specs, args.timeframe, save=True)

    logger.info("Correlation analysis completed. Run build_portfolio_research for full report.")

if __name__ == "__main__":
    main()
