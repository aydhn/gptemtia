# -*- coding: utf-8 -*-
"""Phase 139: Run GPU Training Resource Policies Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_training_resource_policies import (
    build_gpu_training_resource_policy_registry,
)
from advanced_gpu_training_governance.gpu_device_selection_policies import (
    build_gpu_device_selection_policy_registry,
)
from advanced_gpu_training_governance.gpu_memory_budget_policies import (
    build_gpu_memory_budget_policy_registry,
)
from advanced_gpu_training_governance.cpu_fallback_policies import (
    build_cpu_fallback_policy_registry,
)
from advanced_gpu_training_governance.training_timeout_policies import (
    build_training_timeout_policy_registry,
)
from advanced_gpu_training_governance.batch_size_placeholder_policies import (
    build_batch_size_placeholder_policy_registry,
)
from advanced_gpu_training_governance.dataloader_placeholder_policies import (
    build_dataloader_placeholder_policy_registry,
)
from reports.report_builder import ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_gpu_training_governance_profile()

    df_res, s_res = build_gpu_training_resource_policy_registry(profile)
    data_lake.save_gpu_training_resource_policy_registry(df_res, s_res)

    df_dev, s_dev = build_gpu_device_selection_policy_registry(profile)
    data_lake.save_gpu_device_selection_policy_registry(df_dev, s_dev)

    df_mem, s_mem = build_gpu_memory_budget_policy_registry(profile)
    data_lake.save_gpu_memory_budget_policy_registry(df_mem, s_mem)

    df_cpu, s_cpu = build_cpu_fallback_policy_registry(profile)
    data_lake.save_cpu_fallback_policy_registry(df_cpu, s_cpu)

    df_tmo, s_tmo = build_training_timeout_policy_registry(profile)
    data_lake.save_training_timeout_policy_registry(df_tmo, s_tmo)

    df_bat, s_bat = build_batch_size_placeholder_policy_registry(profile)
    data_lake.save_batch_size_placeholder_policy_registry(df_bat, s_bat)

    df_dl, s_dl = build_dataloader_placeholder_policy_registry(profile)
    data_lake.save_dataloader_placeholder_policy_registry(df_dl, s_dl)

    print("=" * 70)
    print("PHASE 139: GPU TRAINING RESOURCE POLICIES & PLACEHOLDERS")
    print("=" * 70)
    print(ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Resource Policies   : {s_res['total_policies']}")
    print(f"Device Selection    : {s_dev['total_policies']}")
    print(f"Memory Budget       : {s_mem['total_policies']}")
    print(f"CPU Fallback        : {s_cpu['total_policies']}")
    print(f"Timeout Policies    : {s_tmo['total_policies']}")
    print(f"Batch Placeholders  : {s_bat['total_policies']}")
    print(f"Dataloader Plhdrs   : {s_dl['total_policies']}")
    print(f"Contract Only Mode  : {s_res['all_contract_only']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
