# -*- coding: utf-8 -*-
"""Phase 156: Run Portfolio Scenario Testing Contracts Script."""

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

    dfs, summary = pipeline.build_scenario_testing_contracts(save=True)

    print("=" * 70)
    print("PHASE 156: PORTFOLIO SCENARIO TESTING CONTRACTS")
    print("=" * 70)
    print(f"Total Contracts    : {summary['scenario_contracts_summary']['total_contracts']}")
    print(f"Resilience Count   : {summary['resilience_summary']['total_resilience_contracts']}")
    print(f"Library Count      : {summary['library_summary']['total_libraries']}")
    print(f"Execution Disabled : {summary['scenario_contracts_summary']['all_execution_disabled']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
