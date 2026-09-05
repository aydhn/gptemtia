"""Phase 124: Run Feature Store Metadata Manifest Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_feature_store_integration.feature_store_integration_config import (
    get_default_feature_store_integration_profile,
)
from advanced_feature_store_integration.feature_store_lineage_references import (
    build_feature_store_lineage_reference_registry,
)
from advanced_feature_store_integration.feature_store_validation_status import (
    build_feature_store_validation_status_registry,
)
from advanced_feature_store_integration.feature_store_manual_review_blockers import (
    build_feature_store_manual_review_blocker_registry,
)
from advanced_feature_store_integration.feature_store_metadata_manifest import (
    build_feature_store_metadata_manifest,
)
from advanced_feature_store_integration.feature_store_integration_report_builder import (
    build_feature_store_manifest_markdown_report,
)
from reports.report_builder import build_feature_store_manifest_text_report


def main():
    data_lake = DataLake()
    profile = get_default_feature_store_integration_profile()

    df_lin, s_lin = build_feature_store_lineage_reference_registry(profile)
    df_val, s_val = build_feature_store_validation_status_registry(profile)
    df_blk, s_blk = build_feature_store_manual_review_blocker_registry(profile)
    df_man, s_man = build_feature_store_metadata_manifest(profile)

    data_lake.save_feature_store_lineage_reference_registry(df_lin, s_lin)
    data_lake.save_feature_store_validation_status_registry(df_val, s_val)
    data_lake.save_feature_store_manual_review_blocker_registry(df_blk, s_blk)
    data_lake.save_feature_store_metadata_manifest(df_man, s_man)

    md_report = build_feature_store_manifest_markdown_report(s_man, df_man)
    txt_report = build_feature_store_manifest_text_report(s_man, df_man)

    reports_dir = Path("reports/output/advanced_feature_store_integration")
    reports_dir.mkdir(parents=True, exist_ok=True)
    with open(reports_dir / "feature_store_manifest.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(reports_dir / "feature_store_manifest.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("=" * 70)
    print("PHASE 124: FEATURE STORE METADATA MANIFEST & AUDIT")
    print("=" * 70)
    print(f"Store Name       : {s_man['store_name']}")
    print(f"Features Covered : {s_man['total_features']}")
    print(f"Factors Covered  : {s_man['total_factors']}")
    print(f"Active Blockers  : {s_blk['active_blocking_count']}")
    print(f"Non-Signal       : {s_man['non_signal']}")
    print(f"Source Preserved : {s_man['source_preserved']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
