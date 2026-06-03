#!/usr/bin/env python3
import argparse
import sys
import logging
import json
from pathlib import Path

# Fix python path
sys.path.append(str(Path(__file__).parent.parent))

from config.settings import settings
from config.paths import DATA_DIR
from data.storage.data_lake import DataLake
from config.symbols import SymbolSpec
from portfolio_research.portfolio_config import get_portfolio_research_profile
from portfolio_research.portfolio_pipeline import PortfolioResearchPipeline

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def parse_args():
    parser = argparse.ArgumentParser(description="Run Portfolio Research Report")
    parser.add_argument("--asset-class", type=str, help="Filter by asset class")
    parser.add_argument("--symbol", type=str, help="Filter by symbol")
    parser.add_argument("--limit", type=int, help="Limit number of symbols")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe (default: 1d)")
    parser.add_argument("--profile", type=str, default="balanced_portfolio_research", help="Research profile")
    parser.add_argument("--no-save", action="store_true", help="Do not save output")
    return parser.parse_args()

def main():
    args = parse_args()

    data_lake = DataLake(DATA_DIR / "lake")
    profile = get_portfolio_research_profile(args.profile)

    processed_dir = data_lake.paths.processed_ohlcv
    specs = []

    if processed_dir.exists():
        for f in processed_dir.glob(f"*_{args.timeframe}.parquet"):
            sym = f.stem.split("_")[0]
            if args.symbol and sym != args.symbol:
                continue

            ac = "unknown"
            if sym.endswith("=F"): ac = "metals"
            elif sym.endswith("=X"): ac = "forex"

            if args.asset_class and ac != args.asset_class:
                continue

            specs.append(SymbolSpec(symbol=sym, asset_class=ac, base_currency="USD", quote_currency="USD", currency="USD", name="test", sub_class="test"))

    if not specs:
        specs = [
            SymbolSpec(symbol="GC=F", asset_class="metals", base_currency="XAU", quote_currency="USD", currency="USD", name="Gold", sub_class="Precious"),
            SymbolSpec(symbol="SI=F", asset_class="metals", base_currency="XAG", quote_currency="USD", currency="USD", name="Silver", sub_class="Precious"),
            SymbolSpec(symbol="HG=F", asset_class="metals", base_currency="XCU", quote_currency="USD", currency="USD", name="Copper", sub_class="Base")
        ]

    if args.limit:
        specs = specs[:args.limit]

    pipeline = PortfolioResearchPipeline(data_lake, settings, profile)
    report, info = pipeline.build_portfolio_research(specs, args.timeframe, save=not args.no_save)

    if report.report_id:
        logger.info(f"Report generated: {report.report_id}")
        if info["quality"]["passed"]:
            logger.info("Quality checks passed.")
        else:
            logger.warning("Quality checks failed or warnings exist.")
            logger.warning(json.dumps(info["warnings"], indent=2))

        print(f"\n--- PORTFOLIO RESEARCH REPORT ({args.timeframe}) ---\n")
        print(report.markdown[:500] + "\n... [TRUNCATED] ...\n")
    else:
        logger.error("Failed to generate report.")

if __name__ == "__main__":
    main()
