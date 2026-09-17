# -*- coding: utf-8 -*-
"""Phase 144: Run Governance Disabled Execution Reports Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from advanced_model_governance.model_governance_pipeline import ModelGovernancePipeline
from reports.report_builder import ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER


def main():
    pipe = ModelGovernancePipeline()
    tables, summary = pipe.build_disabled_execution_reports(save=True)
    print("=" * 70)
    print("PHASE 144: GOVERNANCE DISABLED EXECUTION ENFORCEMENT REPORTS")
    print("=" * 70)
    print(ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Disabled Enforcement Policies: {summary.get('total_reports', len(tables))}")
    print(f"All Disabled Enforced: {summary.get('all_disabled', True)}")
    for name, df in tables.items():
        is_disabled = df["is_disabled"].all() if "is_disabled" in df.columns else True
        print(f"  - {name}: enforced={is_disabled}")
    print("=" * 70)


if __name__ == "__main__":
    main()
