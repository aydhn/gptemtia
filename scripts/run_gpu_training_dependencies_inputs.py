# -*- coding: utf-8 -*-
"""Phase 139: Run GPU Training Dependencies, Inputs, and Audit Placeholders Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_training_dataset_contract_dependencies import (
    build_gpu_training_dataset_contract_dependency_registry,
)
from advanced_gpu_training_governance.gpu_training_baseline_model_contract_dependencies import (
    build_gpu_training_baseline_model_contract_dependency_registry,
)
from advanced_gpu_training_governance.gpu_training_runtime_dependencies import (
    build_gpu_training_runtime_dependency_registry,
)
from advanced_gpu_training_governance.gpu_training_featurestore_input_dependencies import (
    build_gpu_training_featurestore_input_dependency_registry,
)
from advanced_gpu_training_governance.gpu_training_no_lookahead_guards import (
    build_gpu_training_no_lookahead_guard_registry,
)
from advanced_gpu_training_governance.gpu_training_metadata_only_news_guards import (
    build_gpu_training_metadata_only_news_guard_registry,
)
from advanced_gpu_training_governance.gpu_training_source_preservation_guards import (
    build_gpu_training_source_preservation_guard_registry,
)
from advanced_gpu_training_governance.gpu_training_forbidden_column_policies import (
    build_gpu_training_forbidden_column_policy_registry,
)
from advanced_gpu_training_governance.gpu_training_resource_audit_placeholders import (
    build_gpu_training_resource_audit_placeholder_registry,
)
from advanced_gpu_training_governance.gpu_training_experiment_audit_placeholders import (
    build_gpu_training_experiment_audit_placeholder_registry,
)
from reports.report_builder import ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_gpu_training_governance_profile()

    df_ds, s_ds = build_gpu_training_dataset_contract_dependency_registry(profile)
    data_lake.save_gpu_training_dataset_contract_dependency_registry(df_ds, s_ds)

    df_base, s_base = build_gpu_training_baseline_model_contract_dependency_registry(profile)
    data_lake.save_gpu_training_baseline_model_contract_dependency_registry(df_base, s_base)

    df_run, s_run = build_gpu_training_runtime_dependency_registry(profile)
    data_lake.save_gpu_training_runtime_dependency_registry(df_run, s_run)

    df_fs, s_fs = build_gpu_training_featurestore_input_dependency_registry(profile)
    data_lake.save_gpu_training_featurestore_input_dependency_registry(df_fs, s_fs)

    df_nla, s_nla = build_gpu_training_no_lookahead_guard_registry(profile)
    data_lake.save_gpu_training_no_lookahead_guard_registry(df_nla, s_nla)

    df_news, s_news = build_gpu_training_metadata_only_news_guard_registry(profile)
    data_lake.save_gpu_training_metadata_only_news_guard_registry(df_news, s_news)

    df_src, s_src = build_gpu_training_source_preservation_guard_registry(profile)
    data_lake.save_gpu_training_source_preservation_guard_registry(df_src, s_src)

    df_forb, s_forb = build_gpu_training_forbidden_column_policy_registry(profile)
    data_lake.save_gpu_training_forbidden_column_policy_registry(df_forb, s_forb)

    df_res_aud, s_res_aud = build_gpu_training_resource_audit_placeholder_registry(profile)
    data_lake.save_gpu_training_resource_audit_placeholder_registry(df_res_aud, s_res_aud)

    df_exp_aud, s_exp_aud = build_gpu_training_experiment_audit_placeholder_registry(profile)
    data_lake.save_gpu_training_experiment_audit_placeholder_registry(df_exp_aud, s_exp_aud)

    print("=" * 70)
    print("PHASE 139: GPU TRAINING DEPENDENCIES, GUARDS & AUDIT PLACEHOLDERS")
    print("=" * 70)
    print(ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Dataset Dependencies   : {s_ds['total_dependencies']}")
    print(f"Baseline Dependencies  : {s_base['total_dependencies']}")
    print(f"Runtime Dependencies   : {s_run['total_dependencies']}")
    print(f"FeatureStore Inputs    : {s_fs['total_dependencies']}")
    print(f"No-Lookahead Guards    : {s_nla['total_guards']}")
    print(f"News Metadata Guards   : {s_news['total_guards']}")
    print(f"Source Preservation    : {s_src['total_guards']}")
    print(f"Forbidden Columns      : {s_forb['total_forbidden_columns']}")
    print(f"Resource Audit Plhdrs  : {s_res_aud['total_placeholders']}")
    print(f"Experiment Audit Plhdrs: {s_exp_aud['total_placeholders']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
