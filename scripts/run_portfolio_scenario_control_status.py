# -*- coding: utf-8 -*-
"""Phase 156: Run Portfolio Scenario Control Status Script."""

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

    df_status, s_status = pipeline.build_portfolio_scenario_control_status(save=True)

    print("=" * 70)
    print("PHASE 156: PORTFOLIO SCENARIO CONTROL STATUS OVERVIEW")
    print("=" * 70)
    print(f"Profile Name              : {profile.profile_name}")
    print(f"Current Phase             : {s_status['current_phase']}")
    print(f"Next Phase                : {s_status['next_phase']}")
    print(f"Target Final Phase        : {s_status['target_final_phase']}")
    print(f"Pipeline Status           : {s_status['pipeline_status']}")
    print(f"Total Components          : {s_status['total_components']}")
    print(f"All Ready                 : {s_status['all_ready']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
