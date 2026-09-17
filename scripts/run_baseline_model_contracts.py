"""Phase 138: Run Baseline Model Contracts Script.

Builds and persists model families, model contracts, input/output contracts, and training plans.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_baseline_ml_models.baseline_ml_model_config import (
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.baseline_model_families import (
    build_baseline_model_family_registry,
)
from advanced_baseline_ml_models.baseline_model_contracts import (
    build_baseline_model_contract_registry,
)
from advanced_baseline_ml_models.baseline_model_input_contracts import (
    build_baseline_model_input_contract_registry,
)
from advanced_baseline_ml_models.baseline_model_output_contracts import (
    build_baseline_model_output_contract_registry,
)
from advanced_baseline_ml_models.baseline_model_training_plans import (
    build_baseline_model_training_plan_registry,
)
from reports.report_builder import ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_baseline_ml_model_profile()

    df_fam, s_fam = build_baseline_model_family_registry(profile)
    data_lake.save_baseline_model_family_registry(df_fam, s_fam)

    df_cont, s_cont = build_baseline_model_contract_registry(profile)
    data_lake.save_baseline_model_contract_registry(df_cont, s_cont)

    df_inp, s_inp = build_baseline_model_input_contract_registry(profile)
    data_lake.save_baseline_model_input_contract_registry(df_inp, s_inp)

    df_out, s_out = build_baseline_model_output_contract_registry(profile)
    data_lake.save_baseline_model_output_contract_registry(df_out, s_out)

    df_tp, s_tp = build_baseline_model_training_plan_registry(profile)
    data_lake.save_baseline_model_training_plan_registry(df_tp, s_tp)

    print("=" * 70)
    print("PHASE 138: BASELINE MODEL CONTRACTS")
    print("=" * 70)
    print(ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Model Families   : {s_fam['total_families']}")
    print(f"Model Contracts  : {s_cont['total_contracts']}")
    print(f"Input Contracts  : {s_inp['total_input_contracts']}")
    print(f"Output Contracts : {s_out['total_output_contracts']}")
    print(f"Training Plans   : {s_tp['total_training_plans']}")
    print(f"Real Training    : {s_tp.get('zero_real_training_allowed', True)}")
    print("=" * 70)



if __name__ == "__main__":
    main()
