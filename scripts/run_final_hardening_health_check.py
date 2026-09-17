# -*- coding: utf-8 -*-
"""Phase 159: Run Final Hardening Health Check Script.

Builds and persists health check artifacts verifying system module availability.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_final_hardening.final_hardening_config import (
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_health import (
    build_final_hardening_health_check,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_final_hardening_profile()

    df_hlth, s_hlth = build_final_hardening_health_check(profile=profile)
    data_lake.save_release_candidate_health_check(df_hlth, s_hlth)

    print("=" * 70)
    print("PHASE 159: FINAL HARDENING HEALTH CHECK")
    print("=" * 70)
    print(f"Passed Checks: {s_hlth['passed_checks']} / {s_hlth['total_checks']}")
    print(f"All Passed: {s_hlth['all_passed']}")
    print(f"Status: {s_hlth['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
