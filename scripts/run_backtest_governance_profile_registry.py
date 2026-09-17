# -*- coding: utf-8 -*-
"""Phase 150: Run Backtest Governance Profile Registry Script.

Builds and persists Phase 150 backtest governance profile, domain, and scope registries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_governance_profile_registry import (
    build_backtest_governance_profile_registry,
)
from advanced_backtest_governance.backtest_governance_domain_registry import (
    build_backtest_governance_domain_registry,
)
from advanced_backtest_governance.backtest_governance_scope_registry import (
    build_backtest_governance_scope_registry,
)
from advanced_backtest_governance.backtest_governance_report_builder import (
    build_backtest_governance_profile_markdown_report,
)
from reports.report_builder import (
    build_backtest_governance_profile_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_backtest_governance_profile()

    df_prof, s_prof = build_backtest_governance_profile_registry(profile)
    df_dom, s_dom = build_backtest_governance_domain_registry(profile)
    df_scope, s_scope = build_backtest_governance_scope_registry(profile)

    data_lake.save_backtest_governance_profile_registry(df_prof, s_prof)
    data_lake.save_backtest_governance_domain_registry(df_dom, s_dom)
    data_lake.save_backtest_governance_scope_registry(df_scope, s_scope)

    out_dir = Path("reports/output/advanced_backtest_governance")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "profiles.md", "w", encoding="utf-8") as f:
        f.write(build_backtest_governance_profile_markdown_report(s_prof, df_prof))
    with open(out_dir / "profiles.txt", "w", encoding="utf-8") as f:
        f.write(build_backtest_governance_profile_text_report(s_prof, df_prof))

    print("Phase 150 backtest governance profiles, domains, and scopes successfully built.")


if __name__ == "__main__":
    main()
