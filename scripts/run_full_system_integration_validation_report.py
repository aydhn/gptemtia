# -*- coding: utf-8 -*-
"""Phase 158: Run Full-System Integration Validation Report Script.

Builds validation and safety boundary reports and checks compliance.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.full_system_integration_profile_registry import (
    build_full_system_integration_profile_registry,
)
from advanced_full_system_integration.system_component_checkpoints import (
    build_system_component_checkpoint_registry,
)
from advanced_full_system_integration.system_contract_integration import (
    build_system_contract_integration_registry,
)
from advanced_full_system_integration.advanced_acceptance_rehearsal import (
    build_advanced_acceptance_rehearsal_registry,
)
from advanced_full_system_integration.full_system_integration_manifest import (
    build_full_system_integration_manifest,
)
from advanced_full_system_integration.full_system_integration_validation import (
    build_full_system_integration_validation_report,
)
from advanced_full_system_integration.full_system_integration_safety_boundary import (
    build_full_system_integration_safety_boundary,
)
from advanced_full_system_integration.full_system_integration_report_builder import (
    build_full_system_integration_validation_markdown_report,
    build_full_system_integration_safety_markdown_report,
)
from reports.report_builder import (
    build_full_system_integration_validation_text_report,
    build_full_system_integration_safety_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_full_system_integration_profile()

    df_prof, _ = build_full_system_integration_profile_registry(profile)
    df_chk, _ = build_system_component_checkpoint_registry(profile)
    df_cnt, _ = build_system_contract_integration_registry(profile)
    df_reh, _ = build_advanced_acceptance_rehearsal_registry(profile)
    df_mnf, _ = build_full_system_integration_manifest(profile)

    eval_tables = {
        "profiles": df_prof,
        "checkpoints": df_chk,
        "contracts": df_cnt,
        "rehearsal": df_reh,
        "manifest": df_mnf,
        "summary": {"active_profile": profile.profile_name},
    }

    df_val, s_val = build_full_system_integration_validation_report(eval_tables, profile)
    df_sft, s_sft = build_full_system_integration_safety_boundary(profile)

    data_lake.save_full_system_integration_validation_report(df_val, s_val)
    data_lake.save_full_system_integration_safety_boundary(df_sft, s_sft)

    out_dir = Path("reports/output/advanced_full_system_integration")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_val = build_full_system_integration_validation_markdown_report(s_val, df_val)
    txt_val = build_full_system_integration_validation_text_report(s_val, df_val)
    md_sft = build_full_system_integration_safety_markdown_report(s_sft, df_sft)
    txt_sft = build_full_system_integration_safety_text_report(s_sft, df_sft)

    with open(out_dir / "validation.md", "w", encoding="utf-8") as f:
        f.write(md_val)
    with open(out_dir / "validation.txt", "w", encoding="utf-8") as f:
        f.write(txt_val)
    with open(out_dir / "safety.md", "w", encoding="utf-8") as f:
        f.write(md_sft)
    with open(out_dir / "safety.txt", "w", encoding="utf-8") as f:
        f.write(txt_sft)

    print("=" * 70)
    print("PHASE 158: VALIDATION & SAFETY BOUNDARY VERIFIED")
    print("=" * 70)
    print(f"Validation Status   : {s_val['validation_status']}")
    print(f"Passed Rules        : {s_val['passed_rules']} / {s_val['total_rules']}")
    print(f"Safety Status       : {s_sft['safety_status']}")
    print(f"NO-GO Rules Enforced: {s_sft['no_go_count']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
