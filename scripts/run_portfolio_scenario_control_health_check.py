# -*- coding: utf-8 -*-
"""Phase 156: Run Portfolio Scenario Control Health Check Script."""

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

    df_hlth, summary = pipeline.build_health_check(save=True)

    print("=" * 70)
    print("PHASE 156: HEALTH CHECK REPORT")
    print("=" * 70)
    print(f"Status        : {summary['status']}")
    print(f"Total Checks  : {summary['total_checks']}")
    print(f"Passed Checks : {summary['passed_checks']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
