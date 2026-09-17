# -*- coding: utf-8 -*-
"""Phase 154: Run Portfolio Optimization Status Script.

Generates consolidated status across all Phase 154 sub-registries and pipeline outputs.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_portfolio_optimization.portfolio_optimization_config import (
    get_default_portfolio_optimization_profile,
)
from advanced_portfolio_optimization.portfolio_optimization_pipeline import (
    PortfolioOptimizationPipeline,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_portfolio_optimization_profile()
    pipeline = PortfolioOptimizationPipeline(data_lake=data_lake, settings=settings, profile=profile)

    df_status, s_status = pipeline.build_portfolio_optimization_status(save=True)

    print("=" * 70)
    print("PHASE 154: PORTFOLIO OPTIMIZATION STATUS OVERVIEW")
    print("=" * 70)
    print(f"Profile Name              : {profile.profile_name}")
    print(f"Current Phase             : {s_status['current_phase']}")
    print(f"Next Phase                : {s_status['next_phase']}")
    print(f"Target Final Phase        : {s_status['target_final_phase']}")
    print(f"Pipeline Status           : {s_status['pipeline_status']}")
    print(f"All Stages Completed      : {s_status['all_stages_completed']}")
    print(f"Phase 155 Handoff Ready   : {s_status['phase_155_handoff_ready']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
