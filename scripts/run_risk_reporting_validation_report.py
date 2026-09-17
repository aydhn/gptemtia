# -*- coding: utf-8 -*-
"""Phase 155: Run Risk Reporting Validation Report Script."""

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

    dfs, summary = pipeline.build_health_validation_safety_handoff(save=True)

    print("=" * 70)
    print("PHASE 155: RISK REPORTING VALIDATION & SAFETY REPORT")
    print("=" * 70)
    print(f"Validation Status      : {summary['validation']['status']}")
    print(f"Total Checks           : {summary['validation']['total_checks']}")
    print(f"All Checks Passed      : {summary['validation']['all_passed']}")
    print(f"Safety Status          : {summary['safety']['status']}")
    print(f"NO-GO Rules Enforced   : {summary['safety']['no_go_count']}")
    print(f"SAFE-GO Rules Active   : {summary['safety']['safe_go_count']}")
    print(f"Phase 156 Handoff OK   : {summary['handoff']['handoff_ready']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
