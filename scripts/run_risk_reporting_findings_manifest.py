# -*- coding: utf-8 -*-
"""Phase 155: Run Risk Reporting Findings & Manifest Script."""

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

    dfs, summary = pipeline.build_findings_scoring_manifest(save=True)

    print("=" * 70)
    print("PHASE 155: RISK REPORTING FINDINGS & MANIFEST")
    print("=" * 70)
    print(f"Total Findings        : {summary['findings']['finding_count']}")
    print(f"Critical Findings     : {summary['findings']['critical_count']}")
    print(f"Readiness Score       : {summary['scoring']['readiness_score']:.4f}")
    print(f"Classification        : {summary['scoring']['classification']}")
    print(f"Manifest Name         : {summary['manifest']['manifest_name']}")
    print(f"Phase 156 Handoff OK  : {summary['manifest']['phase_156_handoff_ready']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
