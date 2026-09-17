# -*- coding: utf-8 -*-
"""Phase 155: Run Risk Reporting Dependencies & Guards Script."""

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

    dfs, summary = pipeline.build_dependencies_guards(save=True)

    print("=" * 70)
    print("PHASE 155: RISK REPORTING DEPENDENCIES & GUARDS")
    print("=" * 70)
    print(f"Total Dependencies     : {summary['dependency_summary']['dependency_count']}")
    print(f"All Deps Satisfied     : {summary['dependency_summary'].get('all_available', True)}")
    print(f"Total Guards           : {summary['guard_summary']['guard_count']}")
    print(f"All Guards Enforced    : {summary['guard_summary'].get('all_active', True)}")
    print(f"Validation Evidence    : {summary['evidence_summary']['evidence_count']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
