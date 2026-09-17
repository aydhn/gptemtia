# -*- coding: utf-8 -*-
"""Phase 160: Run Final Delivery Profile Registry Script.

Builds and persists profile, domain, and scope registries with Markdown and TXT outputs.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_final_delivery.final_delivery_config import (
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_profile_registry import (
    build_final_delivery_profile_registry,
)
from advanced_final_delivery.final_delivery_domain_registry import (
    build_final_delivery_domain_registry,
)
from advanced_final_delivery.final_delivery_scope_registry import (
    build_final_delivery_scope_registry,
)
from advanced_final_delivery.final_delivery_report_builder import (
    build_final_delivery_profile_markdown_report,
)
from reports.report_builder import (
    build_final_delivery_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_final_delivery_profile()

    df_prof, s_prof = build_final_delivery_profile_registry(profile)
    df_dom, s_dom = build_final_delivery_domain_registry(profile)
    df_scp, s_scp = build_final_delivery_scope_registry(profile)

    if "--no-save" not in sys.argv and settings.final_delivery_save_reports:
        data_lake.save_final_delivery_profile_registry(df_prof, s_prof)
        data_lake.save_final_delivery_domain_registry(df_dom, s_dom)
        data_lake.save_final_delivery_scope_registry(df_scp, s_scp)

    out_dir = Path("reports/output/advanced_final_delivery")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_report = build_final_delivery_profile_markdown_report(s_prof, df_prof)
    txt_report = build_final_delivery_text_report(s_prof, df_prof)

    if "--no-save" not in sys.argv:
        with open(out_dir / "profiles.md", "w", encoding="utf-8") as f:
            f.write(md_report)
        with open(out_dir / "profiles.txt", "w", encoding="utf-8") as f:
            f.write(txt_report)

    print("=" * 70)
    print("PHASE 160: FINAL DELIVERY PROFILES & SCOPE INITIALIZED")
    print("=" * 70)
    print(f"Active Profile: {s_prof['active_profile']}")
    print(f"Profiles: {s_prof['profile_count']} | Domains: {s_dom['domain_count']} | Scope Items: {s_scp['scope_item_count']}")
    print(f"Status: {s_prof['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
