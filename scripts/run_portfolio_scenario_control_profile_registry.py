# -*- coding: utf-8 -*-
"""Phase 156: Run Portfolio Scenario Control Profile Registry Script."""

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

    dfs, summary = pipeline.build_profiles_domains_scope(save=True)

    print("=" * 70)
    print("PHASE 156: PORTFOLIO SCENARIO CONTROL PROFILES & DOMAINS")
    print("=" * 70)
    print(f"Active Profile : {summary['profile_summary']['active_profile']}")
    print(f"Total Profiles : {summary['profile_summary']['total_profiles']}")
    print(f"Total Domains  : {summary['domain_summary']['total_domains']}")
    print(f"Total Scopes   : {summary['scope_summary']['total_scopes']}")
    print(f"Non-Production : {summary['profile_summary']['all_non_production']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
