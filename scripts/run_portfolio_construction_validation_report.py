# -*- coding: utf-8 -*-
"""Phase 153: Run Portfolio Construction Validation Report Script."""

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

    df_val, s_val = pipeline.build_validation_report(save=True)

    print("=" * 70)
    print("PHASE 153: PORTFOLIO CONSTRUCTION VALIDATION REPORT")
    print("=" * 70)
    print(f"Total Checks : {s_val['total_checks']}")
    print(f"Passed Count : {s_val['passed_count']}")
    print(f"All Passed   : {s_val['all_passed']}")
    print(f"Status       : {s_val['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
