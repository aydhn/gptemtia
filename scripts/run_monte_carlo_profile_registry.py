# -*- coding: utf-8 -*-
"""Phase 149: Run Monte Carlo Profile Registry Script.

Builds and persists Monte Carlo profile, domain, and scope registries.
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
from advanced_monte_carlo_robustness.monte_carlo_domain_registry import (
    build_monte_carlo_domain_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_scope_registry import (
    build_monte_carlo_scope_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_report_builder import (
    build_monte_carlo_profile_markdown_report,
)
from reports.report_builder import build_monte_carlo_profile_text_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_monte_carlo_profile()

    df_prof, s_prof = build_monte_carlo_profile_registry(profile)
    df_dom, s_dom = build_monte_carlo_domain_registry(profile)
    df_scp, s_scp = build_monte_carlo_scope_registry(profile)

    data_lake.save_monte_carlo_profile_registry(df_prof, s_prof)
    data_lake.save_monte_carlo_domain_registry(df_dom, s_dom)
    data_lake.save_monte_carlo_scope_registry(df_scp, s_scp)

    md_report = build_monte_carlo_profile_markdown_report(s_prof, df_prof)
    txt_report = build_monte_carlo_profile_text_report(s_prof, df_prof)

    out_dir = Path("reports/output/advanced_monte_carlo_robustness")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "profiles.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "profiles.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("Monte Carlo profile, domain, and scope registries successfully built.")


if __name__ == "__main__":
    main()
