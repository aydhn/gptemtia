"""Phase 136: Run ML Runtime Safety Contracts Script.

Establishes and saves ML experiment safety contracts, permission policies, disabled policies, and governance placeholders.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_gpu_ml_runtime.gpu_ml_runtime_config import get_default_gpu_ml_runtime_profile
from advanced_gpu_ml_runtime.ml_runtime_safety_contracts import build_ml_runtime_safety_contract_registry
from advanced_gpu_ml_runtime.ml_experiment_permission_policies import build_ml_experiment_permission_policy_registry
from advanced_gpu_ml_runtime.ml_training_disabled_policies import build_ml_training_disabled_policy_registry
from advanced_gpu_ml_runtime.ml_inference_disabled_policies import build_ml_inference_disabled_policy_registry
from advanced_gpu_ml_runtime.ml_target_label_disabled_policies import build_ml_target_label_disabled_policy_registry
from advanced_gpu_ml_runtime.ml_artifact_governance_placeholders import build_ml_artifact_governance_placeholder_registry
from reports.report_builder import GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_gpu_ml_runtime_profile()

    df_contracts, s_contracts = build_ml_runtime_safety_contract_registry(profile)
    data_lake.save_ml_runtime_safety_contract_registry(df_contracts, s_contracts)

    df_perm, s_perm = build_ml_experiment_permission_policy_registry(profile)
    data_lake.save_ml_experiment_permission_policy_registry(df_perm, s_perm)

    df_train, s_train = build_ml_training_disabled_policy_registry(profile)
    data_lake.save_ml_training_disabled_policy_registry(df_train, s_train)

    df_inf, s_inf = build_ml_inference_disabled_policy_registry(profile)
    data_lake.save_ml_inference_disabled_policy_registry(df_inf, s_inf)

    df_tgt, s_tgt = build_ml_target_label_disabled_policy_registry(profile)
    data_lake.save_ml_target_label_disabled_policy_registry(df_tgt, s_tgt)

    df_gov, s_gov = build_ml_artifact_governance_placeholder_registry(profile)
    data_lake.save_ml_artifact_governance_placeholder_registry(df_gov, s_gov)

    print("=" * 70)
    print("PHASE 136: ML RUNTIME SAFETY CONTRACTS AND POLICIES")
    print("=" * 70)
    print(GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Safety Contracts : {s_contracts.get('total_contracts', 0)}")
    print(f"Active Contracts       : {s_contracts.get('active_contracts', 0)}")
    print(f"Training Blocked       : True")
    print(f"Inference Blocked      : True")
    print(f"Target/Label Blocked   : True")
    print(f"Artifact Placeholders  : {s_gov.get('total_schemas', 0)}")
    print(f"Non-Signal             : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
