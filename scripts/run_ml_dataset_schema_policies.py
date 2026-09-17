"""Phase 137: Run ML Dataset Schema and Policy Registries Script.

Builds and persists schema, namespace, version, partition, time-index, and split policies.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_ml_dataset_registry.advanced_ml_dataset_config import (
    get_default_advanced_ml_dataset_profile,
)
from advanced_ml_dataset_registry.ml_dataset_schema import (
    build_ml_dataset_schema_registry,
)
from advanced_ml_dataset_registry.ml_dataset_feature_namespace import (
    build_ml_dataset_feature_namespace_registry,
)
from advanced_ml_dataset_registry.ml_dataset_version_policies import (
    build_ml_dataset_version_policy_registry,
)
from advanced_ml_dataset_registry.ml_dataset_partition_policies import (
    build_ml_dataset_partition_policy_registry,
)
from advanced_ml_dataset_registry.ml_dataset_time_index_policies import (
    build_ml_dataset_time_index_policy_registry,
)
from advanced_ml_dataset_registry.ml_dataset_time_series_split_policies import (
    build_ml_dataset_time_series_split_policy_registry,
)
from advanced_ml_dataset_registry.ml_dataset_walk_forward_split_policies import (
    build_ml_dataset_walk_forward_split_policy_registry,
)
from advanced_ml_dataset_registry.ml_dataset_purged_split_placeholders import (
    build_ml_dataset_purged_split_placeholder_registry,
)
from reports.report_builder import ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_advanced_ml_dataset_profile()

    df_schema, s_schema = build_ml_dataset_schema_registry(profile)
    data_lake.save_ml_dataset_schema_registry(df_schema, s_schema)

    df_ns, s_ns = build_ml_dataset_feature_namespace_registry(profile)
    data_lake.save_ml_dataset_feature_namespace_registry(df_ns, s_ns)

    df_vp, s_vp = build_ml_dataset_version_policy_registry(profile)
    data_lake.save_ml_dataset_version_policy_registry(df_vp, s_vp)

    df_pp, s_pp = build_ml_dataset_partition_policy_registry(profile)
    data_lake.save_ml_dataset_partition_policy_registry(df_pp, s_pp)

    df_ti, s_ti = build_ml_dataset_time_index_policy_registry(profile)
    data_lake.save_ml_dataset_time_index_policy_registry(df_ti, s_ti)

    df_ts, s_ts = build_ml_dataset_time_series_split_policy_registry(profile)
    data_lake.save_ml_dataset_time_series_split_policy_registry(df_ts, s_ts)

    df_wf, s_wf = build_ml_dataset_walk_forward_split_policy_registry(profile)
    data_lake.save_ml_dataset_walk_forward_split_policy_registry(df_wf, s_wf)

    df_ps, s_ps = build_ml_dataset_purged_split_placeholder_registry(profile)
    data_lake.save_ml_dataset_purged_split_placeholder_registry(df_ps, s_ps)

    print("=" * 70)
    print("PHASE 137: ML DATASET SCHEMAS & POLICIES")
    print("=" * 70)
    print(ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Schemas       : {s_schema['total_schemas']}")
    print(f"Namespaces Defined  : {s_ns['total_namespaces']}")
    print(f"Time-Series Splits  : {s_ts['total_split_policies']}")
    print(f"Purged Placeholders : {s_ps['total_purged_split_placeholders']}")
    print(f"Split Execution     : Blocked (placeholder-only)")
    print(f"Non-Signal          : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
