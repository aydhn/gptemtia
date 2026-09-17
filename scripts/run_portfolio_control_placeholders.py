# -*- coding: utf-8 -*-
"""Phase 156: Run Portfolio Control Action Placeholders Script."""

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

    dfs, summary = pipeline.build_portfolio_control_placeholders(save=True)

    print("=" * 70)
    print("PHASE 156: PORTFOLIO CONTROL ACTION PLACEHOLDERS")
    print("=" * 70)
    print(f"Exposure Reduction : {summary['reduction_summary']['total_reduction_placeholders']}")
    print(f"De-Risking         : {summary['derisking_summary']['total_derisking_placeholders']}")
    print(f"Hedge Control      : {summary['hedge_summary']['total_hedge_placeholders']}")
    print(f"Execution Disabled : {summary['reduction_summary']['execution_disabled']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
