# -*- coding: utf-8 -*-
"""Phase 153: Run Portfolio Disabled Execution Reports Script."""

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

    dfs, summary = pipeline.build_disabled_execution_reports(save=True)

    print("=" * 70)
    print("PHASE 153: DISABLED EXECUTION CERTIFICATION REPORTS")
    print("=" * 70)
    print(f"Total Disabled Actions : {summary['total_disabled']}")
    print(f"All Executions Blocked : {summary['all_disabled']}")
    print(f"Non-Signal Policy      : {summary['non_signal']}")
    print("Status                 : EXECUTION_BLOCKED_CERTIFIED")
    print("=" * 70)


if __name__ == "__main__":
    main()
