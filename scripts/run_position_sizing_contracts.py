# -*- coding: utf-8 -*-
"""Phase 153: Run Position Sizing Contracts Script."""

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

    dfs, summary = pipeline.build_position_sizing_contracts(save=True)

    print("=" * 70)
    print("PHASE 153: POSITION SIZING CONTRACTS & PLACEHOLDERS")
    print("=" * 70)
    print(f"Total Sizing Models : {summary['sizing'].get('total_contracts', len(dfs['sizing_contracts']))}")
    print(f"Fixed Fractional    : {len(dfs['fixed_fractional'])} rules")
    print(f"Volatility Targeting: {len(dfs['volatility_targeting'])} rules")
    print(f"Risk Parity         : {len(dfs['risk_parity'])} rules")
    print(f"Drawdown Aware      : {len(dfs['drawdown_aware'])} rules")
    print(f"Status              : {summary['sizing']['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
