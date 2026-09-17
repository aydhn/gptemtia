# -*- coding: utf-8 -*-
"""Phase 140: Run Ensemble Disabled Execution Reports Script."""

import sys
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_ensemble_model_registry.ensemble_execution_disabled import (
    build_ensemble_execution_disabled_report,
    summarize_ensemble_execution_disabled_report,
)
from advanced_ensemble_model_registry.candidate_model_training_disabled import (
    build_candidate_model_training_disabled_report,
    summarize_candidate_model_training_disabled_report,
)
from advanced_ensemble_model_registry.candidate_model_prediction_disabled import (
    build_candidate_model_prediction_disabled_report,
    summarize_candidate_model_prediction_disabled_report,
)
from advanced_ensemble_model_registry.candidate_model_target_label_disabled import (
    build_candidate_model_target_label_disabled_report,
    summarize_candidate_model_target_label_disabled_report,
)
from advanced_ensemble_model_registry.candidate_model_artifact_disabled import (
    build_candidate_model_artifact_disabled_report,
    summarize_candidate_model_artifact_disabled_report,
)
from advanced_ensemble_model_registry.candidate_model_registry_write_disabled import (
    build_candidate_model_registry_write_disabled_report,
    summarize_candidate_model_registry_write_disabled_report,
)
from reports.report_builder import ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()

    r_ens = build_ensemble_execution_disabled_report()
    s_ens = summarize_ensemble_execution_disabled_report(r_ens)
    df_ens = pd.DataFrame([r_ens])
    data_lake.save_ensemble_disabled_execution_report_registry(df_ens, s_ens)

    r_trn = build_candidate_model_training_disabled_report()
    s_trn = summarize_candidate_model_training_disabled_report(r_trn)
    df_trn = pd.DataFrame([r_trn])
    data_lake.save_candidate_model_training_disabled_report(df_trn, s_trn)

    r_prd = build_candidate_model_prediction_disabled_report()
    s_prd = summarize_candidate_model_prediction_disabled_report(r_prd)
    df_prd = pd.DataFrame([r_prd])
    data_lake.save_candidate_model_prediction_disabled_report(df_prd, s_prd)

    r_tgt = build_candidate_model_target_label_disabled_report()
    s_tgt = summarize_candidate_model_target_label_disabled_report(r_tgt)
    df_tgt = pd.DataFrame([r_tgt])
    data_lake.save_candidate_model_target_label_disabled_report(df_tgt, s_tgt)

    r_art = build_candidate_model_artifact_disabled_report()
    s_art = summarize_candidate_model_artifact_disabled_report(r_art)
    df_art = pd.DataFrame([r_art])
    data_lake.save_candidate_model_artifact_disabled_report(df_art, s_art)

    r_reg = build_candidate_model_registry_write_disabled_report()
    s_reg = summarize_candidate_model_registry_write_disabled_report(r_reg)
    df_reg = pd.DataFrame([r_reg])
    data_lake.save_candidate_model_registry_write_disabled_report(df_reg, s_reg)

    print("=" * 70)
    print("PHASE 140: ENSEMBLE DISABLED EXECUTION REPORTS")
    print("=" * 70)
    print(ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Ensemble Execution Disabled : {s_ens['all_executions_disabled']}")
    print(f"Candidate Training Disabled : {s_trn['training_disabled']}")
    print(f"Candidate Prediction Disabled: {s_prd['prediction_disabled']}")
    print(f"Target Label Gen Disabled   : {s_tgt['target_label_generation_disabled']}")
    print(f"Artifact Persist Disabled   : {s_art['artifact_persistence_disabled']}")
    print(f"Registry Write Disabled     : {s_reg['registry_write_disabled']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
