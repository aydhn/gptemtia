# -*- coding: utf-8 -*-
"""Phase 154: Run Portfolio Optimization Findings & Manifest Script."""

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

    dfs, summary = pipeline.build_findings_scoring_manifest(save=True)

    print("=" * 70)
    print("PHASE 154: PORTFOLIO OPTIMIZATION FINDINGS & MANIFEST")
    print("=" * 70)
    print(f"Total Findings        : {summary['finding_summary']['finding_count']}")
    print(f"Blocker Findings      : {summary['finding_summary']['blocker_count']}")
    print(f"Readiness Score       : {summary['readiness_summary']['readiness_score']:.4f}")
    print(f"Classification        : {summary['readiness_summary']['classification']}")
    print(f"Manifest Name         : {summary['manifest_summary']['manifest_name']}")
    print(f"Phase 155 Handoff OK  : {summary['manifest_summary']['phase_155_handoff_ready']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
