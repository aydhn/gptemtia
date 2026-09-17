# -*- coding: utf-8 -*-
"""Phase 144: Run Governance Boundaries Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from advanced_model_governance.model_governance_pipeline import ModelGovernancePipeline
from reports.report_builder import ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER


def main():
    pipe = ModelGovernancePipeline()
    tables, summary = pipe.build_boundaries_gates_risk(save=True)
    print("=" * 70)
    print("PHASE 144: GOVERNANCE BOUNDARIES & MANUAL REVIEW GATES")
    print("=" * 70)
    print(ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Approval Boundaries: {len(tables['approval_boundaries'])}")
    print(f"Total Release Boundaries: {len(tables['release_boundaries'])}")
    print(f"Total Non-Production Boundaries: {len(tables['non_production_boundaries'])}")
    print(f"Total Manual Review Gates: {len(tables['manual_review_gates'])}")
    print(f"Total Compliance Placeholders: {len(tables['compliance_placeholders'])}")
    print("=" * 70)


if __name__ == "__main__":
    main()
