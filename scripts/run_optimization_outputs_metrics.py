# -*- coding: utf-8 -*-
"""Phase 154: Run Optimization Outputs & Metrics Script."""

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
    print("PHASE 154: OPTIMIZATION OUTPUT CONTRACTS & METRICS")
    print("=" * 70)
    print(f"Output Contract Name     : {summary['output_summary']['output_contract_name']}")
    print(f"Contract Ready           : {summary['output_summary']['contract_ready']}")
    print(f"Zero Actual Weights      : {summary['output_summary']['zero_actual_weights']}")
    print(f"Metric Placeholders      : {summary['metric_summary']['metric_count']}")
    print(f"All Metrics Placeholders : {summary['metric_summary']['all_metrics_placeholders']}")
    print(f"Zero Metrics Calculated  : {summary['metric_summary']['zero_metrics_calculated']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
