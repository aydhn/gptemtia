# -*- coding: utf-8 -*-
"""Phase 157: Run Portfolio Acceptance Profile Registry Script.

Builds and persists profile, domain, and scope registries with Markdown and TXT outputs.
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
from advanced_portfolio_acceptance.portfolio_acceptance_domain_registry import (
    build_portfolio_acceptance_domain_registry,
)
from advanced_portfolio_acceptance.portfolio_acceptance_scope_registry import (
    build_portfolio_acceptance_scope_registry,
)
from advanced_portfolio_acceptance.portfolio_acceptance_report_builder import (
    build_portfolio_acceptance_profile_markdown_report,
)
from reports.report_builder import (
    build_portfolio_acceptance_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_portfolio_acceptance_profile()

    df_prof, s_prof = build_portfolio_acceptance_profile_registry(profile)
    df_dom, s_dom = build_portfolio_acceptance_domain_registry(profile)
    df_scp, s_scp = build_portfolio_acceptance_scope_registry(profile)

    data_lake.save_portfolio_acceptance_profile_registry(df_prof, s_prof)
    data_lake.save_portfolio_acceptance_domain_registry(df_dom, s_dom)
    data_lake.save_portfolio_acceptance_scope_registry(df_scp, s_scp)

    out_dir = Path("reports/output/advanced_portfolio_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_report = build_portfolio_acceptance_profile_markdown_report(s_prof, df_prof)
    txt_report = build_portfolio_acceptance_text_report(s_prof, df_prof)

    with open(out_dir / "profiles.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "profiles.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("=" * 70)
    print("PHASE 157: PORTFOLIO ACCEPTANCE PROFILES & SCOPE INITIALIZED")
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
