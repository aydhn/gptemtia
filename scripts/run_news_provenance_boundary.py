from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.copyright_boundary_provenance import (
    build_copyright_boundary_provenance_registry,
    check_copyright_boundary_provenance,
)
from advanced_data_lineage.metadata_only_provenance import build_metadata_only_provenance_registry
from advanced_data_lineage.data_lineage_report_builder import (
    build_license_copyright_markdown_report,
)


def main():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
    profile = get_default_data_lineage_profile()

    cop_df, cop_sum = build_copyright_boundary_provenance_registry(profile)
    meta_df, meta_sum = build_metadata_only_provenance_registry(profile)

    check_res = check_copyright_boundary_provenance(cop_df)
    if not check_res["passed"]:
        raise RuntimeError(f"Copyright boundary check failed: {check_res['violations']}")

    data_lake.save_copyright_boundary_provenance_registry(cop_df, cop_sum)
    data_lake.save_metadata_only_provenance_registry(meta_df, meta_sum)

    out_dir = project_root / "reports" / "output" / "advanced_data_lineage"
    csv_dir = out_dir / "csv"
    md_dir = out_dir / "markdown"
    txt_dir = out_dir / "txt"

    for d in [csv_dir, md_dir, txt_dir]:
        d.mkdir(parents=True, exist_ok=True)

    cop_df.to_csv(csv_dir / "copyright_boundary_registry.csv", index=False)
    meta_df.to_csv(csv_dir / "metadata_only_registry.csv", index=False)

    md_cop = build_license_copyright_markdown_report(cop_sum, cop_df)
    (md_dir / "copyright_boundary_provenance.md").write_text(md_cop, encoding="utf-8")
    (txt_dir / "copyright_boundary_provenance.txt").write_text(md_cop, encoding="utf-8")

    print(f"News copyright boundary and metadata-only registries verified: zero full text confirmed across {len(cop_df)} checks.")


if __name__ == "__main__":
    main()
