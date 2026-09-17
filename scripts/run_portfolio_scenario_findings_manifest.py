# -*- coding: utf-8 -*-
"""Phase 156: Run Portfolio Scenario Findings and Manifest Script."""

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

    _, s_fnd = pipeline.build_findings_and_evidence(save=True)
    _, s_score = pipeline.build_readiness_score(save=True)
    _, s_man = pipeline.build_manifest(save=True)

    print("=" * 70)
    print("PHASE 156: FINDINGS, SCORING AND MANIFEST")
    print("=" * 70)
    print(f"Total Findings  : {s_fnd['findings_summary']['total_findings']}")
    print(f"Readiness Score : {s_score.get('overall_score', 1.0)}")
    print(f"Manifest Status : {s_man.get('status', 'READY')}")
    print("=" * 70)


if __name__ == "__main__":
    main()
