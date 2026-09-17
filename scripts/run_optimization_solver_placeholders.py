# -*- coding: utf-8 -*-
"""Phase 154: Run Optimization Solver Placeholders Script."""

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

    dfs, summary = pipeline.build_solver_outputs_metrics(save=True)

    print("=" * 70)
    print("PHASE 154: OPTIMIZATION SOLVER PLACEHOLDERS & FRONTIERS")
    print("=" * 70)
    print(f"Total Solvers         : {summary['solver_summary']['solver_count']}")
    print(f"Solvers Placeholders  : {summary['solver_summary']['all_solvers_placeholders']}")
    print(f"Zero Executed         : {summary['solver_summary']['zero_solvers_executed']}")
    print(f"Frontier Calculated   : {summary['frontier_summary']['frontier_calculated']}")
    print(f"Frontier Placeholder  : {summary['frontier_summary']['is_placeholder']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
