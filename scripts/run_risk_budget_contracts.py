# -*- coding: utf-8 -*-
"""Phase 153: Run Risk Budget Contracts Script."""

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

    dfs, summary = pipeline.build_risk_budget_contracts(save=True)

    print("=" * 70)
    print("PHASE 153: RISK BUDGET CONTRACTS & PLACEHOLDERS")
    print("=" * 70)
    print(f"Total Rules   : {summary['risk_budget'].get('total_contracts', len(dfs['risk_budget_contracts']))}")
    print(f"Per Asset     : {len(dfs['per_asset'])} rules")
    print(f"Per Strategy  : {len(dfs['per_strategy'])} rules")
    print(f"Per Regime    : {len(dfs['per_regime'])} rules")
    print(f"Portfolio Lvl : {len(dfs['portfolio'])} rules")
    print(f"Status        : {summary['risk_budget']['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
