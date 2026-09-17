# -*- coding: utf-8 -*-
"""Phase 148: Run Stress Testing Profile Registry Script.

Builds and persists stress testing profile, domain, and scope registries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_testing_profile_registry import (
    build_stress_testing_profile_registry,
)
from advanced_stress_testing.stress_testing_domain_registry import (
    build_stress_testing_domain_registry,
)
from advanced_stress_testing.stress_testing_scope_registry import (
    build_stress_testing_scope_registry,
)
from advanced_stress_testing.stress_testing_report_builder import (
    build_stress_testing_profile_markdown_report,
)
from reports.report_builder import build_stress_testing_profile_text_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_stress_testing_profile()

    df_prof, s_prof = build_stress_testing_profile_registry(profile)
    df_dom, s_dom = build_stress_testing_domain_registry(profile)
    df_scp, s_scp = build_stress_testing_scope_registry(profile)

    data_lake.save_stress_testing_profile_registry(df_prof, s_prof)
    data_lake.save_stress_testing_domain_registry(df_dom, s_dom)
    data_lake.save_stress_testing_scope_registry(df_scp, s_scp)

    md_report = build_stress_testing_profile_markdown_report(s_prof, df_prof)
    txt_report = build_stress_testing_profile_text_report(s_prof, df_prof)

    out_dir = Path("reports/output/advanced_stress_testing")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "profiles.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "profiles.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("Stress testing profile, domain, and scope registries successfully built.")


if __name__ == "__main__":
    main()
