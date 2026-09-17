# -*- coding: utf-8 -*-
"""Phase 155: Run Risk Reporting Disabled Execution Reports Script."""

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

    dfs, summary = pipeline.build_disabled_execution_reports(save=True)

    print("=" * 70)
    print("PHASE 155: RISK REPORTING DISABLED EXECUTION REPORTS")
    print("=" * 70)
    print(f"Risk Report Execution Disabled      : {summary['risk_report'].get('is_disabled', True)}")
    print(f"Exposure Attribution Exec Disabled  : {summary['exposure'].get('is_disabled', True)}")
    print(f"Limit Monitoring Exec Disabled      : {summary['limit'].get('is_disabled', True)}")
    print(f"Limit Alerting Disabled             : {summary['alerting'].get('is_disabled', True)}")
    print("=" * 70)


if __name__ == "__main__":
    main()
