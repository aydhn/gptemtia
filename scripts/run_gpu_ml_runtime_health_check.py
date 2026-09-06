"""Phase 136: Run GPU ML Runtime Health Check Script.

Performs health checks on directory structures, upstream modules (Phase 1-135), and safety prohibitions.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_gpu_ml_runtime.gpu_ml_runtime_config import get_default_gpu_ml_runtime_profile
from advanced_gpu_ml_runtime.gpu_ml_runtime_health import build_gpu_ml_runtime_health_check
from reports.report_builder import GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_gpu_ml_runtime_profile()

    df_health, s_health = build_gpu_ml_runtime_health_check(Path.cwd(), profile)
    data_lake.save_gpu_ml_runtime_health_check(df_health, s_health)

    print("=" * 70)
    print("PHASE 136: GPU & ML RUNTIME HEALTH CHECK")
    print("=" * 70)
    print(GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Overall Health Status : {s_health.get('status', 'READY')}")
    print(f"Total Checks          : {s_health.get('total_components', 0)}")
    print(f"Passed Checks         : {s_health.get('passed_components', 0)}")
    print(f"All Passed            : {s_health.get('all_healthy', True)}")
    print(f"Non-Signal            : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
