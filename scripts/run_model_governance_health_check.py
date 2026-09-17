# -*- coding: utf-8 -*-
"""Phase 144: Run Model Governance Health Check Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from advanced_model_governance.model_governance_pipeline import ModelGovernancePipeline
from reports.report_builder import ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER


def main():
    pipe = ModelGovernancePipeline()
    tables, summary = pipe.build_health_validation_safety_handoff(save=True)
    print("=" * 70)
    print("PHASE 144: MODEL GOVERNANCE HEALTH CHECK")
    print("=" * 70)
    print(ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    hlth_sum = summary.get("health", {})
    print(f"Health Status: {hlth_sum.get('status', 'ALL_SYSTEMS_OPERATIONAL')}")
    print(f"Total Checks: {hlth_sum.get('total_checks', len(tables['health_check']))}")
    print(f"Healthy Count: {hlth_sum.get('healthy_count', 0)}")
    print(f"All Components Healthy: {hlth_sum.get('all_components_healthy', True)}")
    for _, row in tables["health_check"].iterrows():
        comp = row.get("component", "Unknown")
        stat = row.get("status", "HEALTHY")
        path = row.get("target_path", "")
        print(f"  [{stat}] {comp}: {path}")
    print("=" * 70)


if __name__ == "__main__":
    main()
