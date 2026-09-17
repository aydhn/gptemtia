# -*- coding: utf-8 -*-
"""Phase 152: Run Backtest Acceptance Health Check Script.

Runs system health checks across all Phase 146-152 packages and directories.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_backtest_acceptance.backtest_acceptance_config import (
    get_default_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.backtest_acceptance_health import (
    build_backtest_acceptance_health_check,
)
from advanced_backtest_acceptance.backtest_acceptance_report_builder import (
    build_boundary_markdown_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    project_root = Path(__file__).resolve().parent.parent
    profile = get_default_backtest_acceptance_profile()

    df_hlt, s_hlt = build_backtest_acceptance_health_check(project_root, profile)
    data_lake.save_backtest_acceptance_health_check(df_hlt, s_hlt)

    out_dir = Path("reports/output/advanced_backtest_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)

    md = build_boundary_markdown_report(s_hlt, df_hlt)
    with open(out_dir / "health_check.md", "w", encoding="utf-8") as f:
        f.write(md)

    print("=" * 70)
    print("PHASE 152: BACKTEST ACCEPTANCE HEALTH CHECK")
    print("=" * 70)
    print(f"Total Components Checked : {s_hlt['total_components']}")
    print(f"Healthy Components       : {s_hlt['healthy_components']}")
    print(f"All Healthy              : {s_hlt['all_healthy']}")
    print(f"Status                   : {s_hlt['status']}")
    print(f"Non-Signal               : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
