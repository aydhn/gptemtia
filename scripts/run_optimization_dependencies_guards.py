# -*- coding: utf-8 -*-
"""Phase 154: Run Optimization Dependencies & Guards Script."""

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

    dfs, summary = pipeline.build_dependencies_guards(save=True)

    print("=" * 70)
    print("PHASE 154: OPTIMIZATION DEPENDENCIES & GUARDS")
    print("=" * 70)
    print(f"Total Dependencies     : {summary['dependency_summary']['dependency_count']}")
    print(f"Dependencies Verified  : {summary['dependency_summary']['all_dependencies_verified']}")
    print(f"Allocation Guard       : {summary['allocation_guard']['is_active']}")
    print(f"Weight Gen Guard       : {summary['weight_guard']['is_active']}")
    print(f"Advice Guard           : {summary['advice_guard']['is_active']}")
    print(f"Forbidden Columns      : {len(dfs['forbidden_columns'])} quarantined")
    print("=" * 70)


if __name__ == "__main__":
    main()
