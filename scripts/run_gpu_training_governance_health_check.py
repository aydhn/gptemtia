# -*- coding: utf-8 -*-
"""Phase 139: Run GPU Training Governance Health Check Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_training_governance_health import (
    build_gpu_training_governance_health_check,
)
from reports.report_builder import ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_gpu_training_governance_profile()
    project_root = Path(__file__).resolve().parent.parent

    df_hl, s_hl = build_gpu_training_governance_health_check(project_root, profile)
    data_lake.save_gpu_training_governance_health_check(df_hl, s_hl)

    print("=" * 70)
    print("PHASE 139: GPU TRAINING GOVERNANCE HEALTH CHECK")
    print("=" * 70)
    print(ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Checks    : {s_hl['total_checks']}")
    print(f"Healthy Count   : {s_hl['healthy_count']}")
    print(f"Health Status   : {s_hl['health_status']}")
    print(f"All Healthy     : {s_hl['all_healthy']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
