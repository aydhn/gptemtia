# -*- coding: utf-8 -*-
"""Phase 155: Run Risk Monitor Placeholders Script."""

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

    dfs, summary = pipeline.build_monitor_placeholders(save=True)

    print("=" * 70)
    print("PHASE 155: RISK MONITOR PLACEHOLDERS")
    print("=" * 70)
    print(f"Risk Contribution Placeholder Count : {summary['risk_contribution']['placeholder_count']}")
    print(f"Drawdown Monitor Placeholder Count  : {summary['drawdown']['placeholder_count']}")
    print(f"VaR Monitor Placeholder Count       : {summary['var']['placeholder_count']}")
    print(f"ES Monitor Placeholder Count        : {summary['expected_shortfall']['placeholder_count']}")
    print(f"Zero Live Calculation               : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
