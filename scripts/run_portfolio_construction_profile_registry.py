# -*- coding: utf-8 -*-
"""Phase 153: Run Portfolio Construction Profile Registry Script."""

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

    dfs, summary = pipeline.build_profiles_domains_scope(save=True)

    print("=" * 70)
    print("PHASE 153: PORTFOLIO CONSTRUCTION PROFILE & DOMAIN REGISTRY")
    print("=" * 70)
    print(f"Active Profile : {summary['profiles']['active_profile']}")
    print(f"Total Profiles : {summary['profiles']['total_profiles']}")
    print(f"Total Domains  : {summary['domains']['total_domains']}")
    print(f"Total Scopes   : {summary['scope']['total_scopes']}")
    print(f"Status         : {summary['profiles']['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
