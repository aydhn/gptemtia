# -*- coding: utf-8 -*-
"""Phase 144: Run Model Governance Contracts Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from advanced_model_governance.model_governance_pipeline import ModelGovernancePipeline
from reports.report_builder import ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER


def main():
    pipe = ModelGovernancePipeline()
    tables, summary = pipe.build_governance_contracts(save=True)
    print("=" * 70)
    print("PHASE 144: MODEL GOVERNANCE CONTRACTS REGISTRY")
    print("=" * 70)
    print(ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Governance Contracts: {len(tables['governance_contracts'])}")
    print(f"Total Validation Evidences: {len(tables['governance_validation_evidence'])}")
    print(f"Total Risk Register Items: {len(tables['governance_risk_register'])}")
    print(f"Total Control Checklist Items: {len(tables['governance_control_checklists'])}")
    print("=" * 70)


if __name__ == "__main__":
    main()
