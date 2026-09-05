"""Phase 122: Run Factor Metadata Validation and Safety Report Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_factor_metadata.factor_metadata_config import get_default_factor_metadata_profile
from advanced_factor_metadata.factor_metadata_profile_registry import build_factor_metadata_profile_registry
from advanced_factor_metadata.factor_family_registry import build_factor_family_registry
from advanced_factor_metadata.factor_contract_registry import build_factor_contract_registry
from advanced_factor_metadata.factor_namespace_registry import build_factor_namespace_registry
from advanced_factor_metadata.factor_output_schema import build_factor_output_schema_registry
from advanced_factor_metadata.factor_metadata_manifest import build_factor_metadata_manifest
from advanced_factor_metadata.factor_metadata_validation import build_factor_metadata_validation_report
from advanced_factor_metadata.factor_metadata_safety_boundary import build_factor_metadata_safety_boundary
from advanced_factor_metadata.factor_metadata_report_builder import (
    build_factor_validation_markdown_report,
    build_factor_safety_markdown_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_factor_metadata_profile()

    df_prof, _ = build_factor_metadata_profile_registry(profile)
    df_fam, _ = build_factor_family_registry(profile)
    df_cntr, _ = build_factor_contract_registry(profile)
    df_ns, _ = build_factor_namespace_registry(profile)
    df_sch, _ = build_factor_output_schema_registry(profile)
    df_manf, _ = build_factor_metadata_manifest(profile)

    tables = {
        "profiles": df_prof,
        "families": df_fam,
        "contracts": df_cntr,
        "namespaces": df_ns,
        "schemas": df_sch,
        "manifests": df_manf,
    }

    df_val, s_val = build_factor_metadata_validation_report(tables, profile)
    df_safety, s_safety = build_factor_metadata_safety_boundary(profile)

    data_lake.save_factor_validation_report(df_val, s_val)
    data_lake.save_factor_safety_boundary(df_safety, s_safety)

    md_val = build_factor_validation_markdown_report(s_val, df_val)
    md_safety = build_factor_safety_markdown_report(s_safety, df_safety)

    reports_dir = Path("reports/output/advanced_factor_metadata")
    reports_dir.mkdir(parents=True, exist_ok=True)
    with open(reports_dir / "factor_validation_report.md", "w", encoding="utf-8") as f:
        f.write(md_val)
    with open(reports_dir / "factor_safety_boundary.md", "w", encoding="utf-8") as f:
        f.write(md_safety)

    print("=" * 70)
    print("PHASE 122: FACTOR VALIDATION AND SAFETY REPORT")
    print("=" * 70)
    print(f"Validation Status    : {s_val['status']}")
    print(f"Total Checks         : {s_val['total_validation_checks']}")
    print(f"Passed Checks        : {s_val['passed_checks']}")
    print(f"Failed Checks        : {s_val['failed_checks']}")
    print(f"Safety Status        : {s_safety['safety_status']}")
    print(f"NO-GO Rules Enforced : {s_safety['no_go_count']}")
    print(f"SAFE-GO Rules Active : {s_safety['safe_go_count']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
