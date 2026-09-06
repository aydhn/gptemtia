"""Phase 136: Run Local Hardware Discovery Script.

Safely discovers local CPU, memory, GPU, CUDA, and environment capabilities without running models.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_gpu_ml_runtime.gpu_ml_runtime_config import get_default_gpu_ml_runtime_profile
from advanced_gpu_ml_runtime.local_hardware_discovery import build_local_hardware_discovery_report
from advanced_gpu_ml_runtime.gpu_capability_registry import build_gpu_capability_registry
from advanced_gpu_ml_runtime.cpu_capability_registry import build_cpu_capability_registry
from advanced_gpu_ml_runtime.memory_capability_registry import build_memory_capability_registry
from advanced_gpu_ml_runtime.cuda_availability import build_cuda_availability_report
from advanced_gpu_ml_runtime.accelerator_backend_registry import build_accelerator_backend_registry
from advanced_gpu_ml_runtime.ml_runtime_environment_snapshot import build_ml_runtime_environment_snapshot
from reports.report_builder import GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_gpu_ml_runtime_profile()

    df_hw, s_hw = build_local_hardware_discovery_report(profile)
    data_lake.save_local_hardware_discovery_report(df_hw, s_hw)

    df_gpu, s_gpu = build_gpu_capability_registry(profile)
    data_lake.save_gpu_capability_registry(df_gpu, s_gpu)

    df_cpu, s_cpu = build_cpu_capability_registry(profile)
    data_lake.save_cpu_capability_registry(df_cpu, s_cpu)

    df_mem, s_mem = build_memory_capability_registry(profile)
    data_lake.save_memory_capability_registry(df_mem, s_mem)

    df_cuda, s_cuda = build_cuda_availability_report(profile)
    data_lake.save_cuda_availability_report(df_cuda, s_cuda)

    df_acc, s_acc = build_accelerator_backend_registry(profile)
    data_lake.save_accelerator_backend_registry(df_acc, s_acc)

    df_env, s_env = build_ml_runtime_environment_snapshot(profile)
    data_lake.save_ml_runtime_environment_snapshot(df_env, s_env)

    print("=" * 70)
    print("PHASE 136: LOCAL HARDWARE & ACCELERATOR DISCOVERY")
    print("=" * 70)
    print(GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Hardware Items  : {s_hw['total_items']}")
    print(f"CPU Physical    : {s_cpu.get('physical_cores', 0)} cores ({s_cpu.get('logical_cores', 0)} logical)")
    print(f"RAM Total GB    : {s_mem.get('total_ram_gb', 0.0):.2f} GB (Available: {s_mem.get('available_ram_gb', 0.0):.2f} GB)")
    print(f"GPU Available   : {s_gpu.get('gpu_available', False)} (Backend: {s_gpu.get('active_backend', 'cpu')})")
    print(f"CUDA Available  : {s_cuda.get('cuda_available', False)}")
    print(f"Active Backend  : {s_acc.get('active_backend', 'cpu')}")
    print(f"Non-Signal      : {s_hw['non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
