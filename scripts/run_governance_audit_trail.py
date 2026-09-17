# -*- coding: utf-8 -*-
"""Phase 144: Run Governance Audit Trail Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from advanced_model_governance.model_governance_pipeline import ModelGovernancePipeline
from reports.report_builder import ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER


def main():
    pipe = ModelGovernancePipeline()
    tables, summary = pipe.build_audit_placeholders(save=True)
    print("=" * 70)
    print("PHASE 144: GOVERNANCE AUDIT TRAIL PLACEHOLDERS")
    print("=" * 70)
    print(ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Audit Trail Placeholders: {len(tables['audit_trail_placeholders'])}")
    print(f"Decision Log Placeholders: {len(tables['decision_log_placeholders'])}")
    print(f"Change Log Placeholders: {len(tables['change_log_placeholders'])}")
    print(f"Owner Responsibility Placeholders: {len(tables['owner_responsibility_placeholders'])}")
    print(f"Lifecycle Placeholders: {len(tables['lifecycle_placeholders'])}")
    print(f"Version Placeholders: {len(tables['version_placeholders'])}")
    print(f"Governance Audit Placeholders: {len(tables['governance_audit_placeholders'])}")
    print("=" * 70)


if __name__ == "__main__":
    main()
