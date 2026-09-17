# -*- coding: utf-8 -*-
"""Phase 158: Run Full-System Integration Health Check Script.

Scans project files and validates module presence.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.full_system_integration_health import (
    build_full_system_integration_health_check,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    project_root = Path(__file__).resolve().parent.parent
    profile = get_default_full_system_integration_profile()

    df_hlth, s_hlth = build_full_system_integration_health_check(project_root, profile)
    data_lake.save_full_system_integration_health_check(df_hlth, s_hlth)

    print("=" * 70)
    print("PHASE 158: FULL-SYSTEM INTEGRATION HEALTH CHECK")
    print("=" * 70)
    print(f"Total Components Checked : {s_hlth['total_checked']}")
    print(f"Healthy Components       : {s_hlth['healthy_count']}")
    print(f"Missing Components       : {s_hlth['missing_count']}")
    print(f"System Health Status     : {s_hlth['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
