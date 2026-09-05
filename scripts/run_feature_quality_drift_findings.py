"""Phase 123: Run Feature Quality and Drift Findings, Scoring and Manifest Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_feature_quality_drift.feature_quality_drift_config import get_default_feature_quality_drift_profile
from advanced_feature_quality_drift.feature_quality_drift_pipeline import FeatureQualityDriftPipeline
from advanced_feature_quality_drift.feature_quality_drift_report_builder import (
    build_quality_findings_markdown_report,
    build_drift_findings_markdown_report,
    build_quality_drift_manifest_markdown_report,
    build_phase_124_handoff_markdown_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_feature_quality_drift_profile()
    pipeline = FeatureQualityDriftPipeline(data_lake, settings, Path("."), profile)

    tables, summaries = pipeline.build_findings_scoring_manifest(save=True)
    h_tables, h_summaries = pipeline.build_health_validation_safety_handoff(save=True)

    md_qf = build_quality_findings_markdown_report(summaries["quality_findings"], tables["quality_findings"])
    md_df = build_drift_findings_markdown_report(summaries["drift_findings"], tables["drift_findings"])
    md_man = build_quality_drift_manifest_markdown_report(summaries["manifest"], tables["manifest"])
    md_hand = build_phase_124_handoff_markdown_report(h_summaries["phase_124_handoff"], h_tables["phase_124_handoff"])

    reports_dir = Path("reports/output/advanced_feature_quality_drift")
    reports_dir.mkdir(parents=True, exist_ok=True)
    with open(reports_dir / "quality_findings.md", "w", encoding="utf-8") as f:
        f.write(md_qf)
    with open(reports_dir / "drift_findings.md", "w", encoding="utf-8") as f:
        f.write(md_df)
    with open(reports_dir / "quality_drift_manifest.md", "w", encoding="utf-8") as f:
        f.write(md_man)
    with open(reports_dir / "phase_124_handoff.md", "w", encoding="utf-8") as f:
        f.write(md_hand)

    print("=" * 70)
    print("PHASE 123: FINDINGS, SCORING, MANIFEST & PHASE 124 HANDOFF")
    print("=" * 70)
    s_qf = summaries["quality_findings"]
    s_df = summaries["drift_findings"]
    s_qs = summaries["quality_score"]
    s_ds = summaries["drift_score"]
    s_man = summaries["manifest"]
    s_hand = h_summaries["phase_124_handoff"]
    print(f"Total Quality Findings     : {s_qf['total_findings']}")
    print(f"Total Drift Findings       : {s_df['total_drift_findings']}")
    print(f"Overall Quality Score      : {s_qs['overall_quality_score']}")
    print(f"Overall Drift Score        : {s_ds['overall_drift_score']}")
    print(f"Manifest Feature Count     : {s_man['total_features']}")
    print(f"Phase 124 Handoff Status   : {s_hand['handoff_status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
