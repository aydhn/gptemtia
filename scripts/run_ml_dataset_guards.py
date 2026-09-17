"""Phase 137: Run ML Dataset Guards and Prohibition Policies Script.

Builds and persists leakage, no-lookahead, news, source preservation, and forbidden column guards.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_ml_dataset_registry.advanced_ml_dataset_config import (
    get_default_advanced_ml_dataset_profile,
)
from advanced_ml_dataset_registry.ml_dataset_leakage_guards import (
    build_ml_dataset_leakage_guard_registry,
)
from advanced_ml_dataset_registry.ml_dataset_no_lookahead_guards import (
    build_ml_dataset_no_lookahead_guard_registry,
)
from advanced_ml_dataset_registry.ml_dataset_metadata_only_news_guards import (
    build_ml_dataset_metadata_only_news_guard_registry,
)
from advanced_ml_dataset_registry.ml_dataset_source_preservation_guards import (
    build_ml_dataset_source_preservation_guard_registry,
)
from advanced_ml_dataset_registry.ml_dataset_forbidden_column_policies import (
    build_ml_dataset_forbidden_column_policy_registry,
)
from advanced_ml_dataset_registry.ml_dataset_target_label_disabled_policies import (
    build_ml_dataset_target_label_disabled_policy_registry,
)
from reports.report_builder import ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_advanced_ml_dataset_profile()

    df_lg, s_lg = build_ml_dataset_leakage_guard_registry(profile)
    data_lake.save_ml_dataset_leakage_guard_registry(df_lg, s_lg)

    df_nl, s_nl = build_ml_dataset_no_lookahead_guard_registry(profile)
    data_lake.save_ml_dataset_no_lookahead_guard_registry(df_nl, s_nl)

    df_mn, s_mn = build_ml_dataset_metadata_only_news_guard_registry(profile)
    data_lake.save_ml_dataset_metadata_only_news_guard_registry(df_mn, s_mn)

    df_sp, s_sp = build_ml_dataset_source_preservation_guard_registry(profile)
    data_lake.save_ml_dataset_source_preservation_guard_registry(df_sp, s_sp)

    df_fc, s_fc = build_ml_dataset_forbidden_column_policy_registry(profile)
    data_lake.save_ml_dataset_forbidden_column_policy_registry(df_fc, s_fc)

    df_tl, s_tl = build_ml_dataset_target_label_disabled_policy_registry(profile)
    data_lake.save_ml_dataset_target_label_disabled_policy_registry(df_tl, s_tl)

    print("=" * 70)
    print("PHASE 137: ML DATASET SAFETY GUARDS & POLICIES")
    print("=" * 70)
    print(ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Leakage Guards        : {s_lg.get('total_leakage_guards', len(df_lg))}")
    print(f"No-Lookahead Guards   : {s_nl.get('total_no_lookahead_guards', len(df_nl))}")
    print(f"News Metadata Guards  : {s_mn.get('total_news_guards', len(df_mn))}")
    print(f"Source Preservation   : {s_sp.get('total_sp_guards', len(df_sp))}")
    print(f"Forbidden Columns     : {s_fc.get('total_forbidden_columns', len(df_fc))}")
    print(f"Target/Label Disabled : Enforced")
    print(f"Non-Signal            : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
