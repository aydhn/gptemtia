# -*- coding: utf-8 -*-
"""Phase 140: Run Ensemble Model Profile & Domain Registry Script."""

import sys
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_ensemble_model_registry.ensemble_model_profile_registry import (
    build_ensemble_model_profile_registry,
    summarize_ensemble_model_profiles,
)
from advanced_ensemble_model_registry.ensemble_model_domain_registry import (
    build_ensemble_model_domain_registry,
    summarize_ensemble_model_domains,
)
from reports.report_builder import ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()

    df_prof, s_prof = build_ensemble_model_profile_registry()
    data_lake.save_ensemble_model_profile_registry(df_prof, s_prof)

    df_dom, s_dom = build_ensemble_model_domain_registry()
    data_lake.save_ensemble_model_domain_registry(df_dom, s_dom)

    print("=" * 70)
    print("PHASE 140: ENSEMBLE MODEL PROFILE & DOMAIN REGISTRY")
    print("=" * 70)
    print(ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Profiles   : {s_prof['total_profiles']}")
    print(f"Active Profiles  : {', '.join(s_prof['profiles'])}")
    print(f"Total Domains    : {s_dom['total_domains']}")
    print(f"All Local Only   : {s_prof['all_local_only']}")
    print(f"All Non-Signal   : {s_prof['all_non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
