"""Phase 123: Run Feature Drift and Stability Diagnostics Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_feature_quality_drift.feature_quality_drift_config import get_default_feature_quality_drift_profile
from advanced_feature_quality_drift.feature_quality_drift_pipeline import FeatureQualityDriftPipeline
from advanced_feature_quality_drift.feature_quality_drift_report_builder import build_distribution_drift_markdown_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_feature_quality_drift_profile()
    pipeline = FeatureQualityDriftPipeline(data_lake, settings, Path("."), profile)

    tables, summaries = pipeline.build_drift_diagnostics(save=True)

    md_drift = build_distribution_drift_markdown_report(summaries["distribution_drift"], tables["distribution_drift"])

    reports_dir = Path("reports/output/advanced_feature_quality_drift")
    reports_dir.mkdir(parents=True, exist_ok=True)
    with open(reports_dir / "feature_distribution_drift.md", "w", encoding="utf-8") as f:
        f.write(md_drift)

    print("=" * 70)
    print("PHASE 123: FEATURE DISTRIBUTION DRIFT & ROLLING STABILITY")
    print("=" * 70)
    s_drift = summaries["distribution_drift"]
    s_stab = summaries["rolling_stability"]
    print(f"Features Compared (Drift)   : {s_drift['total_features_compared']}")
    print(f"Critical Drift Detected     : {s_drift['critical_drift_count']}")
    print(f"Warning Drift Detected      : {s_drift['warning_drift_count']}")
    print(f"Stable Features             : {s_drift['stable_features_count']}")
    print(f"Mean Rolling Stability Score: {s_stab['mean_stability_score']}")
    print(f"Unstable Features Count     : {s_stab['unstable_features_count']}")
    print(f"Overall Drift Status        : {s_drift['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
