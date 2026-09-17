# -*- coding: utf-8 -*-
"""Phase 156: Run Drawdown Control Contracts Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_portfolio_scenario_control.portfolio_scenario_control_config import (
    get_default_portfolio_scenario_control_profile,
)
from advanced_portfolio_scenario_control.portfolio_scenario_control_pipeline import (
    PortfolioScenarioControlPipeline,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_portfolio_scenario_control_profile()
    pipeline = PortfolioScenarioControlPipeline(data_lake=data_lake, settings=settings, profile=profile)

    dfs, summary = pipeline.build_drawdown_control_contracts(save=True)

    print("=" * 70)
    print("PHASE 156: DRAWDOWN CONTROL CONTRACTS")
    print("=" * 70)
    print(f"Total Drawdown Contracts : {summary['drawdown_summary']['total_drawdown_control_contracts']}")
    print(f"Threshold Tiers Count    : {summary['threshold_summary']['total_threshold_tiers']}")
    print(f"Execution Disabled       : {summary['drawdown_summary']['all_execution_disabled']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
