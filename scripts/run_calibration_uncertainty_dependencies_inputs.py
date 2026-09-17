# -*- coding: utf-8 -*-
"""Phase 141: Run Calibration & Uncertainty Dependencies & Guards Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_calibration_uncertainty.calibration_candidate_model_dependencies import (
    build_calibration_candidate_model_dependency_registry,
    summarize_calibration_candidate_model_dependencies,
)
from advanced_calibration_uncertainty.calibration_ensemble_dependencies import (
    build_calibration_ensemble_dependency_registry,
    summarize_calibration_ensemble_dependencies,
)
from advanced_calibration_uncertainty.calibration_dataset_dependencies import (
    build_calibration_dataset_dependency_registry,
    summarize_calibration_dataset_dependencies,
)
from advanced_calibration_uncertainty.calibration_runtime_dependencies import (
    build_calibration_runtime_dependency_registry,
    summarize_calibration_runtime_dependencies,
)
from advanced_calibration_uncertainty.calibration_no_lookahead_guards import (
    build_calibration_no_lookahead_guard_registry,
    summarize_calibration_no_lookahead_guards,
)
from advanced_calibration_uncertainty.calibration_metadata_only_news_guards import (
    build_calibration_metadata_only_news_guard_registry,
    summarize_calibration_metadata_only_news_guards,
)
from advanced_calibration_uncertainty.calibration_source_preservation_guards import (
    build_calibration_source_preservation_guard_registry,
    summarize_calibration_source_preservation_guards,
)
from advanced_calibration_uncertainty.calibration_forbidden_column_policies import (
    build_calibration_forbidden_column_policy_registry,
    summarize_calibration_forbidden_column_policies,
)
from advanced_calibration_uncertainty.uncertainty_no_lookahead_guards import (
    build_uncertainty_no_lookahead_guard_registry,
    summarize_uncertainty_no_lookahead_guards,
)
from advanced_calibration_uncertainty.uncertainty_metadata_only_news_guards import (
    build_uncertainty_metadata_only_news_guard_registry,
    summarize_uncertainty_metadata_only_news_guards,
)
from advanced_calibration_uncertainty.uncertainty_source_preservation_guards import (
    build_uncertainty_source_preservation_guard_registry,
    summarize_uncertainty_source_preservation_guards,
)
from advanced_calibration_uncertainty.uncertainty_forbidden_column_policies import (
    build_uncertainty_forbidden_column_policy_registry,
    summarize_uncertainty_forbidden_column_policies,
)
from advanced_calibration_uncertainty.calibration_uncertainty_lineage import (
    build_calibration_uncertainty_lineage_registry,
    summarize_calibration_uncertainty_lineage,
)
from advanced_calibration_uncertainty.calibration_uncertainty_experiment_linkage import (
    build_calibration_uncertainty_experiment_linkage_registry,
    summarize_calibration_uncertainty_experiment_linkage,
)
from reports.report_builder import ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()

    df_cmd, s_cmd = build_calibration_candidate_model_dependency_registry()
    data_lake.save_calibration_candidate_model_dependency_registry(df_cmd, s_cmd)

    df_ed, s_ed = build_calibration_ensemble_dependency_registry()
    data_lake.save_calibration_ensemble_dependency_registry(df_ed, s_ed)

    df_dd, s_dd = build_calibration_dataset_dependency_registry()
    data_lake.save_calibration_dataset_dependency_registry(df_dd, s_dd)

    df_rd, s_rd = build_calibration_runtime_dependency_registry()
    data_lake.save_calibration_runtime_dependency_registry(df_rd, s_rd)

    df_cnl, s_cnl = build_calibration_no_lookahead_guard_registry()
    data_lake.save_calibration_no_lookahead_guard_registry(df_cnl, s_cnl)

    df_cmn, s_cmn = build_calibration_metadata_only_news_guard_registry()
    data_lake.save_calibration_metadata_only_news_guard_registry(df_cmn, s_cmn)

    df_csp, s_csp = build_calibration_source_preservation_guard_registry()
    data_lake.save_calibration_source_preservation_guard_registry(df_csp, s_csp)

    df_cfc, s_cfc = build_calibration_forbidden_column_policy_registry()
    data_lake.save_calibration_forbidden_column_policy_registry(df_cfc, s_cfc)

    df_unl, s_unl = build_uncertainty_no_lookahead_guard_registry()
    data_lake.save_uncertainty_no_lookahead_guard_registry(df_unl, s_unl)

    df_umn, s_umn = build_uncertainty_metadata_only_news_guard_registry()
    data_lake.save_uncertainty_metadata_only_news_guard_registry(df_umn, s_umn)

    df_usp, s_usp = build_uncertainty_source_preservation_guard_registry()
    data_lake.save_uncertainty_source_preservation_guard_registry(df_usp, s_usp)

    df_ufc, s_ufc = build_uncertainty_forbidden_column_policy_registry()
    data_lake.save_uncertainty_forbidden_column_policy_registry(df_ufc, s_ufc)

    df_lin, s_lin = build_calibration_uncertainty_lineage_registry()
    data_lake.save_calibration_uncertainty_lineage_registry(df_lin, s_lin)

    df_exp, s_exp = build_calibration_uncertainty_experiment_linkage_registry()
    data_lake.save_calibration_uncertainty_experiment_linkage_registry(df_exp, s_exp)

    print("=" * 70)
    print("PHASE 141: CALIBRATION & UNCERTAINTY DEPENDENCIES & GUARDS")
    print("=" * 70)
    print(ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Candidate Dependencies     : {s_cmd.get('total_dependencies', 0)}")
    print(f"Ensemble Dependencies      : {s_ed.get('total_dependencies', 0)}")
    print(f"Dataset Dependencies       : {s_dd.get('total_dependencies', 0)}")
    print(f"Runtime Dependencies       : {s_rd.get('total_dependencies', 0)}")
    print(f"Calibration Lookahead Grds : {s_cnl.get('total_guards', 0)}")
    print(f"Uncertainty Lookahead Grds : {s_unl.get('total_guards', 0)}")
    print(f"Calibration Forbidden Cols : {s_cfc.get('total_policies', 0)}")
    print(f"Uncertainty Forbidden Cols : {s_ufc.get('total_policies', 0)}")
    print(f"Lineage Records            : {s_lin.get('total_records', len(df_lin))}")
    print(f"Experiment Linkages        : {s_exp.get('total_linkages', len(df_exp))}")
    print("=" * 70)


if __name__ == "__main__":
    main()
