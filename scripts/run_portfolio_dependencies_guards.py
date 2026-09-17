# -*- coding: utf-8 -*-
"""Phase 153: Run Portfolio Dependencies & Guards Script."""

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

    dfs, summary = pipeline.build_dependencies_guards(save=True)

    print("=" * 70)
    print("PHASE 153: PORTFOLIO DEPENDENCIES & SAFETY GUARDS")
    print("=" * 70)
    print(f"Dependencies   : {summary['dependencies']['total_dependencies']}")
    print(f"Evidence Items : {len(dfs['evidence'])}")
    print(f"Lookahead Guard: {len(dfs['lookahead_guard'])} active rules")
    print(f"Alloc Claim G  : {len(dfs['allocation_guard'])} active rules")
    print(f"Advice Guard   : {len(dfs['advice_guard'])} active rules")
    print(f"Status         : {summary['dependencies']['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
