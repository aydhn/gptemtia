"""Phase 127: Run Regime Matrix Validation and Safety Report Script.

Runs validation rules, safety boundaries, non-signal policies, and Phase 128 handoff.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_matrix.regime_matrix_config import (
    get_default_regime_matrix_profile,
)
from advanced_regime_matrix.regime_matrix_validation import (
    run_regime_matrix_validation,
)
from advanced_regime_matrix.regime_matrix_safety_boundary import (
    audit_regime_matrix_safety_boundary,
)
from advanced_regime_matrix.regime_matrix_non_signal_policies import (
    build_regime_matrix_non_signal_policies,
)
from advanced_regime_matrix.regime_matrix_source_preservation_policies import (
    build_regime_matrix_source_preservation_policies,
)
from advanced_regime_matrix.phase_128_handoff import (
    build_phase_128_handoff_registry,
)
from advanced_regime_matrix.regime_matrix_report_builder import (
    build_regime_matrix_validation_markdown_report,
    build_regime_matrix_safety_markdown_report,
    build_phase_128_handoff_markdown_report,
)
from reports.report_builder import (
    build_regime_matrix_validation_text_report,
    build_regime_matrix_safety_text_report,
    build_phase_128_handoff_text_report,
)


def main():
    data_lake = DataLake()
    profile = get_default_regime_matrix_profile()

    df_val, s_val = run_regime_matrix_validation()
    df_saf, s_saf = audit_regime_matrix_safety_boundary()
    df_nsp, s_nsp = build_regime_matrix_non_signal_policies()
    df_spp, s_spp = build_regime_matrix_source_preservation_policies()
    df_ho, s_ho = build_phase_128_handoff_registry()

    data_lake.save_regime_matrix_validation(df_val, s_val)
    data_lake.save_regime_matrix_safety(df_saf, s_saf)
    data_lake.save_regime_matrix_non_signal_policies(df_nsp, s_nsp)
    data_lake.save_regime_matrix_source_preservation_policies(df_spp, s_spp)
    data_lake.save_phase_128_handoff(df_ho, s_ho)

    md_val = build_regime_matrix_validation_markdown_report(s_val, df_val)
    txt_val = build_regime_matrix_validation_text_report(s_val, df_val)
    md_saf = build_regime_matrix_safety_markdown_report(s_saf, df_saf)
    txt_saf = build_regime_matrix_safety_text_report(s_saf, df_saf)
    md_ho = build_phase_128_handoff_markdown_report(s_ho, df_ho)
    txt_ho = build_phase_128_handoff_text_report(s_ho, df_ho)

    out_dir = Path("reports/output/advanced_regime_matrix")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "validation_report.md", "w", encoding="utf-8") as f:
        f.write(md_val)
    with open(out_dir / "validation_report.txt", "w", encoding="utf-8") as f:
        f.write(txt_val)
    with open(out_dir / "safety_report.md", "w", encoding="utf-8") as f:
        f.write(md_saf)
    with open(out_dir / "safety_report.txt", "w", encoding="utf-8") as f:
        f.write(txt_saf)
    with open(out_dir / "phase_128_handoff.md", "w", encoding="utf-8") as f:
        f.write(md_ho)
    with open(out_dir / "phase_128_handoff.txt", "w", encoding="utf-8") as f:
        f.write(txt_ho)

    print("=" * 70)
    print("PHASE 127: REGIME MATRIX VALIDATION, SAFETY & PHASE 128 HANDOFF")
    print("=" * 70)
    print(f"Validation Status: {s_val['validation_status']}")
    print(f"Passed Rules     : {s_val['passed_rules']}/{s_val['total_rules']}")
    print(f"Forbidden Clean  : {s_val['forbidden_claims_clean']}")
    print(f"Safety Status    : {s_saf['safety_status']}")
    print(f"NO-GO Rules      : {s_saf['no_go_count']}")
    print(f"SAFE-GO Rules    : {s_saf['safe_go_count']}")
    print(f"Phase 128 Handoff: {s_ho['handoff_status']}")
    print(f"Total Handoff    : {s_ho['total_handoff_items']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
