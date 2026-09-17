# -*- coding: utf-8 -*-
"""Phase 150: Run Backtest Governance Health Check Script.

Executes health checks across dependent modules, storage layers, and settings.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_governance_health import (
    build_backtest_governance_health_check,
)
from advanced_backtest_governance.backtest_governance_report_builder import (
    build_backtest_governance_health_markdown_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_backtest_governance_profile()

    df_hlth, s_hlth = build_backtest_governance_health_check(profile=profile)

    data_lake.save_backtest_governance_health_check(df_hlth, s_hlth)

    out_dir = Path("reports/output/advanced_backtest_governance")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "health_check.md", "w", encoding="utf-8") as f:
        f.write(build_backtest_governance_health_markdown_report(s_hlth))

    print("=" * 70)
    print("PHASE 150: BACKTEST GOVERNANCE HEALTH CHECK REPORT")
    print("=" * 70)
    print(df_hlth.to_string(index=False))
    print("-" * 70)
    print(f"Overall Health: {s_hlth.get('overall_health')}")
    print(f"Passed Checks : {s_hlth.get('passed_checks')} / {s_hlth.get('total_checks')}")
    print("=" * 70)


if __name__ == "__main__":
    main()
