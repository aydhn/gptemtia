# -*- coding: utf-8 -*-
"""Phase 141: Run Probability Calibration Contracts Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_calibration_uncertainty.probability_calibration_contracts import (
    build_probability_calibration_contract_registry,
    summarize_probability_calibration_contracts,
)
from advanced_calibration_uncertainty.calibration_method_placeholders import (
    build_calibration_method_placeholder_registry,
    summarize_calibration_method_placeholders,
)
from advanced_calibration_uncertainty.calibration_input_contracts import (
    build_calibration_input_contract_registry,
    summarize_calibration_input_contracts,
)
from advanced_calibration_uncertainty.calibration_output_contracts import (
    build_calibration_output_contract_registry,
    summarize_calibration_output_contracts,
)
from advanced_calibration_uncertainty.calibration_quality_gates import (
    build_calibration_quality_gate_registry,
    summarize_calibration_quality_gates,
)
from reports.report_builder import ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()

    df_con, s_con = build_probability_calibration_contract_registry()
    data_lake.save_probability_calibration_contract_registry(df_con, s_con)

    df_meth, s_meth = build_calibration_method_placeholder_registry()
    data_lake.save_calibration_method_placeholder_registry(df_meth, s_meth)

    df_inp, s_inp = build_calibration_input_contract_registry()
    data_lake.save_calibration_input_contract_registry(df_inp, s_inp)

    df_out, s_out = build_calibration_output_contract_registry()
    data_lake.save_calibration_output_contract_registry(df_out, s_out)

    df_qg, s_qg = build_calibration_quality_gate_registry()
    data_lake.save_calibration_quality_gate_registry(df_qg, s_qg)

    print("=" * 70)
    print("PHASE 141: PROBABILITY CALIBRATION CONTRACTS & GATES")
    print("=" * 70)
    print(ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Calibration Contracts  : {s_con.get('total_contracts', 0)}")
    print(f"Calibration Methods    : {s_meth.get('total_methods', 0)}")
    print(f"Input Contracts        : {s_inp.get('total_input_contracts', 0)}")
    print(f"Output Contracts       : {s_out.get('total_output_contracts', 0)}")
    print(f"Quality Gates          : {s_qg.get('total_gates', 0)}")
    print(f"Execution Disabled     : {s_con.get('all_zero_prediction', True)}")
    print("=" * 70)


if __name__ == "__main__":
    main()
