# -*- coding: utf-8 -*-
"""Phase 153: Run Portfolio Construction Health Check Script."""

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

    df_hlth, s_hlth = pipeline.build_health_check(save=True)

    print("=" * 70)
    print("PHASE 153: PORTFOLIO CONSTRUCTION HEALTH CHECK")
    print("=" * 70)
    print(f"Total Components : {s_hlth['total_components']}")
    print(f"Healthy Count    : {s_hlth['healthy_count']}")
    print(f"All Healthy      : {s_hlth['all_healthy']}")
    print(f"Status           : {s_hlth['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
