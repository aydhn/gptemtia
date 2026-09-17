# -*- coding: utf-8 -*-
"""Phase 157: Run Portfolio Acceptance Status Script.

Executes the complete PortfolioAcceptancePipeline and reports global status.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_default_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.portfolio_acceptance_pipeline import (
    PortfolioAcceptancePipeline,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_portfolio_acceptance_profile()

    pipeline = PortfolioAcceptancePipeline(
        data_lake=data_lake,
        settings=settings,
        project_root=Path(__file__).resolve().parent.parent,
        profile=profile,
    )

    df_status, s_full = pipeline.build_portfolio_acceptance_status(save=True)

    print("=" * 70)
    print("PHASE 157: PORTFOLIO ACCEPTANCE STATUS OVERVIEW")
    print("=" * 70)
    print(f"Active Profile        : {s_full['active_profile']}")
    print(f"Readiness Score       : {s_full['readiness_score']:.4f}")
    print(f"Classification        : {s_full['classification']}")
    print(f"Meets Threshold       : {s_full['meets_threshold']}")
    print(f"Handoff Ready         : {s_full['handoff_ready']}")
    print(f"Status                : {s_full['status']}")
    print(f"Non-Signal Guarantee  : {s_full['non_signal']}")
    print("-" * 70)
    for _, row in df_status.iterrows():
        dom = row.get("domain", "")
        st = row.get("status", "")
        print(f"  [{st}] {dom}")
    print("=" * 70)


if __name__ == "__main__":
    main()
