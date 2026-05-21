import argparse
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.symbols import get_enabled_symbols, SymbolSpec
from config.settings import settings
from config.paths import ensure_project_directories
from core.logger import get_logger
from data.storage.data_lake import DataLake
from portfolio_regime.regime_config import get_portfolio_regime_profile
from portfolio_regime.regime_pipeline import PortfolioRegimePipeline

logger = get_logger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Run Risk Regime Exposure Report")
    parser.add_argument("--asset-class", type=str, help="Filter by asset class")
    parser.add_argument("--limit", type=int, help="Limit number of symbols")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe (default 1d)")
    parser.add_argument("--profile", type=str, default=settings.default_portfolio_regime_profile, help="Portfolio regime profile name")

    args = parser.parse_args()

    ensure_project_directories()

    specs = get_enabled_symbols()
    if args.asset_class:
        specs = [s for s in specs if s.asset_class == args.asset_class]
    if args.limit:
        specs = specs[:args.limit]

    logger.info(f"Running risk regime exposure report for {len(specs)} symbols on timeframe {args.timeframe}")

    data_lake = DataLake(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')))
    profile = get_portfolio_regime_profile(args.profile)
    pipeline = PortfolioRegimePipeline(data_lake, settings, profile)

    df, summary = pipeline.build_risk_regime_exposure_report(
        specs,
        timeframe=args.timeframe,
        profile=profile,
        limit=args.limit
    )

    logger.info("Report execution completed.")

if __name__ == "__main__":
    main()
