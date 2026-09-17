# -*- coding: utf-8 -*-
"""Phase 139: Run GPU Training Disabled Execution Reports Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.no_real_training_execution import (
    build_no_real_training_execution_report,
)
from advanced_gpu_training_governance.no_prediction_execution import (
    build_no_prediction_execution_report,
)
from advanced_gpu_training_governance.no_target_label_generation import (
    build_no_target_label_generation_report,
)
from advanced_gpu_training_governance.no_model_artifact_persistence import (
    build_no_model_artifact_persistence_report,
)
from advanced_gpu_training_governance.no_model_registry_write import (
    build_no_model_registry_write_report,
)
from reports.report_builder import ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_gpu_training_governance_profile()

    df_trn, s_trn = build_no_real_training_execution_report(profile)
    data_lake.save_gpu_training_no_real_training_execution_report(df_trn, s_trn)

    df_prd, s_prd = build_no_prediction_execution_report(profile)
    data_lake.save_gpu_training_no_prediction_execution_report(df_prd, s_prd)

    df_tgt, s_tgt = build_no_target_label_generation_report(profile)
    data_lake.save_gpu_training_no_target_label_generation_report(df_tgt, s_tgt)

    df_art, s_art = build_no_model_artifact_persistence_report(profile)
    data_lake.save_no_model_artifact_persistence_report(df_art, s_art)

    df_reg, s_reg = build_no_model_registry_write_report(profile)
    data_lake.save_no_model_registry_write_report(df_reg, s_reg)

    print("=" * 70)
    print("PHASE 139: GPU TRAINING DISABLED EXECUTION VERIFICATION")
    print("=" * 70)
    print(ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Real Training Disabled  : {s_trn['all_disabled']}")
    print(f"Prediction Disabled     : {s_prd['all_disabled']}")
    print(f"Target/Label Disabled   : {s_tgt['all_disabled']}")
    print(f"Artifact Write Disabled : {s_art['all_disabled']}")
    print(f"Registry Write Disabled : {s_reg['all_disabled']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
