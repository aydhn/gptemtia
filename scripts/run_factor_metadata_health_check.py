"""Phase 122: Run Factor Metadata Health Check Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_factor_metadata.factor_metadata_config import get_default_factor_metadata_profile
from advanced_factor_metadata.factor_metadata_health import build_factor_metadata_health_check
from advanced_factor_metadata.factor_metadata_report_builder import build_factor_health_markdown_report
from reports.report_builder import build_factor_safety_text_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    project_root = Path(__file__).resolve().parent.parent
    profile = get_default_factor_metadata_profile()

    df_health, s_health = build_factor_metadata_health_check(project_root, profile)
    data_lake.save_factor_health_check(df_health, s_health)

    md_report = build_factor_health_markdown_report(s_health, df_health)
    reports_dir = Path("reports/output/advanced_factor_metadata")
    reports_dir.mkdir(parents=True, exist_ok=True)
    with open(reports_dir / "factor_health_check.md", "w", encoding="utf-8") as f:
        f.write(md_report)

    print("=" * 70)
    print("PHASE 122: FACTOR METADATA HEALTH CHECK")
    print("=" * 70)
    print(f"Health Status      : {s_health['health_status']}")
    print(f"Total Checks       : {s_health['total_checks']}")
    print(f"Passed Checks      : {s_health['passed_checks']}")
    print(f"Failed Checks      : {s_health['failed_checks']}")
    print(f"Prerequisites Ready: {s_health['prerequisites_ready']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
