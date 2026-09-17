# -*- coding: utf-8 -*-
"""Phase 141: Run Uncertainty Estimation Contracts Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_calibration_uncertainty.uncertainty_estimation_contracts import (
    build_uncertainty_estimation_contract_registry,
    summarize_uncertainty_estimation_contracts,
)
from advanced_calibration_uncertainty.uncertainty_method_placeholders import (
    build_uncertainty_method_placeholder_registry,
    summarize_uncertainty_method_placeholders,
)
from advanced_calibration_uncertainty.uncertainty_input_contracts import (
    build_uncertainty_input_contract_registry,
    summarize_uncertainty_input_contracts,
)
from advanced_calibration_uncertainty.uncertainty_output_contracts import (
    build_uncertainty_output_contract_registry,
    summarize_uncertainty_output_contracts,
)
from advanced_calibration_uncertainty.uncertainty_quality_gates import (
    build_uncertainty_quality_gate_registry,
    summarize_uncertainty_quality_gates,
)
from reports.report_builder import ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()

    df_con, s_con = build_uncertainty_estimation_contract_registry()
    data_lake.save_uncertainty_estimation_contract_registry(df_con, s_con)

    df_meth, s_meth = build_uncertainty_method_placeholder_registry()
    data_lake.save_uncertainty_method_placeholder_registry(df_meth, s_meth)

    df_inp, s_inp = build_uncertainty_input_contract_registry()
    data_lake.save_uncertainty_input_contract_registry(df_inp, s_inp)

    df_out, s_out = build_uncertainty_output_contract_registry()
    data_lake.save_uncertainty_output_contract_registry(df_out, s_out)

    df_qg, s_qg = build_uncertainty_quality_gate_registry()
    data_lake.save_uncertainty_quality_gate_registry(df_qg, s_qg)

    print("=" * 70)
    print("PHASE 141: UNCERTAINTY ESTIMATION CONTRACTS & GATES")
    print("=" * 70)
    print(ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Uncertainty Contracts  : {s_con.get('total_contracts', 0)}")
    print(f"Uncertainty Methods    : {s_meth.get('total_methods', 0)}")
    print(f"Input Contracts        : {s_inp.get('total_input_contracts', 0)}")
    print(f"Output Contracts       : {s_out.get('total_output_contracts', 0)}")
    print(f"Quality Gates          : {s_qg.get('total_gates', 0)}")
    print(f"Execution Disabled     : {s_con.get('all_zero_uncertainty', True)}")
    print("=" * 70)


if __name__ == "__main__":
    main()
