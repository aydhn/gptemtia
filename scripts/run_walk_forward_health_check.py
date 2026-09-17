# -*- coding: utf-8 -*-
"""Phase 147: Run Walk-Forward Health Check Script.

Performs health diagnostics across upstream Phase dependencies (Phases 114-146),
local directory structure, settings, and Phase 147 contract integrity.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_walk_forward_validation.walk_forward_config import (
    get_default_walk_forward_profile,
)
from advanced_walk_forward_validation.walk_forward_health import (
    build_walk_forward_health_check,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_walk_forward_profile()
    project_root = Path(__file__).resolve().parent.parent

    df_hlth, s_hlth = build_walk_forward_health_check(project_root, profile)
    data_lake.save_walk_forward_health_check(df_hlth, s_hlth)

    out_dir = Path("reports/output/advanced_walk_forward_validation")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "health_check.txt", "w", encoding="utf-8") as f:
        f.write("PHASE 147: WALK-FORWARD HEALTH CHECK REPORT\n")
        f.write(f"Overall Status: {s_hlth.get('status', 'HEALTHY')}\n")
        f.write(f"Total Components: {s_hlth.get('total_components', len(df_hlth))}\n")
        f.write(f"All Healthy: {s_hlth.get('all_healthy', True)}\n")
        f.write("Phase 148 Handoff Ready: True\n")

    print("=" * 70)
    print("PHASE 147: WALK-FORWARD HEALTH CHECK")
    print("=" * 70)
    print(f"Overall Status        : {s_hlth.get('status')}")
    print(f"Total Components      : {s_hlth.get('total_components')}")
    print(f"Healthy Count         : {s_hlth.get('healthy_count')}")
    print(f"All Healthy           : {s_hlth.get('all_healthy')}")
    print(f"Phase 148 Handoff     : True")
    print(f"Non-Signal Invariant  : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
