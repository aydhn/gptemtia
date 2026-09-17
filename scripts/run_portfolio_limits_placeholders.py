# -*- coding: utf-8 -*-
"""Phase 153: Run Portfolio Limits Placeholders Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_portfolio_construction.portfolio_construction_config import (
    get_default_portfolio_construction_profile,
)
from advanced_portfolio_construction.portfolio_construction_pipeline import (
    PortfolioConstructionPipeline,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_portfolio_construction_profile()
    pipeline = PortfolioConstructionPipeline(data_lake=data_lake, settings=settings, profile=profile)

    dfs, summary = pipeline.build_limits_placeholders(save=True)

    print("=" * 70)
    print("PHASE 153: PORTFOLIO LIMIT CONTRACTS & PLACEHOLDERS")
    print("=" * 70)
    print(f"Concentration Limits: {summary['concentration']['total_limits']}")
    print(f"Exposure Limits     : {summary['exposure']['total_limits']}")
    print(f"Leverage Rules      : {len(dfs['leverage'])}")
    print(f"Margin Rules        : {len(dfs['margin'])}")
    print(f"Notional Rules      : {len(dfs['notional'])}")
    print(f"Status              : {summary['concentration']['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
