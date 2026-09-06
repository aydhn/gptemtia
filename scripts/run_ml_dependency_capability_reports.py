"""Phase 136: Run ML Dependency Capability Reports Script.

Inspects PyTorch, scikit-learn, NumPy, Pandas, and optional ML libraries without fitting models or running inference.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_gpu_ml_runtime.gpu_ml_runtime_config import get_default_gpu_ml_runtime_profile
from advanced_gpu_ml_runtime.torch_runtime_capability import build_torch_runtime_capability_report
from advanced_gpu_ml_runtime.sklearn_runtime_capability import build_sklearn_runtime_capability_report
from advanced_gpu_ml_runtime.numpy_pandas_runtime_capability import build_numpy_pandas_runtime_capability_report
from advanced_gpu_ml_runtime.optional_ml_dependency_registry import build_optional_ml_dependency_registry
from reports.report_builder import GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_gpu_ml_runtime_profile()

    df_torch, s_torch = build_torch_runtime_capability_report(profile)
    data_lake.save_torch_runtime_capability_report(df_torch, s_torch)

    df_sklearn, s_sklearn = build_sklearn_runtime_capability_report(profile)
    data_lake.save_sklearn_runtime_capability_report(df_sklearn, s_sklearn)

    df_np_pd, s_np_pd = build_numpy_pandas_runtime_capability_report(profile)
    data_lake.save_numpy_pandas_runtime_capability_report(df_np_pd, s_np_pd)

    df_opt, s_opt = build_optional_ml_dependency_registry(profile)
    data_lake.save_optional_ml_dependency_registry(df_opt, s_opt)

    print("=" * 70)
    print("PHASE 136: ML RUNTIME DEPENDENCY CAPABILITY REPORTS")
    print("=" * 70)
    print(GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"PyTorch Available   : {s_torch.get('torch_available', False)}")
    print(f"Scikit-Learn Avail. : {s_sklearn.get('sklearn_available', False)}")
    print(f"NumPy / Pandas Avail: {s_np_pd.get('all_ready', False)}")
    print(f"Optional ML Checked : {s_opt.get('total_optional_libraries', 0)}")
    print(f"No Models Fit       : True")
    print(f"Non-Signal          : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
