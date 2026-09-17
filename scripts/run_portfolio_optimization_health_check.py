# -*- coding: utf-8 -*-
"""Phase 154: Run Portfolio Optimization Health Check Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_portfolio_optimization.portfolio_optimization_config import (
    get_default_portfolio_optimization_profile,
)
from advanced_portfolio_optimization.portfolio_optimization_pipeline import (
    PortfolioOptimizationPipeline,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_portfolio_optimization_profile()
    pipeline = PortfolioOptimizationPipeline(data_lake=data_lake, settings=settings, profile=profile)

    dfs, summary = pipeline.build_health_validation_safety_handoff(save=True)

    print("=" * 70)
    print("PHASE 154: PORTFOLIO OPTIMIZATION HEALTH CHECK")
    print("=" * 70)
    print(f"Health Status         : {summary['health_summary']['overall_status']}")
    print(f"Total Components      : {summary['health_summary']['total_components']}")
    print(f"Healthy Count         : {summary['health_summary']['healthy_count']}")
    print(f"All Healthy           : {summary['health_summary']['all_healthy']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
