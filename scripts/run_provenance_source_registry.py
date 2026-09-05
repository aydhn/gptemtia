from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.provenance_source_registry import build_provenance_source_registry
from advanced_data_lineage.source_reference_registry import build_source_reference_registry
from advanced_data_lineage.license_provenance_registry import build_license_provenance_registry
from advanced_data_lineage.data_usage_boundary_registry import build_data_usage_boundary_registry
from advanced_data_lineage.data_lineage_report_builder import (
    build_provenance_source_markdown_report,
    build_license_copyright_markdown_report,
)


def main():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
    profile = get_default_data_lineage_profile()

    src_df, src_sum = build_provenance_source_registry(profile)
    ref_df, ref_sum = build_source_reference_registry(profile)
    lic_df, lic_sum = build_license_provenance_registry(profile)
    use_df, use_sum = build_data_usage_boundary_registry(profile)

    data_lake.save_provenance_source_registry(src_df, src_sum)
    data_lake.save_source_reference_registry(ref_df, ref_sum)
    data_lake.save_license_provenance_registry(lic_df, lic_sum)
    data_lake.save_data_usage_boundary_registry(use_df, use_sum)

    out_dir = project_root / "reports" / "output" / "advanced_data_lineage"
    csv_dir = out_dir / "csv"
    md_dir = out_dir / "markdown"
    txt_dir = out_dir / "txt"

    for d in [csv_dir, md_dir, txt_dir]:
        d.mkdir(parents=True, exist_ok=True)

    src_df.to_csv(csv_dir / "provenance_source_registry.csv", index=False)
    ref_df.to_csv(csv_dir / "source_reference_registry.csv", index=False)
    lic_df.to_csv(csv_dir / "license_provenance_registry.csv", index=False)
    use_df.to_csv(csv_dir / "data_usage_boundary_registry.csv", index=False)

    md_src = build_provenance_source_markdown_report(src_sum, src_df)
    (md_dir / "provenance_source_registry.md").write_text(md_src, encoding="utf-8")
    (txt_dir / "provenance_source_registry.txt").write_text(md_src, encoding="utf-8")

    md_lic = build_license_copyright_markdown_report(lic_sum, lic_df)
    (md_dir / "license_provenance_registry.md").write_text(md_lic, encoding="utf-8")
    (txt_dir / "license_provenance_registry.txt").write_text(md_lic, encoding="utf-8")

    print(f"Provenance source & usage registries built successfully: {len(src_df)} sources, {len(ref_df)} references, {len(lic_df)} licenses.")


if __name__ == "__main__":
    main()
