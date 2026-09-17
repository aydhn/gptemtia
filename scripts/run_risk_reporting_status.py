# -*- coding: utf-8 -*-
"""Phase 155: Run Risk Reporting Status Script.

Generates consolidated status across all Phase 155 sub-registries and pipeline outputs.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_risk_reporting.risk_reporting_config import (
    get_default_risk_reporting_profile,
)
from advanced_risk_reporting.risk_reporting_pipeline import (
    RiskReportingPipeline,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_risk_reporting_profile()
    pipeline = RiskReportingPipeline(data_lake=data_lake, settings=settings, profile=profile)

    df_status, s_status = pipeline.build_risk_reporting_status(save=True)

    print("=" * 70)
    print("PHASE 155: RISK REPORTING STATUS OVERVIEW")
    print("=" * 70)
    print(f"Profile Name              : {profile.profile_name}")
    print(f"Current Phase             : {s_status['current_phase']}")
    print(f"Next Phase                : {s_status['next_phase']}")
    print(f"Target Final Phase        : {s_status['target_final_phase']}")
    print(f"Pipeline Status           : {s_status['pipeline_status']}")
    print(f"Total Components          : {s_status['total_components']}")
    print(f"All Ready                 : {s_status['all_ready']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
