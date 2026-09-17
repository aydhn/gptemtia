"""Phase 137: Run ML Experiment Registry and Governance Script.

Builds and persists feature snapshot contracts, quality gates, lineage,
experiment registry, templates, permissions, placeholders, and disabled contracts.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_ml_dataset_registry.advanced_ml_dataset_config import (
    get_default_advanced_ml_dataset_profile,
)
from advanced_ml_dataset_registry.ml_dataset_feature_snapshot_contracts import (
    build_ml_dataset_feature_snapshot_contract_registry,
)
from advanced_ml_dataset_registry.ml_dataset_feature_snapshot_manifest_placeholders import (
    build_feature_snapshot_manifest_placeholder_registry,
)
from advanced_ml_dataset_registry.ml_dataset_quality_gates import (
    build_ml_dataset_quality_gate_registry,
)
from advanced_ml_dataset_registry.ml_dataset_validation_dependencies import (
    build_ml_dataset_validation_dependency_registry,
)
from advanced_ml_dataset_registry.ml_dataset_quality_dependencies import (
    build_ml_dataset_quality_dependency_registry,
)
from advanced_ml_dataset_registry.ml_dataset_lineage import (
    build_ml_dataset_lineage_registry,
)
from advanced_ml_dataset_registry.ml_experiment_registry import (
    build_ml_experiment_registry,
)
from advanced_ml_dataset_registry.ml_experiment_templates import (
    build_ml_experiment_template_registry,
)
from advanced_ml_dataset_registry.ml_experiment_permissions import (
    build_ml_experiment_permission_registry,
)
from advanced_ml_dataset_registry.ml_experiment_run_plan_placeholders import (
    build_ml_experiment_run_plan_placeholder_registry,
)
from advanced_ml_dataset_registry.ml_model_family_placeholders import (
    build_ml_model_family_placeholder_registry,
)
from advanced_ml_dataset_registry.ml_metric_placeholders import (
    build_ml_metric_placeholder_registry,
)
from advanced_ml_dataset_registry.ml_training_harness_disabled_contracts import (
    build_ml_training_harness_disabled_contract_registry,
)
from advanced_ml_dataset_registry.ml_prediction_disabled_contracts import (
    build_ml_prediction_disabled_contract_registry,
)
from advanced_ml_dataset_registry.ml_artifact_disabled_contracts import (
    build_ml_artifact_disabled_contract_registry,
)
from reports.report_builder import ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_advanced_ml_dataset_profile()

    df_sc, s_sc = build_ml_dataset_feature_snapshot_contract_registry(profile)
    data_lake.save_ml_dataset_feature_snapshot_contract_registry(df_sc, s_sc)

    df_sm, s_sm = build_feature_snapshot_manifest_placeholder_registry(profile)
    data_lake.save_ml_dataset_feature_snapshot_manifest_placeholder_registry(df_sm, s_sm)

    df_qg, s_qg = build_ml_dataset_quality_gate_registry(profile)
    data_lake.save_ml_dataset_quality_gate_registry(df_qg, s_qg)

    df_vd, s_vd = build_ml_dataset_validation_dependency_registry(profile)
    data_lake.save_ml_dataset_validation_dependency_registry(df_vd, s_vd)

    df_qd, s_qd = build_ml_dataset_quality_dependency_registry(profile)
    data_lake.save_ml_dataset_quality_dependency_registry(df_qd, s_qd)

    df_lin, s_lin = build_ml_dataset_lineage_registry(profile)
    data_lake.save_ml_dataset_lineage_registry(df_lin, s_lin)

    df_er, s_er = build_ml_experiment_registry(profile)
    data_lake.save_ml_experiment_registry(df_er, s_er)

    df_et, s_et = build_ml_experiment_template_registry(profile)
    data_lake.save_ml_experiment_template_registry(df_et, s_et)

    df_ep, s_ep = build_ml_experiment_permission_registry(profile)
    data_lake.save_ml_experiment_permission_registry(df_ep, s_ep)

    df_rp, s_rp = build_ml_experiment_run_plan_placeholder_registry(profile)
    data_lake.save_ml_experiment_run_plan_placeholder_registry(df_rp, s_rp)

    df_mf, s_mf = build_ml_model_family_placeholder_registry(profile)
    data_lake.save_ml_model_family_placeholder_registry(df_mf, s_mf)

    df_mp, s_mp = build_ml_metric_placeholder_registry(profile)
    data_lake.save_ml_metric_placeholder_registry(df_mp, s_mp)

    df_th, s_th = build_ml_training_harness_disabled_contract_registry(profile)
    data_lake.save_ml_training_harness_disabled_contract_registry(df_th, s_th)

    df_pd, s_pd = build_ml_prediction_disabled_contract_registry(profile)
    data_lake.save_ml_prediction_disabled_contract_registry(df_pd, s_pd)

    df_ad, s_ad = build_ml_artifact_disabled_contract_registry(profile)
    data_lake.save_ml_artifact_disabled_contract_registry(df_ad, s_ad)

    print("=" * 70)
    print("PHASE 137: ML EXPERIMENT REGISTRY & GOVERNANCE")
    print("=" * 70)
    print(ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Snapshot Contracts    : {s_sc.get('total_snapshot_contracts', len(df_sc))} (materialized=False)")
    print(f"Quality Gates         : {s_qg.get('total_quality_gates', len(df_qg))}")
    print(f"Experiments Defined   : {s_er.get('total_experiments', len(df_er))}")
    print(f"Model Families        : {s_mf.get('total_model_families', len(df_mf))} (placeholders)")
    print(f"Metric Families       : {s_mp.get('total_metric_families', len(df_mp))} (placeholders)")
    print(f"Training Prohibited   : True")
    print(f"Inference Prohibited  : True")
    print(f"Artifacts Prohibited  : True")
    print(f"Non-Signal            : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
