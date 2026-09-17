# -*- coding: utf-8 -*-
"""Phase 148: Run Stress Dependencies and Guards Script.

Builds and persists stress no-lookahead guards, scenario leakage guards,
and forbidden column policies.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_no_lookahead_guards import (
    build_stress_no_lookahead_guard_registry,
)
from advanced_stress_testing.stress_scenario_leakage_guards import (
    build_stress_scenario_leakage_guard_registry,
)
from advanced_stress_testing.stress_forbidden_column_policies import (
    build_stress_forbidden_column_policy_registry,
)
from advanced_stress_testing.stress_testing_report_builder import (
    build_stress_guard_markdown_report,
)
from reports.report_builder import build_stress_guard_text_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_stress_testing_profile()

    df_nl, s_nl = build_stress_no_lookahead_guard_registry(profile)
    df_leak, s_leak = build_stress_scenario_leakage_guard_registry(profile)
    df_forb, s_forb = build_stress_forbidden_column_policy_registry(profile)

    data_lake.save_stress_no_lookahead_guard_registry(df_nl, s_nl)
    data_lake.save_stress_scenario_leakage_guard_registry(df_leak, s_leak)
    data_lake.save_stress_forbidden_column_policy_registry(df_forb, s_forb)

    summary = {
        "no_lookahead_active": True,
        "scenario_leakage_active": True,
        "forbidden_columns_active": True,
        "total_guards": len(df_nl) + len(df_leak) + len(df_forb),
    }

    md_report = build_stress_guard_markdown_report(summary, df_nl)
    txt_report = build_stress_guard_text_report(summary, df_nl)

    out_dir = Path("reports/output/advanced_stress_testing")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "guards.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "guards.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("Stress dependency and bias guards successfully built and persisted.")


if __name__ == "__main__":
    main()
