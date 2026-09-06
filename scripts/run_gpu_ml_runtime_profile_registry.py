"""Phase 136: Run GPU ML Runtime Profile Registry Script.

Discovers and registers Phase 136 runtime profiles and domain definitions.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_gpu_ml_runtime.gpu_ml_runtime_config import get_default_gpu_ml_runtime_profile
from advanced_gpu_ml_runtime.gpu_ml_runtime_profile_registry import build_gpu_ml_runtime_profile_registry
from advanced_gpu_ml_runtime.gpu_ml_runtime_domain_registry import build_gpu_ml_runtime_domain_registry
from reports.report_builder import GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_gpu_ml_runtime_profile()

    df_profiles, s_profiles = build_gpu_ml_runtime_profile_registry()
    data_lake.save_gpu_ml_runtime_profile_registry(df_profiles, s_profiles)

    df_domains, s_domains = build_gpu_ml_runtime_domain_registry()
    data_lake.save_gpu_ml_runtime_domain_registry(df_domains, s_domains)

    print("=" * 70)
    print("PHASE 136: GPU & ML RUNTIME PROFILE AND DOMAIN REGISTRY")
    print("=" * 70)
    print(GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Active Profile  : {profile.profile_name}")
    print(f"Total Profiles  : {s_profiles['total_profiles']}")
    print(f"Total Domains   : {s_domains['total_domains']}")
    print(f"Current Phase   : {profile.current_phase}")
    print(f"Next Phase      : {profile.next_phase}")
    print(f"Non-Signal      : {s_profiles['non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
