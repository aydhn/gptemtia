# -*- coding: utf-8 -*-
"""Phase 149: Run Monte Carlo Health Check Script.

Audits repository environment, dependent packages, storage, and contract integrity.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_monte_carlo_robustness.monte_carlo_config import (
    get_default_monte_carlo_profile,
)
from advanced_monte_carlo_robustness.monte_carlo_health import (
    build_monte_carlo_health_check,
)


from advanced_monte_carlo_robustness.monte_carlo_report_builder import _df_to_markdown


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_monte_carlo_profile()
    project_root = Path(__file__).resolve().parent.parent

    df_hlth, s_hlth = build_monte_carlo_health_check(project_root, profile)
    data_lake.save_monte_carlo_health_check(df_hlth, s_hlth)

    out_dir = Path("reports/output/advanced_monte_carlo_robustness")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "health_check.md", "w", encoding="utf-8") as f:
        f.write(_df_to_markdown(df_hlth))

    print("=" * 60)
    print("PHASE 149: MONTE CARLO HEALTH CHECK")
    print("=" * 60)
    print(df_hlth.to_string(index=False))
    print("-" * 60)
    print(f"Overall Status : {s_hlth.get('overall_status')}")
    print(f"Passed Checks  : {s_hlth.get('passed_checks')}/{s_hlth.get('total_checks')}")
    print("=" * 60)


if __name__ == "__main__":
    main()
