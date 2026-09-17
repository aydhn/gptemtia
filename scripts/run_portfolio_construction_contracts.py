# -*- coding: utf-8 -*-
"""Phase 153: Run Portfolio Construction Contracts Script."""

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

    dfs, summary = pipeline.build_portfolio_contracts(save=True)

    print("=" * 70)
    print("PHASE 153: PORTFOLIO CONSTRUCTION CONTRACTS")
    print("=" * 70)
    print(f"Total Contracts       : {summary['contracts'].get('total_contracts', len(dfs['contracts']))}")
    print(f"Universe Assets       : {summary['universe'].get('total_assets', len(dfs['universe']))}")
    print(f"Eligibility Rules     : {summary['eligibility'].get('total_rules', len(dfs['eligibility']))}")
    print(f"Signal Input Specs    : {summary['signals'].get('total_signal_inputs', len(dfs['signals']))}")
    print(f"Risk Input Specs      : {summary['risks'].get('total_risk_inputs', len(dfs['risks']))}")
    print(f"Status                : {summary['contracts']['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
