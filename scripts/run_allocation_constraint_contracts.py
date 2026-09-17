# -*- coding: utf-8 -*-
"""Phase 154: Run Allocation Constraint Contracts Script."""

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

    dfs, summary = pipeline.build_allocation_constraints(save=True)

    print("=" * 70)
    print("PHASE 154: ALLOCATION CONSTRAINT CONTRACTS & PLACEHOLDERS")
    print("=" * 70)
    print(f"Total Constraints     : {summary['constraint_summary']['constraint_count']}")
    print(f"All Placeholders      : {summary['constraint_summary']['all_constraints_placeholders']}")
    print(f"Zero Live Enforcement : {summary['constraint_summary']['zero_live_enforcement']}")
    print(f"Zero Weight Gen       : {summary['constraint_summary']['zero_weight_generation']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
