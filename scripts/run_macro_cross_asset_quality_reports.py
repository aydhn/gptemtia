"""Phase 123: Run Macro and Cross-Asset Quality Reports Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_feature_quality_drift.feature_quality_drift_config import get_default_feature_quality_drift_profile
from advanced_feature_quality_drift.feature_quality_drift_pipeline import FeatureQualityDriftPipeline
from advanced_feature_quality_drift.feature_quality_drift_report_builder import build_macro_cross_asset_quality_markdown_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_feature_quality_drift_profile()
    pipeline = FeatureQualityDriftPipeline(data_lake, settings, Path("."), profile)

    tables, summaries = pipeline.build_macro_cross_asset_quality(save=True)

    md_mcn = build_macro_cross_asset_quality_markdown_report(summaries["macro_calendar_news_quality"], tables["macro_calendar_news_quality"])

    reports_dir = Path("reports/output/advanced_feature_quality_drift")
    reports_dir.mkdir(parents=True, exist_ok=True)
    with open(reports_dir / "macro_calendar_news_quality.md", "w", encoding="utf-8") as f:
        f.write(md_mcn)

    print("=" * 70)
    print("PHASE 123: MACRO, CALENDAR, NEWS & CROSS-ASSET FEATURE QUALITY")
    print("=" * 70)
    s_mcn = summaries["macro_calendar_news_quality"]
    s_ca = summaries["cross_asset_feature_quality"]
    print(f"Macro/Calendar/News Checks : {s_mcn['passed_checks']}/{s_mcn['total_checks']} (Passed)")
    print(f"Metadata-Only Boundary     : {s_mcn['metadata_only_boundary_compliant']}")
    print(f"Cross-Asset Quality Checks : {s_ca['passed_checks']}/{s_ca['total_checks']} (Passed)")
    print("=" * 70)


if __name__ == "__main__":
    main()
