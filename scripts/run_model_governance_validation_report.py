# -*- coding: utf-8 -*-
"""Phase 144: Run Model Governance Validation Report Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from advanced_model_governance.model_governance_pipeline import ModelGovernancePipeline
from reports.report_builder import ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER


def main():
    pipe = ModelGovernancePipeline()
    tables, summary = pipe.build_health_validation_safety_handoff(save=True)
    print("=" * 70)
    print("PHASE 144: MODEL GOVERNANCE VALIDATION REPORT")
    print("=" * 70)
    print(ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    val_sum = summary.get("validation", {})
    print(f"Validation Status: {val_sum.get('status', 'PASS')}")
    print(f"Total Checks: {val_sum.get('total_checks', len(tables['validation_report']))}")
    print(f"All Passed: {val_sum.get('all_passed', True)}")
    print(f"Clean Claims: {val_sum.get('clean_claims', True)}")
    for _, row in tables["validation_report"].iterrows():
        chk = row.get("check", "generic_check")
        passed = row.get("passed", True)
        stat = row.get("status", "PASS" if passed else "FAIL")
        print(f"  [{stat}] check={chk} passed={passed}")
    print("=" * 70)


if __name__ == "__main__":
    main()
