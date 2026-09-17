# -*- coding: utf-8 -*-
"""Phase 148: Run Stress Testing Health Check Script.

Performs health check validation for Phase 148 contract components.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_testing_health import (
    check_stress_testing_health,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_stress_testing_profile()

    df_health, s_health = check_stress_testing_health(profile)
    data_lake.save_stress_testing_health_check(df_health, s_health)

    print("=" * 70)
    print("PHASE 148: STRESS TESTING HEALTH CHECK REPORT")
    print("=" * 70)
    print(f"Overall Status: {s_health.get('overall_status')}")
    print(f"Total Checks  : {s_health.get('total_checks')}")
    print(f"Passed Checks : {s_health.get('passed_checks')}")
    print(f"Failed Checks : {s_health.get('failed_checks')}")
    print(f"All Passed    : {s_health.get('all_passed')}")
    print("=" * 70)

    for _, row in df_health.iterrows():
        print(f"[{row['status']}] {row['component']}: {row['details']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
