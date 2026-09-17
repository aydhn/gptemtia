# -*- coding: utf-8 -*-
"""Phase 141: Run Calibration and Uncertainty Profile & Domain Registry Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_calibration_uncertainty.calibration_uncertainty_profile_registry import (
    build_calibration_uncertainty_profile_registry,
    summarize_calibration_uncertainty_profiles,
)
from advanced_calibration_uncertainty.calibration_uncertainty_domain_registry import (
    build_calibration_uncertainty_domain_registry,
    summarize_calibration_uncertainty_domains,
)
from reports.report_builder import ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()

    df_prof, s_prof = build_calibration_uncertainty_profile_registry()
    data_lake.save_calibration_uncertainty_profile_registry(df_prof, s_prof)

    df_dom, s_dom = build_calibration_uncertainty_domain_registry()
    data_lake.save_calibration_uncertainty_domain_registry(df_dom, s_dom)

    print("=" * 70)
    print("PHASE 141: CALIBRATION & UNCERTAINTY PROFILE / DOMAIN REGISTRIES")
    print("=" * 70)
    print(ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Profiles Registered : {s_prof.get('total_profiles', 0)}")
    print(f"Total Domains Registered  : {s_dom.get('total_domains', 0)}")
    print(f"Non-Executing Status      : {s_prof.get('all_non_executing', True)}")
    print(f"Zero Prediction Enforced  : {s_prof.get('all_zero_prediction', True)}")
    print("=" * 70)


if __name__ == "__main__":
    main()
