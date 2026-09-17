# -*- coding: utf-8 -*-
"""Phase 140: Run Candidate Model Contracts Script."""

import sys
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_ensemble_model_registry.candidate_model_families import (
    build_candidate_model_families,
    summarize_candidate_model_families,
)
from advanced_ensemble_model_registry.candidate_model_contracts import (
    build_candidate_model_contracts,
    summarize_candidate_model_contracts,
)
from advanced_ensemble_model_registry.candidate_model_input_contracts import (
    build_candidate_model_input_contracts,
    summarize_candidate_model_input_contracts,
)
from advanced_ensemble_model_registry.candidate_model_output_contracts import (
    build_candidate_model_output_contracts,
    summarize_candidate_model_output_contracts,
)
from reports.report_builder import ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()

    df_fam, s_fam = build_candidate_model_families()
    data_lake.save_candidate_model_family_registry(df_fam, s_fam)

    df_con, s_con = build_candidate_model_contracts()
    data_lake.save_candidate_model_contract_registry(df_con, s_con)

    df_inp, s_inp = build_candidate_model_input_contracts()
    data_lake.save_candidate_model_input_contract_registry(df_inp, s_inp)

    df_out, s_out = build_candidate_model_output_contracts()
    data_lake.save_candidate_model_output_contract_registry(df_out, s_out)

    print("=" * 70)
    print("PHASE 140: CANDIDATE MODEL FAMILIES & CONTRACTS")
    print("=" * 70)
    print(ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Candidate Families   : {s_fam['total_families']}")
    print(f"Candidate Contracts  : {s_con['total_contracts']}")
    print(f"All Zero Training    : {s_con.get('all_training_disabled', True)}")
    print(f"All Zero Prediction  : {s_con.get('all_prediction_disabled', True)}")
    print(f"All Non-Signal       : {s_con.get('all_non_signal_required', True)}")
    print("=" * 70)


if __name__ == "__main__":
    main()
