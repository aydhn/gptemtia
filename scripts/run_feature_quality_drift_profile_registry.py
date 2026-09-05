"""Phase 123: Run Feature Quality and Drift Profile Registry Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_feature_quality_drift.feature_quality_drift_config import get_default_feature_quality_drift_profile
from advanced_feature_quality_drift.feature_quality_drift_profile_registry import build_feature_quality_drift_profile_registry
from advanced_feature_quality_drift.feature_quality_drift_domain_registry import build_feature_quality_drift_domain_registry
from advanced_feature_quality_drift.feature_quality_drift_report_builder import build_feature_quality_drift_profile_markdown_report
from reports.report_builder import build_feature_quality_drift_text_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_feature_quality_drift_profile()

    df_prof, s_prof = build_feature_quality_drift_profile_registry(profile)
    df_dom, s_dom = build_feature_quality_drift_domain_registry(profile)

    data_lake.save_feature_quality_drift_profile_registry(df_prof, s_prof)
    data_lake.save_feature_quality_drift_domain_registry(df_dom, s_dom)

    md_report = build_feature_quality_drift_profile_markdown_report(s_prof, df_prof)
    txt_report = build_feature_quality_drift_text_report(s_prof, df_prof)

    reports_dir = Path("reports/output/advanced_feature_quality_drift")
    reports_dir.mkdir(parents=True, exist_ok=True)
    with open(reports_dir / "feature_quality_drift_profiles.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(reports_dir / "feature_quality_drift_profiles.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("=" * 70)
    print("PHASE 123: FEATURE QUALITY & DRIFT PROFILE AND DOMAIN REGISTRY")
    print("=" * 70)
    print(f"Active Profile : {s_prof['active_profile']}")
    print(f"Total Profiles : {s_prof['total_profiles']}")
    print(f"Total Domains  : {s_dom['total_domains']}")
    print(f"Current Phase  : {s_prof['current_phase']}")
    print(f"Target Phase   : {s_prof['target_final_phase']}")
    print(f"Next Phase     : {s_prof['next_phase']}")
    print(f"Non-Signal     : {s_prof['non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
