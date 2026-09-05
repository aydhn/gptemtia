"""Phase 129: Run Market Behavior Diagnostics Health Check Script.

Performs health check on all Phase 129 market behavior diagnostics artifacts.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    get_default_market_behavior_diagnostics_profile,
)
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_health import (
    run_market_behavior_diagnostics_health_check,
)
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_report_builder import (
    build_market_behavior_diagnostics_health_markdown_report,
)
from reports.report_builder import build_market_behavior_diagnostics_health_text_report


def main():
    data_lake = DataLake()
    profile = get_default_market_behavior_diagnostics_profile()

    df_health, s_health = run_market_behavior_diagnostics_health_check(profile)
    data_lake.save_market_behavior_diagnostics_health_check(df_health, s_health)

    md = build_market_behavior_diagnostics_health_markdown_report(s_health, df_health)
    txt = build_market_behavior_diagnostics_health_text_report(s_health, df_health)

    out_dir = Path("reports/output/advanced_market_behavior_diagnostics")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "health_check.md", "w", encoding="utf-8") as f:
        f.write(md)
    with open(out_dir / "health_check.txt", "w", encoding="utf-8") as f:
        f.write(txt)

    print("=" * 70)
    print("PHASE 129: MARKET BEHAVIOR DIAGNOSTICS HEALTH CHECK")
    print("=" * 70)
    print(f"Health Status      : {s_health.get('health_status', 'HEALTHY')}")
    print(f"Total Checks       : {s_health.get('total_checks', len(df_health))}")
    print(f"Passed Checks      : {s_health.get('healthy_count', len(df_health))}")
    print(f"Failed Checks      : {s_health.get('failed_checks', 0)}")
    print(f"Non-Signal         : {s_health.get('non_signal', True)}")
    print(f"Zero Execution     : {s_health.get('zero_execution', True)}")
    print("-" * 70)
    for _, row in df_health.iterrows():
        col_name = row.get("component_name", row.get("check_name", "check"))
        print(f"[{row['status']}] {col_name:<30} : {row['description']}")
    print("=" * 70)



if __name__ == "__main__":
    main()
