# -*- coding: utf-8 -*-
"""Phase 143: Run Explainability Pipeline Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_explainability_attribution.explainability_pipeline import run_explainability_pipeline
from reports.report_builder import ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    result = run_explainability_pipeline()

    print("=" * 70)
    print("PHASE 143: EXPLAINABILITY AND FEATURE ATTRIBUTION PIPELINE")
    print("=" * 70)
    print(ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Profile: {result['profile']}")
    print(f"Readiness Score: {result['readiness']['readiness_score']:.2f}")
    print(f"Classification: {result['readiness']['classification']}")
    print(f"Report Contracts: {result['reports_summary']['total_report_contracts']}")
    print(f"Attribution Contracts: {result['attribution_summary']['total_attribution_contracts']}")
    print(f"Safeguards Verified: {result['safeguards_summary']['all_execution_disabled']}")
    print(f"Zero Violations: {result['safeguards_summary']['zero_violations']}")
    print(f"Success: {result['success']}")
    print(f"Current Phase: {result['current_phase']} | Next Phase: {result['next_phase']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
