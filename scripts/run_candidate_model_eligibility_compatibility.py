# -*- coding: utf-8 -*-
"""Phase 140: Run Candidate Model Eligibility Gates & Compatibility Matrix Script."""

import sys
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_ensemble_model_registry.candidate_model_eligibility_gates import (
    build_candidate_model_eligibility_gates,
    summarize_candidate_model_eligibility_gates,
)
from advanced_ensemble_model_registry.candidate_model_compatibility_matrix import (
    build_candidate_compatibility_matrix,
    summarize_candidate_compatibility_matrix,
)
from reports.report_builder import ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()

    df_gates, s_gates = build_candidate_model_eligibility_gates()
    data_lake.save_candidate_model_eligibility_gate_registry(df_gates, s_gates)

    df_mat, s_mat = build_candidate_compatibility_matrix()
    data_lake.save_candidate_model_compatibility_matrix(df_mat, s_mat)

    print("=" * 70)
    print("PHASE 140: CANDIDATE MODEL ELIGIBILITY & COMPATIBILITY")
    print("=" * 70)
    print(ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Eligibility Gates    : {s_gates.get('total_gates', len(df_gates))}")
    print(f"All Gates Passed     : {s_gates.get('all_gates_passed', True)}")
    print(f"Compatibility Items  : {s_mat.get('total_compatibility_records', len(df_mat))}")
    print(f"All Non-Signal       : {s_mat.get('non_signal', True)}")
    print("=" * 70)


if __name__ == "__main__":
    main()
