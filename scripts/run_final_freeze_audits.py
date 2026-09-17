# -*- coding: utf-8 -*-
"""Phase 159: Run Final Freeze Audits Script.

Builds and persists configuration, documentation, safety, validation, and dependency freeze contracts,
as well as settings, env template, and paths audit registries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_final_hardening.final_hardening_config import (
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_configuration_freeze_contracts import (
    build_final_configuration_freeze_contract_registry,
)
from advanced_final_hardening.final_documentation_freeze_contracts import (
    build_final_documentation_freeze_contract_registry,
)
from advanced_final_hardening.final_safety_freeze_contracts import (
    build_final_safety_freeze_contract_registry,
)
from advanced_final_hardening.final_validation_freeze_contracts import (
    build_final_validation_freeze_contract_registry,
)
from advanced_final_hardening.final_dependency_freeze_contracts import (
    build_final_dependency_freeze_contract_registry,
)
from advanced_final_hardening.final_manifest_freeze_contracts import (
    build_final_manifest_freeze_contract_registry,
)
from advanced_final_hardening.final_settings_audit_contracts import (
    build_final_settings_audit_contract_registry,
)
from advanced_final_hardening.final_env_template_audit_contracts import (
    build_final_env_template_audit_contract_registry,
)
from advanced_final_hardening.final_paths_audit_contracts import (
    build_final_paths_audit_contract_registry,
)
from advanced_final_hardening.final_hardening_report_builder import (
    build_final_freeze_markdown_report,
)
from reports.report_builder import (
    build_final_freeze_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_final_hardening_profile()

    df_cf, s_cf = build_final_configuration_freeze_contract_registry(profile)
    df_df, s_df = build_final_documentation_freeze_contract_registry(profile)
    df_sf, s_sf = build_final_safety_freeze_contract_registry(profile)
    df_vf, s_vf = build_final_validation_freeze_contract_registry(profile)
    df_dpf, s_dpf = build_final_dependency_freeze_contract_registry(profile)
    df_mf, s_mf = build_final_manifest_freeze_contract_registry(profile)
    df_sa, s_sa = build_final_settings_audit_contract_registry(profile)
    df_ea, s_ea = build_final_env_template_audit_contract_registry(profile)
    df_pa, s_pa = build_final_paths_audit_contract_registry(profile)

    data_lake.save_final_configuration_freeze_contract_registry(df_cf, s_cf)
    data_lake.save_final_documentation_freeze_contract_registry(df_df, s_df)
    data_lake.save_final_safety_freeze_contract_registry(df_sf, s_sf)
    data_lake.save_final_validation_freeze_contract_registry(df_vf, s_vf)
    data_lake.save_final_dependency_freeze_contract_registry(df_dpf, s_dpf)
    data_lake.save_final_manifest_freeze_contract_registry(df_mf, s_mf)
    data_lake.save_final_settings_audit_contract_registry(df_sa, s_sa)
    data_lake.save_final_env_template_audit_contract_registry(df_ea, s_ea)
    data_lake.save_final_paths_audit_contract_registry(df_pa, s_pa)

    out_dir = Path("reports/output/advanced_final_hardening")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_report = build_final_freeze_markdown_report(s_cf, df_cf)
    txt_report = build_final_freeze_text_report(s_cf, df_cf)

    with open(out_dir / "freeze_audits.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "freeze_audits.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("=" * 70)
    print("PHASE 159: FINAL FREEZE CONTRACTS & AUDITS INITIALIZED")
    print("=" * 70)
    print(f"Config Freeze Items: {s_cf['freeze_item_count']} | Docs Freeze: {s_df['freeze_item_count']}")
    print(f"Safety Freeze: {s_sf['freeze_item_count']} | Settings Audit Passed: {s_sa['all_passed']}")
    print(f"Env Template Audit Passed: {s_ea['all_passed']} | Paths Audit Passed: {s_pa['all_passed']}")
    print(f"Status: {s_cf['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
