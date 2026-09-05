"""Phase 123: Run Factor Quality and Drift Reports Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_feature_quality_drift.feature_quality_drift_config import get_default_feature_quality_drift_profile
from advanced_feature_quality_drift.feature_quality_drift_pipeline import FeatureQualityDriftPipeline
from advanced_feature_quality_drift.feature_quality_drift_report_builder import build_factor_quality_markdown_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_feature_quality_drift_profile()
    pipeline = FeatureQualityDriftPipeline(data_lake, settings, Path("."), profile)

    tables, summaries = pipeline.build_factor_quality_drift(save=True)

    md_fq = build_factor_quality_markdown_report(summaries["factor_family_quality"], tables["factor_family_quality"])

    reports_dir = Path("reports/output/advanced_feature_quality_drift")
    reports_dir.mkdir(parents=True, exist_ok=True)
    with open(reports_dir / "factor_family_quality.md", "w", encoding="utf-8") as f:
        f.write(md_fq)

    print("=" * 70)
    print("PHASE 123: FACTOR FAMILY QUALITY, DRIFT & AVAILABILITY")
    print("=" * 70)
    s_fq = summaries["factor_family_quality"]
    s_fd = summaries["factor_family_drift"]
    s_fa = summaries["factor_availability"]
    s_dep = summaries["factor_dependency_quality"]
    print(f"Total Factor Families      : {s_fq['total_families']}")
    print(f"Mean Family Quality Score  : {s_fq['mean_family_quality_score']}")
    print(f"Mean Family Drift Score    : {s_fd['mean_family_drift_score']}")
    print(f"Fully Available Families   : {s_fa['fully_available_families']}")
    print(f"Passed Dependencies        : {s_dep['passed_dependencies']}/{s_dep['total_dependencies']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
