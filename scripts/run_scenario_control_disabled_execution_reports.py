# -*- coding: utf-8 -*-
"""Phase 156: Run Scenario Control Disabled Execution Reports Script."""

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

    dfs, summary = pipeline.build_disabled_execution_reports(save=True)

    print("=" * 70)
    print("PHASE 156: DISABLED EXECUTION REPORTS")
    print("=" * 70)
    print(f"Scenario Execution Disabled : {summary['scenario_disabled_summary']['disabled']}")
    print(f"Drawdown Control Disabled   : {summary['drawdown_disabled_summary']['disabled']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
