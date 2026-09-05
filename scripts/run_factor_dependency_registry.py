"""Phase 122: Run Factor Dependency Registry Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_factor_metadata.factor_metadata_config import get_default_factor_metadata_profile
from advanced_factor_metadata.factor_dependency_registry import build_factor_dependency_registry
from advanced_factor_metadata.factor_validation_dependencies import build_factor_validation_dependency_registry
from advanced_factor_metadata.factor_quality_dependencies import build_factor_quality_dependency_registry
from advanced_factor_metadata.factor_metadata_report_builder import build_factor_dependency_markdown_report
from reports.report_builder import build_factor_dependency_text_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_factor_metadata_profile()

    df_dep, s_dep = build_factor_dependency_registry(profile)
    df_vdep, s_vdep = build_factor_validation_dependency_registry(profile)
    df_qdep, s_qdep = build_factor_quality_dependency_registry(profile)

    data_lake.save_factor_dependency_registry(df_dep, s_dep)
    data_lake.save_factor_validation_dependency_registry(df_vdep, s_vdep)
    data_lake.save_factor_quality_dependency_registry(df_qdep, s_qdep)

    md_report = build_factor_dependency_markdown_report(s_dep, df_dep)
    txt_report = build_factor_dependency_text_report(s_dep, df_dep)

    reports_dir = Path("reports/output/advanced_factor_metadata")
    reports_dir.mkdir(parents=True, exist_ok=True)
    with open(reports_dir / "factor_dependencies.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(reports_dir / "factor_dependencies.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("=" * 70)
    print("PHASE 122: FACTOR DEPENDENCY REGISTRY")
    print("=" * 70)
    print(f"Total Dependencies     : {s_dep['total_dependencies']}")
    print(f"Mandatory Dependencies : {s_dep['mandatory_dependencies']}")
    print(f"Validation Dependencies: {s_vdep['total_validation_dependencies']}")
    print(f"Quality Dependencies   : {s_qdep['total_quality_dependencies']}")
    print(f"Non-Signal             : {s_dep['non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
