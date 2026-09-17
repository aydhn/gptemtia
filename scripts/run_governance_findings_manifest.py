# -*- coding: utf-8 -*-
"""Phase 144: Run Governance Findings and Manifest Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from advanced_model_governance.model_governance_pipeline import ModelGovernancePipeline
from reports.report_builder import ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER


def main():
    pipe = ModelGovernancePipeline()
    tables, summary = pipe.build_findings_scoring_manifest(save=True)
    print("=" * 70)
    print("PHASE 144: GOVERNANCE FINDINGS, SCORING & MANIFEST")
    print("=" * 70)
    print(ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Findings: {len(tables['findings'])}")
    print(f"Total Manual Review Items: {len(tables['manual_review_queue'])}")
    print(f"Readiness Score: {summary['scoring'].get('readiness_score', 1.0)}")
    print(f"Classification: {summary['scoring'].get('classification', 'governance_contract_ready')}")
    print(f"Manifest Profile: {summary['manifest'].get('profile_name', 'default')}")
    print("=" * 70)


if __name__ == "__main__":
    main()
