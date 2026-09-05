"""Phase 123: Run Feature Quality Diagnostics Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_feature_quality_drift.feature_quality_drift_config import get_default_feature_quality_drift_profile
from advanced_feature_quality_drift.feature_quality_drift_pipeline import FeatureQualityDriftPipeline
from advanced_feature_quality_drift.feature_quality_drift_report_builder import build_missingness_markdown_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_feature_quality_drift_profile()
    pipeline = FeatureQualityDriftPipeline(data_lake, settings, Path("."), profile)

    tables, summaries = pipeline.build_quality_diagnostics(save=True)

    md_missing = build_missingness_markdown_report(summaries["missingness"], tables["missingness"])

    reports_dir = Path("reports/output/advanced_feature_quality_drift")
    reports_dir.mkdir(parents=True, exist_ok=True)
    with open(reports_dir / "feature_missingness_diagnostics.md", "w", encoding="utf-8") as f:
        f.write(md_missing)

    print("=" * 70)
    print("PHASE 123: FEATURE QUALITY DIAGNOSTICS SUITE")
    print("=" * 70)
    for name, s in summaries.items():
        st = s.get("status", "PASS")
        cnt = s.get("total_features", s.get("total_features_checked", 0))
        rev = s.get("manual_review_required", False)
        print(f"Subsystem [{name:<22}]: features={cnt:<3} status={st:<28} review={rev}")
    print("=" * 70)


if __name__ == "__main__":
    main()
