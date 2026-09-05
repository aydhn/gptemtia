"""Phase 123: Run Feature Quality and Drift Validation & Safety Report Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_feature_quality_drift.feature_quality_drift_config import get_default_feature_quality_drift_profile
from advanced_feature_quality_drift.feature_quality_drift_validation import build_feature_quality_drift_validation_report
from advanced_feature_quality_drift.feature_quality_drift_safety_boundary import build_feature_quality_drift_safety_boundary
from advanced_feature_quality_drift.feature_quality_drift_report_builder import (
    build_quality_drift_safety_markdown_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_feature_quality_drift_profile()

    df_val, s_val = build_feature_quality_drift_validation_report(None, profile)
    df_safe, s_safe = build_feature_quality_drift_safety_boundary(profile)

    data_lake.save_feature_quality_drift_validation_report(df_val, s_val)
    data_lake.save_feature_quality_drift_safety_boundary(df_safe, s_safe)

    md_safe = build_quality_drift_safety_markdown_report(s_safe, df_safe)

    reports_dir = Path("reports/output/advanced_feature_quality_drift")
    reports_dir.mkdir(parents=True, exist_ok=True)
    with open(reports_dir / "quality_drift_safety.md", "w", encoding="utf-8") as f:
        f.write(md_safe)

    print("=" * 70)
    print("PHASE 123: FEATURE QUALITY & DRIFT VALIDATION AND SAFETY BOUNDARY")
    print("=" * 70)
    print(f"Validation Status      : {s_val['status']}")
    print(f"Passed Checks          : {s_val['passed_checks']}/{s_val['total_validation_checks']}")
    print(f"Safety Status          : {s_safe['safety_status']}")
    print(f"NO-GO Rules Enforced   : {s_safe['no_go_count']}")
    print(f"SAFE-GO Principles     : {s_safe['safe_go_count']}")
    print(f"Non-Signal Mandate     : {s_safe['non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
