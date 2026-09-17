"""Phase 138: Run Baseline Model Dependencies and Inputs Script.

Builds and persists validation dependencies, quality dependencies, lineage, FeatureStore inputs, regime inputs, and experiment linkages.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_baseline_ml_models.baseline_ml_model_config import (
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.baseline_model_validation_dependencies import (
    build_baseline_model_validation_dependency_registry,
)
from advanced_baseline_ml_models.baseline_model_quality_dependencies import (
    build_baseline_model_quality_dependency_registry,
)
from advanced_baseline_ml_models.baseline_model_lineage import (
    build_baseline_model_lineage_registry,
)
from advanced_baseline_ml_models.baseline_model_featurestore_inputs import (
    build_baseline_model_featurestore_input_registry,
)
from advanced_baseline_ml_models.baseline_model_regime_inputs import (
    build_baseline_model_regime_input_registry,
)
from advanced_baseline_ml_models.baseline_model_experiment_linkage import (
    build_baseline_model_experiment_linkage_registry,
)
from reports.report_builder import ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_baseline_ml_model_profile()

    df_vd, s_vd = build_baseline_model_validation_dependency_registry(profile)
    data_lake.save_baseline_model_validation_dependency_registry(df_vd, s_vd)

    df_qd, s_qd = build_baseline_model_quality_dependency_registry(profile)
    data_lake.save_baseline_model_quality_dependency_registry(df_qd, s_qd)


    df_lin, s_lin = build_baseline_model_lineage_registry(profile)
    data_lake.save_baseline_model_lineage_registry(df_lin, s_lin)

    df_fs, s_fs = build_baseline_model_featurestore_input_registry(profile)
    data_lake.save_baseline_model_featurestore_input_registry(df_fs, s_fs)

    df_reg, s_reg = build_baseline_model_regime_input_registry(profile)
    data_lake.save_baseline_model_regime_input_registry(df_reg, s_reg)

    df_exp, s_exp = build_baseline_model_experiment_linkage_registry(profile)
    data_lake.save_baseline_model_experiment_linkage_registry(df_exp, s_exp)

    print("=" * 70)
    print("PHASE 138: BASELINE MODEL DEPENDENCIES & INPUTS")
    print("=" * 70)
    print(ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Validation Dependencies: {s_vd['total_dependencies']}")
    print(f"Quality Dependencies   : {s_qd['total_dependencies']}")
    print(f"Lineage Records        : {s_lin.get('total_lineage_stages', 0)}")
    print(f"FeatureStore Inputs    : {s_fs.get('total_namespaces', 0)}")
    print(f"Regime Inputs          : {s_reg['total_regime_inputs']}")

    print(f"Experiment Linkages    : {s_exp['total_linkages']}")
    print(f"Dependencies Satisfied : {s_vd['all_satisfied']}")
    print("=" * 70)



if __name__ == "__main__":
    main()
