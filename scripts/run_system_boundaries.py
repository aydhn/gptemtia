# -*- coding: utf-8 -*-
"""Phase 158: Run System Boundaries Script.

Builds and persists safety, non-production, dry-run, and forbidden column boundaries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.system_safety_boundaries import (
    build_system_safety_boundary_registry,
)
from advanced_full_system_integration.system_non_production_boundaries import (
    build_system_non_production_boundary_registry,
)
from advanced_full_system_integration.system_dry_run_boundaries import (
    build_system_dry_run_boundary_registry,
)
from advanced_full_system_integration.system_manual_review_gates import (
    build_system_manual_review_gate_registry,
)
from advanced_full_system_integration.forbidden_column_system_policies import (
    build_forbidden_column_system_policy_registry,
)
from advanced_full_system_integration.full_system_integration_report_builder import (
    build_system_boundary_markdown_report,
)
from reports.report_builder import (
    build_system_boundary_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_full_system_integration_profile()

    df_sft, s_sft = build_system_safety_boundary_registry(profile)
    df_npb, s_npb = build_system_non_production_boundary_registry(profile)
    df_drb, s_drb = build_system_dry_run_boundary_registry(profile)
    df_mrg, s_mrg = build_system_manual_review_gate_registry(profile)
    df_fcp, s_fcp = build_forbidden_column_system_policy_registry(profile)

    data_lake.save_system_safety_boundary_registry(df_sft, s_sft)
    data_lake.save_system_non_production_boundary_registry(df_npb, s_npb)
    data_lake.save_system_dry_run_boundary_registry(df_drb, s_drb)
    data_lake.save_system_manual_review_gate_registry(df_mrg, s_mrg)
    data_lake.save_forbidden_column_system_policy_registry(df_fcp, s_fcp)

    out_dir = Path("reports/output/advanced_full_system_integration")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_bnd = build_system_boundary_markdown_report(s_sft, df_sft)
    txt_bnd = build_system_boundary_text_report(s_sft, df_sft)

    with open(out_dir / "boundaries.md", "w", encoding="utf-8") as f:
        f.write(md_bnd)
    with open(out_dir / "boundaries.txt", "w", encoding="utf-8") as f:
        f.write(txt_bnd)

    print("=" * 70)
    print("PHASE 158: SYSTEM BOUNDARIES & GOVERNANCE GATES INITIALIZED")
    print("=" * 70)
    print(f"Total Safety Rules    : {s_sft['total_rules']}")
    print(f"Prohibited Count      : {s_sft['prohibited_actions_count']}")
    print(f"Manual Review Gates   : {s_mrg['total_review_gates']}")
    print(f"Forbidden Columns     : {s_fcp['total_forbidden_columns']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
