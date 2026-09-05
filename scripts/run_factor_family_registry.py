"""Phase 122: Run Factor Family Registry Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_factor_metadata.factor_metadata_config import get_default_factor_metadata_profile
from advanced_factor_metadata.factor_family_registry import build_factor_family_registry
from advanced_factor_metadata.factor_metadata_report_builder import build_factor_family_markdown_report
from reports.report_builder import build_factor_family_text_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_factor_metadata_profile()

    df_fam, s_fam = build_factor_family_registry(profile)
    data_lake.save_factor_family_registry(df_fam, s_fam)

    md_report = build_factor_family_markdown_report(s_fam, df_fam)
    txt_report = build_factor_family_text_report(s_fam, df_fam)

    reports_dir = Path("reports/output/advanced_factor_metadata")
    reports_dir.mkdir(parents=True, exist_ok=True)
    with open(reports_dir / "factor_families.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(reports_dir / "factor_families.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("=" * 70)
    print("PHASE 122: FACTOR FAMILY TAXONOMY REGISTRY")
    print("=" * 70)
    print(f"Total Families      : {s_fam['total_families']}")
    print(f"Ready Families      : {s_fam['ready_families']}")
    print(f"Placeholder Families: {s_fam['placeholder_families']}")
    print(f"Non-Signal          : {s_fam['non_signal']}")
    print(f"Status              : {s_fam['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
