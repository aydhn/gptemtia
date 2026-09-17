# -*- coding: utf-8 -*-
"""Phase 142: Run Model Drift Profile & Domain Registry Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_model_drift_monitoring.model_drift_profile_registry import (
    build_model_drift_profile_registry,
    summarize_model_drift_profiles,
)
from advanced_model_drift_monitoring.model_drift_domain_registry import (
    build_model_drift_domain_registry,
    summarize_model_drift_domains,
)
from reports.report_builder import ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()

    df_prof, s_prof = build_model_drift_profile_registry()
    data_lake.save_model_drift_profile_registry(df_prof, s_prof)

    df_dom, s_dom = build_model_drift_domain_registry()
    data_lake.save_model_drift_domain_registry(df_dom, s_dom)

    print("=" * 70)
    print("PHASE 142: MODEL DRIFT PROFILE & DOMAIN REGISTRIES")
    print("=" * 70)
    print(ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Profiles Registered : {s_prof.get('total_profiles', 0)}")
    print(f"Total Domains Registered  : {s_dom.get('total_domains', 0)}")
    print(f"Non-Executing Status      : {s_prof.get('all_non_executing', True)}")
    print(f"Zero Calculation Enforced : {s_prof.get('all_zero_calculation', True)}")
    print("=" * 70)


if __name__ == "__main__":
    main()
