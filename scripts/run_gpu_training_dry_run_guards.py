# -*- coding: utf-8 -*-
"""Phase 139: Run GPU Training Dry-Run Guards Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.dry_run_resource_checks import (
    build_dry_run_resource_check_report,
)
from advanced_gpu_training_governance.dry_run_device_selection import (
    build_dry_run_device_selection_report,
)
from advanced_gpu_training_governance.dry_run_memory_guards import (
    build_dry_run_memory_guard_report,
)
from advanced_gpu_training_governance.dry_run_timeout_guards import (
    build_dry_run_timeout_guard_report,
)
from advanced_gpu_training_governance.dry_run_training_execution_blocks import (
    build_dry_run_training_execution_block_report,
)
from reports.report_builder import ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_gpu_training_governance_profile()

    df_chk, s_chk = build_dry_run_resource_check_report(profile)
    data_lake.save_dry_run_resource_check_report(df_chk, s_chk)

    df_dev, s_dev = build_dry_run_device_selection_report(profile)
    data_lake.save_dry_run_device_selection_report(df_dev, s_dev)

    df_mem, s_mem = build_dry_run_memory_guard_report(profile)
    data_lake.save_dry_run_memory_guard_report(df_mem, s_mem)

    df_tmo, s_tmo = build_dry_run_timeout_guard_report(profile)
    data_lake.save_dry_run_timeout_guard_report(df_tmo, s_tmo)

    df_blk, s_blk = build_dry_run_training_execution_block_report(profile)
    data_lake.save_dry_run_training_execution_block_report(df_blk, s_blk)

    print("=" * 70)
    print("PHASE 139: GPU TRAINING DRY-RUN GUARDS & EXECUTION BLOCKS")
    print("=" * 70)
    print(ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Resource Checks     : {s_chk['total_checks']} (Passed: {s_chk['all_passed']})")
    print(f"Device Simulations  : {s_dev['total_simulations']}")
    print(f"Memory Guards       : {s_mem['total_tests']}")
    print(f"Timeout Guards      : {s_tmo['total_tests']}")
    print(f"Execution Keywords  : {s_blk['total_keywords_checked']} (All Blocked: {s_blk['all_blocked']})")
    print("=" * 70)


if __name__ == "__main__":
    main()
