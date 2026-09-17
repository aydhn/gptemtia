# -*- coding: utf-8 -*-
"""Phase 148: Run Stress Testing Validation Report Script.

Performs formal validation suite for Phase 148 stress testing contracts and saves reports.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_testing_validation import (
    validate_stress_testing,
)
from advanced_stress_testing.stress_testing_safety_boundary import (
    enforce_stress_testing_safety_boundary,
)
from advanced_stress_testing.phase_149_handoff import (
    build_phase_149_monte_carlo_robustness_parameter_stability_handoff_report,
)
from advanced_stress_testing.stress_testing_report_builder import (
    build_stress_testing_validation_markdown_report,
    build_stress_testing_safety_markdown_report,
    build_phase_149_handoff_markdown_report,
)
from reports.report_builder import (
    build_stress_testing_validation_text_report,
    build_stress_testing_safety_text_report,
    build_phase_149_handoff_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_stress_testing_profile()

    df_val, s_val = validate_stress_testing(profile)
    df_saf, s_saf = enforce_stress_testing_safety_boundary(profile)
    df_han, s_han = build_phase_149_monte_carlo_robustness_parameter_stability_handoff_report(profile)

    data_lake.save_stress_testing_validation_report(df_val, s_val)
    data_lake.save_stress_testing_safety_boundary(df_saf, s_saf)
    data_lake.save_phase_149_monte_carlo_robustness_parameter_stability_handoff_report(df_han, s_han)

    md_val = build_stress_testing_validation_markdown_report(s_val, df_val)
    txt_val = build_stress_testing_validation_text_report(s_val, df_val)

    md_saf = build_stress_testing_safety_markdown_report(s_saf, df_saf)
    txt_saf = build_stress_testing_safety_text_report(s_saf, df_saf)

    md_han = build_phase_149_handoff_markdown_report(s_han, df_han)
    txt_han = build_phase_149_handoff_text_report(s_han, df_han)

    out_dir = Path("reports/output/advanced_stress_testing")
    out_dir.mkdir(parents=True, exist_ok=True)

    with open(out_dir / "validation.md", "w", encoding="utf-8") as f:
        f.write(md_val)
    with open(out_dir / "validation.txt", "w", encoding="utf-8") as f:
        f.write(txt_val)

    with open(out_dir / "safety.md", "w", encoding="utf-8") as f:
        f.write(md_saf)
    with open(out_dir / "safety.txt", "w", encoding="utf-8") as f:
        f.write(txt_saf)

    with open(out_dir / "phase_149_handoff.md", "w", encoding="utf-8") as f:
        f.write(md_han)
    with open(out_dir / "phase_149_handoff.txt", "w", encoding="utf-8") as f:
        f.write(txt_han)

    print("=" * 70)
    print("PHASE 148: STRESS TESTING VALIDATION, SAFETY & PHASE 149 HANDOFF")
    print("=" * 70)
    print(f"Validation Status: {s_val.get('validation_status')}")
    print(f"Safety Status    : {s_saf.get('safety_status')}")
    print(f"Handoff Status   : {s_han.get('handoff_status')}")
    print(f"Next Phase       : {s_han.get('next_phase_name')}")
    print(f"All Ready        : {s_han.get('all_prerequisites_satisfied')}")
    print("=" * 70)


if __name__ == "__main__":
    main()
