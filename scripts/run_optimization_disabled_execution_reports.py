# -*- coding: utf-8 -*-
"""Phase 154: Run Optimization Disabled Execution Reports Script."""

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

    dfs, summary = pipeline.build_disabled_execution_reports(save=True)

    print("=" * 70)
    print("PHASE 154: OPTIMIZATION DISABLED EXECUTION REPORTS")
    print("=" * 70)
    print(f"Optimization Execution Disabled : {summary['opt_disabled']['portfolio_optimization_disabled']}")
    print(f"Weight Generation Disabled      : {summary['weight_disabled']['weight_generation_disabled']}")
    print(f"Live Trading Disabled           : {summary['live_disabled']['live_trading_disabled']}")
    print(f"Broker Execution Disabled       : {summary['broker_disabled']['broker_execution_disabled']}")
    print(f"Runtime Policy Lock Active      : {summary['opt_disabled']['runtime_policy_lock_active']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
