# -*- coding: utf-8 -*-
"""Phase 156: Run Scenario Control Outputs and Metrics Script."""

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

    dfs, summary = pipeline.build_outputs_and_metrics(save=True)

    print("=" * 70)
    print("PHASE 156: SCENARIO CONTROL OUTPUTS AND METRICS")
    print("=" * 70)
    print(f"Scenario Outputs  : {summary['scenario_output_summary']['total_scenario_output_contracts']}")
    print(f"Drawdown Outputs  : {summary['drawdown_output_summary']['total_drawdown_output_contracts']}")
    print(f"Scenario Metrics  : {summary['metric_summary']['total_scenario_metrics']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
