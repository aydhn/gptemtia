"""Phase 128: Run Regime Rule-Free Health Check Script.

Executes subsystem health checks and writes health diagnostic reports.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_rule_free.regime_rule_free_config import (
    get_default_regime_rule_free_profile,
)
from advanced_regime_rule_free.regime_rule_free_health import (
    build_regime_rule_free_health_check,
)


def main():
    data_lake = DataLake()
    project_root = Path(__file__).resolve().parent.parent
    profile = get_default_regime_rule_free_profile()

    df_health, s_health = build_regime_rule_free_health_check(project_root, profile)
    data_lake.save_regime_rule_free_health_check(df_health, s_health)

    out_dir = Path("reports/output/advanced_regime_rule_free")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "health_check.txt", "w", encoding="utf-8") as f:
        f.write(f"Health Status: {s_health['health_status']}\n")
        f.write(f"Passed Checks: {s_health['passed_checks']}/{s_health['total_checks']}\n")

    print("=" * 70)
    print("PHASE 128: HEALTH CHECK")
    print("=" * 70)
    print(f"Health Status : {s_health['health_status']}")
    print(f"Passed Checks : {s_health['passed_checks']}/{s_health['total_checks']}")
    print(f"Failed Checks : {s_health['failed_checks']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
