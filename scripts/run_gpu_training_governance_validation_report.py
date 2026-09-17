# -*- coding: utf-8 -*-
"""Phase 139: Run GPU Training Governance Validation and Safety Report Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_training_governance_validation import (
    build_gpu_training_governance_validation_report,
)
from advanced_gpu_training_governance.gpu_training_governance_safety_boundary import (
    build_gpu_training_governance_safety_boundary,
)
from advanced_gpu_training_governance.gpu_training_governance_profile_registry import (
    build_gpu_training_governance_profile_registry,
)
from advanced_gpu_training_governance.gpu_training_resource_policies import (
    build_gpu_training_resource_policy_registry,
)
from advanced_gpu_training_governance.training_loop_stub_contracts import (
    build_training_loop_stub_contract_registry,
)
from advanced_gpu_training_governance.gpu_training_governance_manifest import (
    build_gpu_training_governance_manifest,
)
from reports.report_builder import ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_gpu_training_governance_profile()

    df_prof, _ = build_gpu_training_governance_profile_registry(profile)
    df_res, _ = build_gpu_training_resource_policy_registry(profile)
    df_harn, _ = build_training_loop_stub_contract_registry(profile)
    df_mf, _ = build_gpu_training_governance_manifest(profile)

    tables = {
        "profiles": df_prof,
        "resource_policies": df_res,
        "harness_contracts": df_harn,
        "manifest": df_mf,
    }

    df_val, s_val = build_gpu_training_governance_validation_report(tables, profile)
    data_lake.save_gpu_training_governance_validation_report(df_val, s_val)

    df_sb, s_sb = build_gpu_training_governance_safety_boundary(profile)
    data_lake.save_gpu_training_governance_safety_boundary(df_sb, s_sb)

    print("=" * 70)
    print("PHASE 139: GPU TRAINING GOVERNANCE VALIDATION & SAFETY REPORT")
    print("=" * 70)
    print(ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Validation Status   : {s_val['validation_status']}")
    print(f"Checks Passed       : {s_val['passed_checks']}/{s_val['total_checks']}")
    print(f"Safety Status       : {s_sb['safety_status']}")
    print(f"NO-GO Rules Enforced: {s_sb['no_go_count']}")
    print(f"SAFE-GO Principles  : {s_sb['safe_go_count']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
