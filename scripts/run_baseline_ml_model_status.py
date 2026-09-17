"""Phase 138: Run Baseline ML Model Status Script.

Runs the complete Phase 138 pipeline, persisting all contracts, reports, and manifests.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from advanced_baseline_ml_models.baseline_ml_model_config import (
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.baseline_ml_model_pipeline import (
    run_baseline_ml_model_pipeline,
)
from reports.report_builder import ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER


def main():
    profile = get_default_baseline_ml_model_profile()
    result = run_baseline_ml_model_pipeline(profile)

    print("=" * 70)
    print("PHASE 138: BASELINE ML MODEL PIPELINE & STATUS")
    print("=" * 70)
    print(ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Active Profile       : {result['profile']}")
    print(f"Pipeline Status      : {result['pipeline_status']}")
    print(f"Current Phase        : {result['current_phase']}")
    print(f"Next Phase           : {result['next_phase']}")
    print(f"Target Final Phase   : {result['target_final_phase']}")
    print(f"Real Training Done   : {result['real_training_executed']}")
    print(f"Predictions Done     : {result['predictions_executed']}")
    print(f"Targets Generated    : {result['targets_generated']}")
    print(f"Artifacts Persisted  : {result['artifacts_persisted']}")
    print(f"Registry Writes Done : {result['registry_writes_executed']}")
    print(f"Handoff Ready        : {result['phase_139_handoff_ready']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
