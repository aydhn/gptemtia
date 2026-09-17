"""Phase 138: Run Baseline Model Findings and Manifest Script.

Builds and persists findings, manual review queue, readiness score, manifest, and Phase 139 handoff.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_baseline_ml_models.baseline_ml_model_config import (
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.baseline_model_findings import (
    build_baseline_model_findings_registry,
)
from advanced_baseline_ml_models.baseline_model_manual_review import (
    build_baseline_model_manual_review_queue,
)
from advanced_baseline_ml_models.baseline_model_readiness_scoring import (
    build_baseline_model_readiness_score_report,
)
from advanced_baseline_ml_models.baseline_ml_model_manifest import (
    build_baseline_ml_model_manifest,
)
from advanced_baseline_ml_models.phase_139_handoff import (
    build_phase_139_gpu_training_harness_resource_governance_handoff_report,
)
from reports.report_builder import ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_baseline_ml_model_profile()

    df_find, s_find = build_baseline_model_findings_registry(profile)
    data_lake.save_baseline_model_findings_registry(df_find, s_find)

    df_mr, s_mr = build_baseline_model_manual_review_queue(profile)
    data_lake.save_baseline_model_manual_review_queue(df_mr, s_mr)

    df_rs, s_rs = build_baseline_model_readiness_score_report(profile)
    data_lake.save_baseline_model_readiness_score_report(df_rs, s_rs)

    df_man, s_man = build_baseline_ml_model_manifest(profile)
    data_lake.save_baseline_ml_model_manifest(df_man, s_man)

    df_ho, s_ho = build_phase_139_gpu_training_harness_resource_governance_handoff_report(profile)
    data_lake.save_phase_139_gpu_training_harness_resource_governance_handoff_report(df_ho, s_ho)

    print("=" * 70)
    print("PHASE 138: BASELINE MODEL FINDINGS & MANIFEST")
    print("=" * 70)
    print(ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Findings       : {s_find['total_findings']}")
    print(f"Manual Reviews       : {s_mr.get('total_review_items', 0)}")
    print(f"Readiness Score      : {s_rs['readiness_score']:.4f}")
    print(f"Classification       : {s_rs.get('score_tier', 'READY_FOR_LOCAL_DRY_RUN_HARNESS')}")
    print(f"Manifest Status      : {s_man['status']}")

    print(f"Handoff Ready        : {s_ho['all_satisfied']}")
    print(f"Zero Real Training   : {s_man['real_training_executed'] == False}")
    print("=" * 70)


if __name__ == "__main__":
    main()
