"""Phase 124: Run Validation & Safety Report Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_feature_store_integration.feature_store_integration_config import (
    get_default_feature_store_integration_profile,
)
from advanced_feature_store_integration.feature_store_integration_pipeline import (
    FeatureStoreIntegrationPipeline,
)
from advanced_feature_store_integration.feature_store_integration_report_builder import (
    build_feature_store_validation_markdown_report,
    build_feature_store_safety_markdown_report,
)
from reports.report_builder import (
    build_feature_store_validation_text_report,
    build_feature_store_safety_text_report,
)


def main():
    data_lake = DataLake()
    profile = get_default_feature_store_integration_profile()
    pipeline = FeatureStoreIntegrationPipeline(data_lake=data_lake, profile=profile)

    tables, summaries = pipeline.build_health_validation_safety_handoff(save=True)
    df_val = tables["validation"]
    s_val = summaries["validation"]
    df_safe = tables["safety"]
    s_safe = summaries["safety"]

    md_val = build_feature_store_validation_markdown_report(s_val, df_val)
    txt_val = build_feature_store_validation_text_report(s_val, df_val)
    md_safe = build_feature_store_safety_markdown_report(s_safe, df_safe)
    txt_safe = build_feature_store_safety_text_report(s_safe, df_safe)

    reports_dir = Path("reports/output/advanced_feature_store_integration")
    reports_dir.mkdir(parents=True, exist_ok=True)
    with open(reports_dir / "feature_store_validation.md", "w", encoding="utf-8") as f:
        f.write(md_val)
    with open(reports_dir / "feature_store_validation.txt", "w", encoding="utf-8") as f:
        f.write(txt_val)
    with open(reports_dir / "feature_store_safety.md", "w", encoding="utf-8") as f:
        f.write(md_safe)
    with open(reports_dir / "feature_store_safety.txt", "w", encoding="utf-8") as f:
        f.write(txt_safe)

    print("=" * 70)
    print("PHASE 124: VALIDATION & SAFETY REPORT")
    print("=" * 70)
    print(f"Validation Status   : {s_val['status']}")
    print(f"Passed Rules        : {s_val['passed_rules']}/{s_val['total_rules']}")
    print(f"Safety Status       : {s_safe['safety_status']}")
    print(f"NO-GO Rules         : {s_safe['no_go_count']}")
    print(f"SAFE-GO Principles  : {s_safe['safe_go_count']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
