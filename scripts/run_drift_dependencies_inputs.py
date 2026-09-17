# -*- coding: utf-8 -*-
"""Phase 142: Run Drift Dependencies & Input Contracts Script."""

import sys
from dataclasses import asdict
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_model_drift_monitoring.drift_validation_dependencies import check_drift_validation_dependencies
from advanced_model_drift_monitoring.drift_quality_dependencies import check_drift_quality_dependencies
from advanced_model_drift_monitoring.drift_runtime_dependencies import check_drift_runtime_dependencies
from advanced_model_drift_monitoring.drift_candidate_model_dependencies import check_drift_candidate_model_dependencies
from advanced_model_drift_monitoring.drift_ensemble_dependencies import check_drift_ensemble_dependencies
from advanced_model_drift_monitoring.drift_calibration_uncertainty_dependencies import check_drift_calibration_uncertainty_dependencies
from advanced_model_drift_monitoring.drift_monitoring_input_contracts import build_drift_monitoring_input_contracts
from advanced_model_drift_monitoring.drift_monitoring_output_contracts import build_drift_monitoring_output_contracts
from reports.report_builder import ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()

    val_dep = check_drift_validation_dependencies()
    data_lake.save_drift_validation_dependency_report(pd.DataFrame(val_dep["dependencies"]), val_dep)

    qual_dep = check_drift_quality_dependencies()
    data_lake.save_drift_quality_dependency_report(pd.DataFrame(qual_dep["dependencies"]), qual_dep)

    run_dep = check_drift_runtime_dependencies()
    data_lake.save_drift_runtime_dependency_report(pd.DataFrame(run_dep["dependencies"]), run_dep)

    cand_dep = check_drift_candidate_model_dependencies()
    data_lake.save_drift_candidate_model_dependency_report(pd.DataFrame(cand_dep["dependencies"]), cand_dep)

    ens_dep = check_drift_ensemble_dependencies()
    data_lake.save_drift_ensemble_dependency_report(pd.DataFrame(ens_dep["dependencies"]), ens_dep)

    cal_dep = check_drift_calibration_uncertainty_dependencies()
    data_lake.save_drift_calibration_uncertainty_dependency_report(pd.DataFrame(cal_dep["dependencies"]), cal_dep)

    inputs = build_drift_monitoring_input_contracts()
    data_lake.save_drift_monitoring_input_contract_registry(pd.DataFrame([asdict(c) for c in inputs]))

    outputs = build_drift_monitoring_output_contracts()
    data_lake.save_drift_monitoring_output_contract_registry(pd.DataFrame([asdict(c) for c in outputs]))

    print("=" * 70)
    print("PHASE 142: DRIFT DEPENDENCIES & I/O CONTRACTS")
    print("=" * 70)
    print(ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Validation Dependencies Satisfied : {val_dep['all_satisfied']}")
    print(f"Quality Dependencies Satisfied    : {qual_dep['all_satisfied']}")
    print(f"Runtime Dependencies Satisfied    : {run_dep['all_satisfied']}")
    print(f"Candidate Model Deps Satisfied    : {cand_dep['all_satisfied']}")
    print(f"Ensemble Dependencies Satisfied   : {ens_dep['all_satisfied']}")
    print(f"Calibration Deps Satisfied        : {cal_dep['all_satisfied']}")
    print(f"Input Contracts Registered        : {len(inputs)}")
    print(f"Output Contracts Registered       : {len(outputs)}")
    print("=" * 70)


if __name__ == "__main__":
    main()
