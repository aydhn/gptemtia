# -*- coding: utf-8 -*-
"""Phase 158: Run Full-System Integration Profile Registry Script.

Builds and persists profile, domain, and scope registries with Markdown and TXT outputs.
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
from advanced_full_system_integration.full_system_integration_domain_registry import (
    build_full_system_integration_domain_registry,
)
from advanced_full_system_integration.full_system_integration_scope_registry import (
    build_full_system_integration_scope_registry,
)
from advanced_full_system_integration.full_system_integration_report_builder import (
    build_full_system_integration_profile_markdown_report,
)
from reports.report_builder import (
    build_full_system_integration_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_full_system_integration_profile()

    df_prof, s_prof = build_full_system_integration_profile_registry(profile)
    df_dom, s_dom = build_full_system_integration_domain_registry(profile)
    df_scp, s_scp = build_full_system_integration_scope_registry(profile)

    data_lake.save_full_system_integration_profile_registry(df_prof, s_prof)
    data_lake.save_full_system_integration_domain_registry(df_dom, s_dom)
    data_lake.save_full_system_integration_scope_registry(df_scp, s_scp)

    out_dir = Path("reports/output/advanced_full_system_integration")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_report = build_full_system_integration_profile_markdown_report(s_prof, df_prof)
    txt_report = build_full_system_integration_text_report(s_prof, df_prof)

    with open(out_dir / "profiles.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "profiles.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("=" * 70)
    print("PHASE 158: FULL-SYSTEM INTEGRATION PROFILES & SCOPE INITIALIZED")
    print("=" * 70)
    print(f"Active Profile  : {s_prof['active_profile']}")
    print(f"Total Profiles  : {s_prof['total_profiles']}")
    print(f"Total Domains   : {s_dom['total_domains']}")
    print(f"Total Scope     : {s_scp['total_scope_items']}")
    print(f"Dry Run Default : {s_prof['all_dry_run']}")
    print(f"Local Only      : {s_prof['all_local_only']}")
    print(f"Non-Production  : {s_prof['all_non_production']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
