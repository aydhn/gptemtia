# -*- coding: utf-8 -*-
"""Phase 159: Run Final Hardening Validation Report Script.

Builds and persists validation and safety boundary reports.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_final_hardening.final_hardening_config import (
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_profile_registry import (
    build_final_hardening_profile_registry,
)
from advanced_final_hardening.final_hardening_contracts import (
    build_final_hardening_contract_registry,
)
from advanced_final_hardening.operator_runbook_contracts import (
    build_operator_runbook_contract_registry,
)
from advanced_final_hardening.release_candidate_contracts import (
    build_release_candidate_contract_registry,
)
from advanced_final_hardening.final_hardening_validation import (
    build_final_hardening_validation_report,
)
from advanced_final_hardening.final_hardening_safety_boundary import (
    build_final_hardening_safety_boundary,
)
from advanced_final_hardening.release_candidate_manifest import (
    build_release_candidate_manifest,
)
from advanced_final_hardening.final_hardening_report_builder import (
    build_final_hardening_validation_markdown_report,
    build_final_hardening_safety_markdown_report,
)
from reports.report_builder import (
    build_final_hardening_validation_text_report,
    build_final_hardening_safety_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_final_hardening_profile()

    df_prof, _ = build_final_hardening_profile_registry(profile)
    df_c, _ = build_final_hardening_contract_registry(profile)
    df_rb, _ = build_operator_runbook_contract_registry(profile)
    df_rc, _ = build_release_candidate_contract_registry(profile)
    df_mnf, _ = build_release_candidate_manifest(profile)

    val_tables = {
        "profiles": df_prof,
        "contracts": df_c,
        "runbooks": df_rb,
        "rc_contracts": df_rc,
        "manifest": df_mnf,
    }

    df_val, s_val = build_final_hardening_validation_report(val_tables, profile)
    df_sfty, s_sfty = build_final_hardening_safety_boundary(profile)

    data_lake.save_release_candidate_validation_report(df_val, s_val)
    data_lake.save_release_candidate_safety_boundary(df_sfty, s_sfty)

    out_dir = Path("reports/output/advanced_final_hardening")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_val = build_final_hardening_validation_markdown_report(s_val, df_val)
    txt_val = build_final_hardening_validation_text_report(s_val, df_val)
    md_sfty = build_final_hardening_safety_markdown_report(s_sfty, df_sfty)
    txt_sfty = build_final_hardening_safety_text_report(s_sfty, df_sfty)

    with open(out_dir / "validation.md", "w", encoding="utf-8") as f:
        f.write(md_val)
    with open(out_dir / "validation.txt", "w", encoding="utf-8") as f:
        f.write(txt_val)
    with open(out_dir / "safety.md", "w", encoding="utf-8") as f:
        f.write(md_sfty)
    with open(out_dir / "safety.txt", "w", encoding="utf-8") as f:
        f.write(txt_sfty)

    print("=" * 70)
    print("PHASE 159: FINAL HARDENING VALIDATION & SAFETY REPORT INITIALIZED")
    print("=" * 70)
    print(f"Validation Status: {s_val['validation_status']} | All Passed: {s_val['all_passed']}")
    print(f"Safety Status: {s_sfty['safety_status']} | NO-GO Count: {s_sfty['no_go_count']}")
    print(f"Status: {s_val['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
