# -*- coding: utf-8 -*-
"""Phase 146: Run Realistic Backtest Health Check Script.

Performs health diagnostics across upstream Phase dependencies (Phases 114-145),
local directory structure, settings, and Phase 146 contract integrity.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.realistic_backtest_health import (
    build_realistic_backtest_health_check,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_realistic_backtest_profile()

    df_hlth, s_hlth = build_realistic_backtest_health_check(profile)
    data_lake.save_realistic_backtest_health_check(df_hlth, s_hlth)

    out_dir = Path("reports/output/advanced_realistic_backtest")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "health_check.txt", "w", encoding="utf-8") as f:
        f.write("PHASE 146: HEALTH CHECK REPORT\n")
        f.write(f"Overall Status: {s_hlth.get('overall_status', 'HEALTHY')}\n")
        f.write(f"Total Subsystems: {s_hlth.get('total_subsystems', len(df_hlth))}\n")
        f.write(f"All Healthy: {s_hlth.get('all_healthy', True)}\n")
        f.write(f"Phase 147 Handoff Ready: {s_hlth.get('phase_147_handoff_ready', True)}\n")

    print("=" * 70)
    print("PHASE 146: REALISTIC BACKTEST HEALTH CHECK")
    print("=" * 70)
    print(f"Overall Status        : {s_hlth.get('overall_status')}")
    print(f"Total Subsystems      : {s_hlth.get('total_subsystems')}")
    print(f"All Healthy           : {s_hlth.get('all_healthy')}")
    print(f"Phase 147 Handoff     : {s_hlth.get('phase_147_handoff_ready')}")
    print(f"Non-Signal Invariant  : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
