# -*- coding: utf-8 -*-
"""Phase 154: Run Portfolio Optimization Validation Report Script."""

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

    dfs, summary = pipeline.build_health_validation_safety_handoff(save=True)

    print("=" * 70)
    print("PHASE 154: PORTFOLIO OPTIMIZATION VALIDATION & SAFETY REPORT")
    print("=" * 70)
    print(f"Validation Status     : {summary['validation_summary']['overall_status']}")
    print(f"Validation Checks     : {summary['validation_summary']['total_checks']}")
    print(f"All Validated         : {summary['validation_summary']['all_checks_passed']}")
    print(f"Safety NO-GO Rules    : {summary['safety_summary']['no_go_count']}")
    print(f"Safety SAFE-GO Rules  : {summary['safety_summary']['safe_go_count']}")
    print(f"Phase 155 Handoff OK  : {summary['handoff_summary']['all_satisfied']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
