# -*- coding: utf-8 -*-
"""Phase 155: Run Exposure Attribution Contracts Script."""

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

    dfs, summary = pipeline.build_exposure_attribution_contracts(save=True)

    print("=" * 70)
    print("PHASE 155: EXPOSURE ATTRIBUTION CONTRACTS")
    print("=" * 70)
    print(f"Total Exposure Contracts : {summary['exposure_contract_summary']['contract_count']}")
    print(f"All Placeholders         : {summary['exposure_contract_summary']['all_contracts_placeholder']}")
    print(f"Zero Calculated          : {summary['exposure_contract_summary']['zero_exposure_calculated']}")
    print(f"Gross Placeholders       : {summary['gross_summary']['placeholder_count']}")
    print(f"Net Placeholders         : {summary['net_summary']['placeholder_count']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
