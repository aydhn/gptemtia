# -*- coding: utf-8 -*-
"""Phase 139: Run GPU Training Harness Contracts Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.training_loop_stub_contracts import (
    build_training_loop_stub_contract_registry,
)
from advanced_gpu_training_governance.gpu_training_harness_interfaces import (
    build_gpu_training_harness_interface_registry,
)
from advanced_gpu_training_governance.gpu_training_harness_stubs import (
    build_gpu_training_harness_stub_registry,
)
from reports.report_builder import ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_gpu_training_governance_profile()

    df_loop, s_loop = build_training_loop_stub_contract_registry(profile)
    data_lake.save_training_loop_stub_contract_registry(df_loop, s_loop)

    df_iface, s_iface = build_gpu_training_harness_interface_registry(profile)
    data_lake.save_gpu_training_harness_interface_registry(df_iface, s_iface)

    df_stub, s_stub = build_gpu_training_harness_stub_registry(profile)
    data_lake.save_gpu_training_harness_stub_registry(df_stub, s_stub)

    print("=" * 70)
    print("PHASE 139: GPU TRAINING HARNESS CONTRACTS & STUBS")
    print("=" * 70)
    print(ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Training Loop Stubs : {s_loop['total_contracts']}")
    print(f"Harness Interfaces  : {s_iface['total_interfaces']}")
    print(f"Harness Stubs       : {s_stub['total_stubs']}")
    print(f"Execution Disabled  : {s_loop['all_execution_disabled']}")
    print(f"Blocked By Policy   : {s_stub['all_blocked_by_policy']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
