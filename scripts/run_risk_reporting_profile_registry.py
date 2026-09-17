# -*- coding: utf-8 -*-
"""Phase 155: Run Risk Reporting Profile Registry Script."""

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

    dfs, summary = pipeline.build_profiles_domains_scope(save=True)

    print("=" * 70)
    print("PHASE 155: RISK REPORTING PROFILE & DOMAIN REGISTRY")
    print("=" * 70)
    print(f"Active Profile : {summary['profile_summary']['active_profile']}")
    print(f"Total Profiles : {summary['profile_summary']['profile_count']}")
    print(f"Total Domains  : {summary['domain_summary']['domain_count']}")
    print(f"Total Scopes   : {summary['scope_summary']['scope_count']}")
    print(f"Non-Production : {summary['profile_summary']['all_profiles_non_production']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
