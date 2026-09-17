# -*- coding: utf-8 -*-
"""Phase 156: Run Portfolio Scenario Control Validation Report Script."""

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

    df_val, summary = pipeline.build_validation_report(save=True)

    print("=" * 70)
    print("PHASE 156: VALIDATION REPORT")
    print("=" * 70)
    print(f"Validation Status : {summary['status']}")
    print(f"Total Rules       : {summary['total_checks']}")
    print(f"All Passed        : {summary['all_passed']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
