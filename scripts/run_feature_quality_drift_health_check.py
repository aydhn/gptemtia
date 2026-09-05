"""Phase 123: Run Feature Quality and Drift Health Check Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_feature_quality_drift.feature_quality_drift_config import get_default_feature_quality_drift_profile
from advanced_feature_quality_drift.feature_quality_drift_health import build_feature_quality_drift_health_check
from advanced_feature_quality_drift.feature_quality_drift_report_builder import build_quality_drift_health_markdown_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_feature_quality_drift_profile()

    df_hlth, s_hlth = build_feature_quality_drift_health_check(Path("."), profile)
    data_lake.save_feature_quality_drift_health_check(df_hlth, s_hlth)

    md_hlth = build_quality_drift_health_markdown_report(s_hlth, df_hlth)

    reports_dir = Path("reports/output/advanced_feature_quality_drift")
    reports_dir.mkdir(parents=True, exist_ok=True)
    with open(reports_dir / "quality_drift_health.md", "w", encoding="utf-8") as f:
        f.write(md_hlth)

    print("=" * 70)
    print("PHASE 123: FEATURE QUALITY & DRIFT HEALTH CHECK")
    print("=" * 70)
    print(f"Health Status         : {s_hlth['status']}")
    print(f"Total Components      : {s_hlth['total_components']}")
    print(f"Healthy Components    : {s_hlth['healthy_components']}")
    print(f"Unhealthy Components  : {s_hlth['unhealthy_components']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
