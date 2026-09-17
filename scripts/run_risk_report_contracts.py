# -*- coding: utf-8 -*-
"""Phase 155: Run Risk Report Contracts Script."""

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

    dfs, summary = pipeline.build_risk_report_contracts(save=True)

    print("=" * 70)
    print("PHASE 155: RISK REPORT CONTRACTS")
    print("=" * 70)
    print(f"Total Contracts       : {summary['contract_summary']['contract_count']}")
    print(f"Zero Live Trading     : {summary['contract_summary']['all_contracts_disallow_live_trading']}")
    print(f"Zero Execution        : {summary['contract_summary']['all_contracts_disallow_execution']}")
    print(f"Manual Review Req     : {summary['contract_summary']['manual_review_required_all']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
