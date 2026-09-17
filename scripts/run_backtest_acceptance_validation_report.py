# -*- coding: utf-8 -*-
"""Phase 152: Run Backtest Acceptance Validation & Safety Report Script.

Builds validation and safety boundary reports and saves them to DataLake.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_backtest_acceptance.backtest_acceptance_config import (
    get_default_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.backtest_acceptance_validation import (
    build_backtest_acceptance_validation_report,
)
from advanced_backtest_acceptance.backtest_acceptance_safety_boundary import (
    build_backtest_acceptance_safety_boundary,
)
from advanced_backtest_acceptance.backtest_acceptance_report_builder import (
    build_backtest_acceptance_validation_markdown_report,
    build_backtest_acceptance_safety_markdown_report,
)
from reports.report_builder import (
    build_backtest_acceptance_validation_text_report,
    build_backtest_acceptance_safety_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_backtest_acceptance_profile()

    df_val, s_val = build_backtest_acceptance_validation_report({}, profile)
    df_sft, s_sft = build_backtest_acceptance_safety_boundary(profile)

    data_lake.save_backtest_acceptance_validation_report(df_val, s_val)
    data_lake.save_backtest_acceptance_safety_boundary(df_sft, s_sft)

    out_dir = Path("reports/output/advanced_backtest_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)

    with open(out_dir / "validation_report.md", "w", encoding="utf-8") as f:
        f.write(build_backtest_acceptance_validation_markdown_report(s_val, df_val))
    with open(out_dir / "validation_report.txt", "w", encoding="utf-8") as f:
        f.write(build_backtest_acceptance_validation_text_report(s_val, df_val))

    with open(out_dir / "safety_boundary.md", "w", encoding="utf-8") as f:
        f.write(build_backtest_acceptance_safety_markdown_report(s_sft, df_sft))
    with open(out_dir / "safety_boundary.txt", "w", encoding="utf-8") as f:
        f.write(build_backtest_acceptance_safety_text_report(s_sft, df_sft))

    print("=" * 70)
    print("PHASE 152: VALIDATION & SAFETY REPORT")
    print("=" * 70)
    print(f"Validation Status   : {s_val['validation_status']}")
    print(f"Total Checks        : {s_val['total_checks']} ({s_val['passed_checks']} Passed)")
    print(f"All Checks Passed   : {s_val['all_passed']}")
    print(f"Safety Status       : {s_sft['safety_status']}")
    print(f"NO-GO Rules Enforced: {s_sft['no_go_count']}")
    print(f"SAFE-GO Rules Active: {s_sft['safe_go_count']}")
    print(f"Non-Signal          : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
