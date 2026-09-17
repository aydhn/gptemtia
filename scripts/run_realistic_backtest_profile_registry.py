# -*- coding: utf-8 -*-
"""Phase 146: Run Realistic Backtest Profile Registry Script.

Builds backtest profile registry, domain registry, scope registry, and execution assumptions,
saving them to DataLake and writing markdown/text reports.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.realistic_backtest_profile_registry import (
    build_realistic_backtest_profile_registry,
)
from advanced_realistic_backtest.realistic_backtest_domain_registry import (
    build_realistic_backtest_domain_registry,
)
from advanced_realistic_backtest.backtest_scope_registry import (
    build_backtest_scope_registry,
)
from advanced_realistic_backtest.realistic_execution_assumptions import (
    build_realistic_execution_assumption_registry,
)
from advanced_realistic_backtest.realistic_backtest_report_builder import (
    build_realistic_backtest_profile_markdown_report,
)
from reports.report_builder import build_realistic_backtest_profile_text_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_realistic_backtest_profile()

    df_prof, s_prof = build_realistic_backtest_profile_registry(profile)
    df_dom, s_dom = build_realistic_backtest_domain_registry(profile)
    df_scp, s_scp = build_backtest_scope_registry(profile)
    df_asm, s_asm = build_realistic_execution_assumption_registry(profile)

    data_lake.save_realistic_backtest_profile_registry(df_prof, s_prof)
    data_lake.save_realistic_backtest_domain_registry(df_dom, s_dom)
    data_lake.save_backtest_scope_registry(df_scp, s_scp)
    data_lake.save_realistic_execution_assumptions(df_asm, s_asm)

    md_report = build_realistic_backtest_profile_markdown_report(s_prof, df_prof)
    txt_report = build_realistic_backtest_profile_text_report(s_prof, df_prof)

    out_dir = Path("reports/output/advanced_realistic_backtest")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "profiles.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "profiles.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("=" * 70)
    print("PHASE 146: REALISTIC BACKTEST PROFILES & DOMAINS")
    print("=" * 70)
    print(f"Active Profile : {s_prof.get('active_profile')}")
    print(f"Total Profiles : {s_prof.get('total_profiles')}")
    print(f"Total Domains  : {s_dom.get('total_domains')}")
    print(f"Scope Items    : {s_scp.get('total_scope_items')}")
    print(f"Assumptions    : {s_asm.get('total_assumptions')}")
    print(f"Current Phase  : {s_prof.get('current_phase')}")
    print(f"Target Phase   : {s_prof.get('target_final_phase')}")
    print(f"Next Phase     : {s_prof.get('next_phase')}")
    print(f"Non-Signal     : {s_prof.get('non_signal')}")
    print("=" * 70)


if __name__ == "__main__":
    main()
