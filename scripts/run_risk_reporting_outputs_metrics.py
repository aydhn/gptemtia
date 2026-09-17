# -*- coding: utf-8 -*-
"""Phase 155: Run Risk Reporting Outputs & Metrics Script."""

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

    dfs, summary = pipeline.build_outputs_metrics(save=True)

    print("=" * 70)
    print("PHASE 155: RISK REPORTING OUTPUTS & METRIC PLACEHOLDERS")
    print("=" * 70)
    print(f"Risk Output Contracts     : {summary['risk_output']['output_contract_count']}")
    print(f"Exposure Output Contracts : {summary['exposure_output']['output_contract_count']}")
    print(f"Limit Output Contracts    : {summary['limit_output']['output_contract_count']}")
    print(f"Metrics Offline Only      : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
