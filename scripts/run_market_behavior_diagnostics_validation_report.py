"""Phase 129: Run Market Behavior Diagnostics Validation Report Script.

Validates safety boundaries, lookahead guard, non-signal invariants, and generates validation report.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    get_default_market_behavior_diagnostics_profile,
)
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_validation import (
    run_market_behavior_diagnostics_validation_report,
)
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_safety_boundary import (
    build_market_behavior_diagnostics_safety_boundary,
)
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_report_builder import (
    build_market_behavior_diagnostics_validation_markdown_report,
    build_market_behavior_diagnostics_safety_markdown_report,
)
from reports.report_builder import (
    build_market_behavior_diagnostics_validation_text_report,
    build_market_behavior_diagnostics_safety_text_report,
)


def main():
    data_lake = DataLake()
    profile = get_default_market_behavior_diagnostics_profile()

    df_val, s_val = run_market_behavior_diagnostics_validation_report(profile)
    df_saf, s_saf = build_market_behavior_diagnostics_safety_boundary(profile)

    data_lake.save_market_behavior_diagnostics_validation_report(df_val, s_val)
    data_lake.save_market_behavior_diagnostics_safety_boundary(df_saf, s_saf)

    md_val = build_market_behavior_diagnostics_validation_markdown_report(s_val, df_val)
    txt_val = build_market_behavior_diagnostics_validation_text_report(s_val, df_val)

    md_saf = build_market_behavior_diagnostics_safety_markdown_report(s_saf, df_saf)
    txt_saf = build_market_behavior_diagnostics_safety_text_report(s_saf, df_saf)

    out_dir = Path("reports/output/advanced_market_behavior_diagnostics")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "validation_report.md", "w", encoding="utf-8") as f:
        f.write(md_val)
    with open(out_dir / "validation_report.txt", "w", encoding="utf-8") as f:
        f.write(txt_val)
    with open(out_dir / "safety_boundary.md", "w", encoding="utf-8") as f:
        f.write(md_saf)
    with open(out_dir / "safety_boundary.txt", "w", encoding="utf-8") as f:
        f.write(txt_saf)

    print("=" * 70)
    print("PHASE 129: MARKET BEHAVIOR DIAGNOSTICS VALIDATION & SAFETY REPORT")
    print("=" * 70)
    print(f"Validation Status : {s_val['validation_status']}")
    print(f"Total Checks      : {s_val['total_checks']}")
    print(f"Passed Checks     : {s_val['passed_checks']}")
    print(f"Safety Status     : {s_saf['safety_status']}")
    print(f"NO-GO Rules       : {s_saf['no_go_count']}")
    print(f"SAFE-GO Rules     : {s_saf['safe_go_count']}")
    print(f"Non-Signal Mandate: True")
    print("=" * 70)


if __name__ == "__main__":
    main()
