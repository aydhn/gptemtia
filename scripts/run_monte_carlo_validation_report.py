# -*- coding: utf-8 -*-
"""Phase 149: Run Monte Carlo Validation Report Script.

Runs comprehensive validation suites verifying negative invariants and safety boundaries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_monte_carlo_robustness.monte_carlo_config import (
    get_default_monte_carlo_profile,
)
from advanced_monte_carlo_robustness.monte_carlo_profile_registry import (
    build_monte_carlo_profile_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_robustness_contracts import (
    build_monte_carlo_robustness_contract_registry,
)
from advanced_monte_carlo_robustness.parameter_stability_contracts import (
    build_parameter_stability_contract_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_manifest import (
    build_monte_carlo_robustness_manifest,
)
from advanced_monte_carlo_robustness.monte_carlo_validation import (
    build_monte_carlo_validation_report,
)
from advanced_monte_carlo_robustness.monte_carlo_safety_boundary import (
    build_monte_carlo_safety_boundary,
)
from advanced_monte_carlo_robustness.phase_150_handoff import (
    build_phase_150_backtest_governance_bias_control_handoff_report,
)
from advanced_monte_carlo_robustness.monte_carlo_report_builder import (
    build_monte_carlo_validation_markdown_report,
    build_monte_carlo_safety_markdown_report,
    build_phase_150_handoff_markdown_report,
)
from reports.report_builder import (
    build_monte_carlo_validation_text_report,
    build_monte_carlo_safety_text_report,
    build_phase_150_handoff_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_monte_carlo_profile()

    df_prof, _ = build_monte_carlo_profile_registry(profile)
    df_core, _ = build_monte_carlo_robustness_contract_registry(profile)
    df_stab, _ = build_parameter_stability_contract_registry(profile)
    df_man, _ = build_monte_carlo_robustness_manifest(profile)

    tables = {
        "profiles": df_prof,
        "contracts": df_core,
        "stability": df_stab,
        "manifest": df_man,
    }

    df_val, s_val = build_monte_carlo_validation_report(tables, profile)
    df_safe, s_safe = build_monte_carlo_safety_boundary(profile)
    df_hndf, s_hndf = build_phase_150_backtest_governance_bias_control_handoff_report(profile)

    data_lake.save_monte_carlo_validation_report(df_val, s_val)
    data_lake.save_monte_carlo_safety_boundary(df_safe, s_safe)
    data_lake.save_phase_150_backtest_governance_bias_control_handoff_report(df_hndf, s_hndf)

    out_dir = Path("reports/output/advanced_monte_carlo_robustness")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "validation_report.md", "w", encoding="utf-8") as f:
        f.write(build_monte_carlo_validation_markdown_report(s_val, df_val))
    with open(out_dir / "validation_report.txt", "w", encoding="utf-8") as f:
        f.write(build_monte_carlo_validation_text_report(s_val, df_val))
    with open(out_dir / "safety_boundary.md", "w", encoding="utf-8") as f:
        f.write(build_monte_carlo_safety_markdown_report(s_safe, df_safe))
    with open(out_dir / "safety_boundary.txt", "w", encoding="utf-8") as f:
        f.write(build_monte_carlo_safety_text_report(s_safe, df_safe))
    with open(out_dir / "phase_150_handoff.md", "w", encoding="utf-8") as f:
        f.write(build_phase_150_handoff_markdown_report(s_hndf, df_hndf))
    with open(out_dir / "phase_150_handoff.txt", "w", encoding="utf-8") as f:
        f.write(build_phase_150_handoff_text_report(s_hndf, df_hndf))

    print("=" * 60)
    print("PHASE 149: VALIDATION & SAFETY REPORT")
    print("=" * 60)
    print(df_val.to_string(index=False))
    print("-" * 60)
    print(f"Validation Status : {s_val.get('validation_status')}")
    print(f"Passed Checks     : {s_val.get('passed_checks')}/{s_val.get('total_checks')}")
    print(f"Phase 150 Handoff : {s_hndf.get('status')}")
    print("=" * 60)


if __name__ == "__main__":
    main()
