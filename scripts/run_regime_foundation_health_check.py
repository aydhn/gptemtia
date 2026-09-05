"""Phase 126: Run Regime Foundation Health Check Script.

Performs and reports system health status across all components.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_foundation.regime_foundation_config import (
    get_default_regime_foundation_profile,
)
from advanced_regime_foundation.regime_foundation_health import (
    build_regime_foundation_health_check,
)
from advanced_regime_foundation.regime_foundation_report_builder import (
    build_regime_health_markdown_report,
)
from reports.report_builder import build_regime_foundation_text_report


def main():
    data_lake = DataLake()
    profile = get_default_regime_foundation_profile()

    df_health, s_health = build_regime_foundation_health_check(Path(__file__).resolve().parent.parent, profile)
    data_lake.save_regime_foundation_health_check(df_health, s_health)

    md_health = build_regime_health_markdown_report(s_health, df_health)
    txt_health = build_regime_foundation_text_report(s_health, df_health)

    out_dir = Path("reports/output/advanced_regime_foundation")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "regime_foundation_health.md", "w", encoding="utf-8") as f:
        f.write(md_health)
    with open(out_dir / "regime_foundation_health.txt", "w", encoding="utf-8") as f:
        f.write(txt_health)

    print("=" * 70)
    print("PHASE 126: REGIME FOUNDATION HEALTH CHECK")
    print("=" * 70)
    print(f"Health Status  : {s_health['health_status']}")
    print(f"Healthy Checks : {s_health['healthy_checks']}/{s_health['total_checks']}")
    print(f"Unhealthy      : {s_health['unhealthy_checks']}")
    print(f"Non-Signal     : {s_health['non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
