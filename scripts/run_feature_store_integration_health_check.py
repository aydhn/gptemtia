"""Phase 124: Run Health Check Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_feature_store_integration.feature_store_integration_config import (
    get_default_feature_store_integration_profile,
)
from advanced_feature_store_integration.feature_store_integration_health import (
    build_feature_store_integration_health_check,
)
from advanced_feature_store_integration.feature_store_integration_report_builder import (
    build_feature_store_health_markdown_report,
)


def main():
    data_lake = DataLake()
    profile = get_default_feature_store_integration_profile()

    df_hlth, s_hlth = build_feature_store_integration_health_check(Path("."), profile)
    data_lake.save_feature_store_integration_health_check(df_hlth, s_hlth)

    md_report = build_feature_store_health_markdown_report(s_hlth, df_hlth)
    reports_dir = Path("reports/output/advanced_feature_store_integration")
    reports_dir.mkdir(parents=True, exist_ok=True)
    with open(reports_dir / "feature_store_health.md", "w", encoding="utf-8") as f:
        f.write(md_report)

    print("=" * 70)
    print("PHASE 124: HEALTH CHECK")
    print("=" * 70)
    print(f"Health Status : {s_hlth['status']}")
    print(f"Total Checks  : {s_hlth['total_checks']}")
    print(f"Passed Checks : {s_hlth['passed_checks']}")
    print(f"Failed Checks : {s_hlth['failed_checks']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
