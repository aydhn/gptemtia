"""Phase 138: Run Baseline Model Safety Reports Script.

Builds and persists disabled execution verification and input guard reports.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_baseline_ml_models.baseline_ml_model_config import (
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.no_real_training_execution import (
    build_no_real_training_execution_report,
)
from advanced_baseline_ml_models.no_prediction_execution import (
    build_no_prediction_execution_report,
)
from advanced_baseline_ml_models.no_target_label_generation import (
    build_no_target_label_generation_report,
)
from advanced_baseline_ml_models.model_artifact_disabled import (
    build_model_artifact_disabled_report,
)
from advanced_baseline_ml_models.model_registry_write_disabled import (
    build_model_registry_write_disabled_report,
)
from advanced_baseline_ml_models.baseline_model_no_lookahead_guards import (
    build_baseline_model_no_lookahead_input_guard_registry,
)
from advanced_baseline_ml_models.baseline_model_metadata_only_news_guards import (
    build_baseline_model_metadata_only_news_guard_registry,
)
from advanced_baseline_ml_models.baseline_model_source_preservation_guards import (
    build_baseline_model_source_preservation_guard_registry,
)
from advanced_baseline_ml_models.baseline_model_forbidden_column_policies import (
    build_baseline_model_forbidden_column_policy_registry,
)
from reports.report_builder import ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_baseline_ml_model_profile()

    df_nrt, s_nrt = build_no_real_training_execution_report(profile)
    data_lake.save_no_real_training_execution_report(df_nrt, s_nrt)

    df_np, s_np = build_no_prediction_execution_report(profile)
    data_lake.save_no_prediction_execution_report(df_np, s_np)

    df_ntlg, s_ntlg = build_no_target_label_generation_report(profile)
    data_lake.save_no_target_label_generation_report(df_ntlg, s_ntlg)

    df_mad, s_mad = build_model_artifact_disabled_report(profile)
    data_lake.save_model_artifact_disabled_report(df_mad, s_mad)

    df_mrwd, s_mrwd = build_model_registry_write_disabled_report(profile)
    data_lake.save_model_registry_write_disabled_report(df_mrwd, s_mrwd)

    df_nlg, s_nlg = build_baseline_model_no_lookahead_input_guard_registry(profile)
    data_lake.save_baseline_model_no_lookahead_input_guard_registry(df_nlg, s_nlg)

    df_mon, s_mon = build_baseline_model_metadata_only_news_guard_registry(profile)
    data_lake.save_baseline_model_metadata_only_news_guard_registry(df_mon, s_mon)

    df_spg, s_spg = build_baseline_model_source_preservation_guard_registry(profile)
    data_lake.save_baseline_model_source_preservation_guard_registry(df_spg, s_spg)

    df_fcp, s_fcp = build_baseline_model_forbidden_column_policy_registry(profile)
    data_lake.save_baseline_model_forbidden_column_policy_registry(df_fcp, s_fcp)


    print("=" * 70)
    print("PHASE 138: BASELINE MODEL SAFETY & GUARD REPORTS")
    print("=" * 70)
    print(ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"No Real Training       : {s_nrt.get('real_training_executed') == False}")
    print(f"No Prediction          : {s_np.get('model_predict_executed') == False}")
    print(f"No Target/Label        : {s_ntlg.get('target_label_generated') == False}")
    print(f"Artifact Disabled      : {s_mad.get('artifact_persisted') == False}")
    print(f"Registry Write Disabled: {s_mrwd.get('model_registry_written') == False}")
    print(f"No-Lookahead Guards    : {s_nlg['total_guards']}")
    print(f"Metadata News Guards   : {s_mon['total_guards']}")
    print(f"Source Guards          : {s_spg['total_guards']}")
    print(f"Forbidden Column Guards: {s_fcp.get('total_forbidden_columns', 0)}")
    print("=" * 70)




if __name__ == "__main__":
    main()
