# -*- coding: utf-8 -*-
"""Phase 157: Run Portfolio Acceptance Validation Report Script.

Builds and persists validation and safety boundary reports for Phase 157.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_default_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.portfolio_acceptance_profile_registry import (
    build_portfolio_acceptance_profile_registry,
)
from advanced_portfolio_acceptance.portfolio_acceptance_component_checkpoints import (
    build_portfolio_acceptance_component_checkpoint_registry,
)
from advanced_portfolio_acceptance.phase_153_portfolio_construction_acceptance import (
    build_phase_153_portfolio_construction_acceptance_registry,
)
from advanced_portfolio_acceptance.phase_154_portfolio_optimization_acceptance import (
    build_phase_154_portfolio_optimization_acceptance_registry,
)
from advanced_portfolio_acceptance.phase_155_risk_reporting_acceptance import (
    build_phase_155_risk_reporting_acceptance_registry,
)
from advanced_portfolio_acceptance.phase_156_portfolio_scenario_control_acceptance import (
    build_phase_156_portfolio_scenario_control_acceptance_registry,
)
from advanced_portfolio_acceptance.portfolio_acceptance_go_no_go_boundaries import (
    build_portfolio_acceptance_go_no_go_boundary_registry,
)
from advanced_portfolio_acceptance.portfolio_acceptance_manifest import (
    build_portfolio_acceptance_manifest,
)
from advanced_portfolio_acceptance.portfolio_acceptance_validation import (
    build_portfolio_acceptance_validation_report,
)
from advanced_portfolio_acceptance.portfolio_acceptance_safety_boundary import (
    build_portfolio_acceptance_safety_boundary,
)
from advanced_portfolio_acceptance.portfolio_acceptance_report_builder import (
    build_portfolio_acceptance_validation_markdown_report,
    build_portfolio_acceptance_safety_markdown_report,
)
from reports.report_builder import (
    build_portfolio_acceptance_validation_text_report,
    build_portfolio_acceptance_safety_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_portfolio_acceptance_profile()

    df_prof, _ = build_portfolio_acceptance_profile_registry(profile)
    df_chk, _ = build_portfolio_acceptance_component_checkpoint_registry(profile)
    df_153, _ = build_phase_153_portfolio_construction_acceptance_registry(profile)
    df_154, _ = build_phase_154_portfolio_optimization_acceptance_registry(profile)
    df_155, _ = build_phase_155_risk_reporting_acceptance_registry(profile)
    df_156, _ = build_phase_156_portfolio_scenario_control_acceptance_registry(profile)
    df_gng, _ = build_portfolio_acceptance_go_no_go_boundary_registry(profile)
    df_mnf, _ = build_portfolio_acceptance_manifest(profile)

    tables = {
        "profiles": df_prof,
        "checkpoints": df_chk,
        "phase_153": df_153,
        "phase_154": df_154,
        "phase_155": df_155,
        "phase_156": df_156,
        "go_no_go": df_gng,
        "manifest": df_mnf,
    }

    df_val, s_val = build_portfolio_acceptance_validation_report(tables, profile)
    df_sft, s_sft = build_portfolio_acceptance_safety_boundary(profile)

    data_lake.save_portfolio_acceptance_validation_report(df_val, s_val)
    data_lake.save_portfolio_acceptance_safety_boundary(df_sft, s_sft)

    out_dir = Path("reports/output/advanced_portfolio_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)

    with open(out_dir / "validation_report.md", "w", encoding="utf-8") as f:
        f.write(build_portfolio_acceptance_validation_markdown_report(s_val, df_val))
    with open(out_dir / "validation_report.txt", "w", encoding="utf-8") as f:
        f.write(build_portfolio_acceptance_validation_text_report(s_val, df_val))

    with open(out_dir / "safety_boundary.md", "w", encoding="utf-8") as f:
        f.write(build_portfolio_acceptance_safety_markdown_report(s_sft, df_sft))
    with open(out_dir / "safety_boundary.txt", "w", encoding="utf-8") as f:
        f.write(build_portfolio_acceptance_safety_text_report(s_sft, df_sft))

    print("=" * 70)
    print("PHASE 157: PORTFOLIO ACCEPTANCE VALIDATION & SAFETY REPORT")
    print("=" * 70)
    print(f"Validation Status : {s_val['validation_status']}")
    print(f"All Rules Passed  : {s_val['all_passed']}")
    print(f"Safety Status     : {s_sft['safety_status']}")
    print(f"No-Go Rules       : {s_sft['no_go_count']}")
    print(f"Safe-Go Principles: {s_sft['safe_go_count']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
