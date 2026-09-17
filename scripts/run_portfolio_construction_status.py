# -*- coding: utf-8 -*-
"""Phase 153: Run Portfolio Construction Status Script.

Generates consolidated status across all Phase 153 sub-registries and pipeline outputs.
"""

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

    df_status, s_status = pipeline.build_portfolio_construction_status(save=True)

    print("=" * 70)
    print("PHASE 153: PORTFOLIO CONSTRUCTION STATUS OVERVIEW")
    print("=" * 70)
    print(f"Profile Name              : {s_status['active_profile']}")
    print(f"Current Phase             : {s_status['current_phase']}")
    print(f"Next Phase                : {s_status['next_phase']}")
    print(f"Target Final Phase        : {s_status['target_final_phase']}")
    print(f"Readiness Score           : {s_status['readiness_score']:.4f}")
    print(f"Classification            : {s_status['classification']}")
    print(f"Overall Contract Status   : {s_status['status']}")
    print(f"Non-Signal                : {s_status['non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
