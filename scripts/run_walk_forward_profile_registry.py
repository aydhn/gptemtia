# -*- coding: utf-8 -*-
"""Phase 147: Run Walk-Forward Profile Registry Script.

Builds and persists walk-forward profile, domain, and scope registries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_walk_forward_validation.walk_forward_config import (
    get_default_walk_forward_profile,
)
from advanced_walk_forward_validation.walk_forward_profile_registry import (
    build_walk_forward_profile_registry,
)
from advanced_walk_forward_validation.walk_forward_domain_registry import (
    build_walk_forward_domain_registry,
)
from advanced_walk_forward_validation.walk_forward_scope_registry import (
    build_walk_forward_scope_registry,
)
from advanced_walk_forward_validation.walk_forward_report_builder import (
    build_walk_forward_profile_markdown_report,
)
from reports.report_builder import build_walk_forward_profile_text_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_walk_forward_profile()

    df_prof, s_prof = build_walk_forward_profile_registry(profile)
    df_dom, s_dom = build_walk_forward_domain_registry(profile)
    df_scp, s_scp = build_walk_forward_scope_registry(profile)

    data_lake.save_walk_forward_profile_registry(df_prof, s_prof)
    data_lake.save_walk_forward_domain_registry(df_dom, s_dom)
    data_lake.save_walk_forward_scope_registry(df_scp, s_scp)

    md_report = build_walk_forward_profile_markdown_report(s_prof, df_prof)
    txt_report = build_walk_forward_profile_text_report(s_prof, df_prof)

    out_dir = Path("reports/output/advanced_walk_forward_validation")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "profiles.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "profiles.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("Walk-forward profile, domain, and scope registries successfully built.")


if __name__ == "__main__":
    main()
