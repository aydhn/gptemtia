# -*- coding: utf-8 -*-
"""Phase 157: Run Portfolio Acceptance Health Check Script.

Verifies and persists health status of all required portfolio and governance subsystems.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_default_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.portfolio_acceptance_health import (
    build_portfolio_acceptance_health_check,
)
from advanced_portfolio_acceptance.portfolio_acceptance_report_builder import (
    build_portfolio_blocker_gap_warning_markdown_report,
)
from reports.report_builder import (
    build_portfolio_acceptance_safety_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_portfolio_acceptance_profile()

    df_hlth, s_hlth = build_portfolio_acceptance_health_check(Path(__file__).resolve().parent.parent, profile)
    data_lake.save_portfolio_acceptance_health_check(df_hlth, s_hlth)

    out_dir = Path("reports/output/advanced_portfolio_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)

    with open(out_dir / "health_check.md", "w", encoding="utf-8") as f:
        f.write(build_portfolio_blocker_gap_warning_markdown_report(s_hlth, df_hlth))

    print("=" * 70)
    print("PHASE 157: PORTFOLIO ACCEPTANCE HEALTH CHECK")
    print("=" * 70)
    print(f"Total Checks  : {s_hlth['total_checks']}")
    print(f"Passed Checks : {s_hlth['passed_checks']}")
    print(f"Failed Checks : {s_hlth['failed_checks']}")
    print(f"All Passed    : {s_hlth['all_passed']}")
    print(f"Health Status : {s_hlth['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
