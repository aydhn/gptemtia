"""Phase 138: Run Dry-Run Training Harness Contracts Script.

Builds and persists harness contracts, trainer stubs, policies, and placeholder registries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_baseline_ml_models.baseline_ml_model_config import (
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.dry_run_training_harness_contracts import (
    build_dry_run_training_harness_contract_registry,
)
from advanced_baseline_ml_models.dry_run_trainer_stubs import (
    build_dry_run_trainer_stub_registry,
)
from advanced_baseline_ml_models.dry_run_training_policies import (
    build_dry_run_training_policy_registry,
)
from advanced_baseline_ml_models.baseline_metric_placeholders import (
    build_baseline_metric_placeholder_registry,
)
from advanced_baseline_ml_models.baseline_evaluation_placeholders import (
    build_baseline_evaluation_placeholder_registry,
)
from reports.report_builder import ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_baseline_ml_model_profile()

    df_hc, s_hc = build_dry_run_training_harness_contract_registry(profile)
    data_lake.save_dry_run_training_harness_contract_registry(df_hc, s_hc)

    df_stubs, s_stubs = build_dry_run_trainer_stub_registry(profile)
    data_lake.save_dry_run_trainer_stub_registry(df_stubs, s_stubs)

    df_pol, s_pol = build_dry_run_training_policy_registry(profile)
    data_lake.save_dry_run_training_policy_registry(df_pol, s_pol)

    df_mp, s_mp = build_baseline_metric_placeholder_registry(profile)
    data_lake.save_baseline_metric_placeholder_registry(df_mp, s_mp)

    df_ep, s_ep = build_baseline_evaluation_placeholder_registry(profile)
    data_lake.save_baseline_evaluation_placeholder_registry(df_ep, s_ep)

    print("=" * 70)
    print("PHASE 138: DRY-RUN TRAINING HARNESS CONTRACTS")
    print("=" * 70)
    print(ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Harness Contracts  : {s_hc['total_harness_contracts']}")
    print(f"Trainer Stubs      : {s_stubs['total_trainer_stubs']}")
    print(f"Training Policies  : {s_pol['total_policies']}")
    print(f"Metric Placeholders: {s_mp['total_placeholders']}")
    print(f"Eval Placeholders  : {s_ep['total_evaluation_placeholders']}")
    print(f"Execution Blocked  : {s_hc.get('all_real_training_blocked', True)}")
    print("=" * 70)



if __name__ == "__main__":
    main()
