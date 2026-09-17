# -*- coding: utf-8 -*-
"""Phase 153: Run Portfolio Findings & Manifest Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_portfolio_construction.portfolio_construction_config import (
    get_default_portfolio_construction_profile,
)
from advanced_portfolio_construction.portfolio_construction_pipeline import (
    PortfolioConstructionPipeline,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_portfolio_construction_profile()
    pipeline = PortfolioConstructionPipeline(data_lake=data_lake, settings=settings, profile=profile)

    dfs, summary = pipeline.build_findings_manifest(save=True)

    print("=" * 70)
    print("PHASE 153: PORTFOLIO FINDINGS, READINESS & MASTER MANIFEST")
    print("=" * 70)
    print(f"Total Findings  : {summary['findings']['total_findings']}")
    print(f"Readiness Score : {summary['readiness']['overall_score']:.4f}")
    print(f"Classification  : {summary['readiness']['classification']}")
    print(f"Manifest ID     : {summary['manifest']['manifest_id']}")
    print(f"Handoff Ready   : {summary['manifest']['phase_154_handoff_ready']}")
    print(f"Status          : {summary['manifest']['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
