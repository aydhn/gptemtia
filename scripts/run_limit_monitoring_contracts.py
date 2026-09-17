# -*- coding: utf-8 -*-
"""Phase 155: Run Limit Monitoring Contracts Script."""

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

    dfs, summary = pipeline.build_limit_monitoring_contracts(save=True)

    print("=" * 70)
    print("PHASE 155: LIMIT MONITORING CONTRACTS")
    print("=" * 70)
    print(f"Total Limit Contracts : {summary['limit_contract_summary']['contract_count']}")
    print(f"Total Limit Defs      : {summary['definition_summary']['contract_count']}")
    print(f"All Placeholders      : {summary['limit_contract_summary']['all_contracts_placeholder']}")
    print(f"Zero Live Enforcement : {summary['limit_contract_summary']['zero_live_enforcement']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
