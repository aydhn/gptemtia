# -*- coding: utf-8 -*-
"""Phase 144: Run Model Card Contracts Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from advanced_model_governance.model_governance_pipeline import ModelGovernancePipeline
from reports.report_builder import ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER


def main():
    pipe = ModelGovernancePipeline()
    tables, summary = pipe.build_model_cards(save=True)
    print("=" * 70)
    print("PHASE 144: MODEL CARD CONTRACTS & TEMPLATES REGISTRY")
    print("=" * 70)
    print(ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Model Card Contracts: {len(tables['model_card_contracts'])}")
    print(f"Total Model Card Templates: {len(tables['model_card_templates'])}")
    print(f"Total Model Card Sections: {len(tables['model_card_sections'])}")
    print(f"Total Limitations: {len(tables['model_card_limitations'])}")
    print(f"Total Intended Uses: {len(tables['model_card_intended_use'])}")
    print(f"Total Prohibited Uses: {len(tables['model_card_prohibited_use'])}")
    print(f"Total Risk Disclosures: {len(tables['model_card_risk_disclosures'])}")
    print("=" * 70)


if __name__ == "__main__":
    main()
