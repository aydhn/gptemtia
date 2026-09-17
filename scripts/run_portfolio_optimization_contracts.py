# -*- coding: utf-8 -*-
"""Phase 154: Run Portfolio Optimization Contracts Script."""

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

    dfs, summary = pipeline.build_optimization_contracts(save=True)

    print("=" * 70)
    print("PHASE 154: PORTFOLIO OPTIMIZATION CONTRACTS")
    print("=" * 70)
    print(f"Total Contracts       : {summary['contract_summary']['contract_count']}")
    print(f"Zero Optimization     : {summary['contract_summary']['all_contracts_disallow_optimization']}")
    print(f"Zero Weight Gen       : {summary['contract_summary']['all_contracts_disallow_weight_generation']}")
    print(f"Zero Live Trading     : {summary['contract_summary']['all_contracts_disallow_live_trading']}")
    print(f"Manual Review Req     : {summary['contract_summary']['manual_review_required_all']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
