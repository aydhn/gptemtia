# -*- coding: utf-8 -*-
"""Phase 144: Run Model Governance Status Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from advanced_model_governance.model_governance_pipeline import ModelGovernancePipeline
from reports.report_builder import ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER


def main():
    pipe = ModelGovernancePipeline()
    status_df, summary = pipe.build_model_governance_status(save=True)
    print("=" * 70)
    print("PHASE 144: MODEL GOVERNANCE END-TO-END PIPELINE STATUS")
    print("=" * 70)
    print(ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Phase: {summary['phase']} -> Next: {summary['next_phase']} (Target Final: {summary['target_final_phase']})")
    print(f"Profile: {summary['profile_name']}")
    print(f"Readiness Score: {summary['readiness_score']}")
    print(f"Classification: {summary['classification']}")
    print(f"Production Ready: {summary['production_ready']}")
    print(f"Broker Ready: {summary['broker_ready']}")
    print(f"Live Trading: {summary['live_trading']}")
    print(f"Model Registry Writes: {summary['model_registry_write']}")
    print(f"Artifact Persisted: {summary['artifact_persisted']}")
    print("-" * 70)
    print("Component Status Table:")
    for _, row in status_df.iterrows():
        print(f"  - {row['component']}: {row['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
