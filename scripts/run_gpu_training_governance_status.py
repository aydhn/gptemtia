# -*- coding: utf-8 -*-
"""Phase 139: Run GPU Training Governance Status Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_gpu_training_governance.gpu_training_governance_pipeline import (
    GpuTrainingGovernancePipeline,
)
from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from reports.report_builder import ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_gpu_training_governance_profile()
    project_root = Path(__file__).resolve().parent.parent

    pipeline = GpuTrainingGovernancePipeline(
        data_lake=data_lake,
        project_root=project_root,
        profile=profile,
    )

    df_status, s_status = pipeline.build_gpu_training_governance_status(save=True)

    print("=" * 70)
    print("PHASE 139: GPU TRAINING GOVERNANCE CONSOLIDATED STATUS")
    print("=" * 70)
    print(ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Active Profile          : {s_status['active_profile']}")
    print(f"Current Phase           : {s_status['current_phase']}")
    print(f"Next Phase              : {s_status['next_phase']}")
    print(f"Target Final Phase      : {s_status['target_final_phase']}")
    print(f"Total Components Ready  : {s_status['total_components']}")
    print(f"Real Training Executed  : {s_status['real_training_executed']}")
    print(f"Model Fit Executed      : {s_status['model_fit_executed']}")
    print(f"Model Predict Executed  : {s_status['model_predict_executed']}")
    print(f"Artifact Persisted      : {s_status['artifact_persisted']}")
    print(f"Registry Written        : {s_status['model_registry_written']}")
    print(f"Non-Signal Certified    : {s_status['non_signal']}")
    print("-" * 70)
    print("Component Summary:")
    for _, r in df_status.iterrows():
        print(f"  - {r['component']:<30}: {r['status']} ({r['count']})")
    print("=" * 70)


if __name__ == "__main__":
    main()
