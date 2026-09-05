from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.provider_provenance_registry import build_provider_provenance_registry
from advanced_data_lineage.dataset_provenance_registry import build_dataset_provenance_registry
from advanced_data_lineage.schema_provenance_registry import build_schema_provenance_registry
from advanced_data_lineage.data_lineage_report_builder import (
    build_provider_provenance_markdown_report,
    build_dataset_provenance_markdown_report,
)


def main():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
    profile = get_default_data_lineage_profile()

    prov_df, prov_sum = build_provider_provenance_registry(profile)
    ds_df, ds_sum = build_dataset_provenance_registry(profile)
    sch_df, sch_sum = build_schema_provenance_registry(profile)

    data_lake.save_provider_provenance_registry(prov_df, prov_sum)
    data_lake.save_dataset_provenance_registry(ds_df, ds_sum)
    data_lake.save_schema_provenance_registry(sch_df, sch_sum)

    out_dir = project_root / "reports" / "output" / "advanced_data_lineage"
    csv_dir = out_dir / "csv"
    md_dir = out_dir / "markdown"
    txt_dir = out_dir / "txt"

    for d in [csv_dir, md_dir, txt_dir]:
        d.mkdir(parents=True, exist_ok=True)

    prov_df.to_csv(csv_dir / "provider_provenance_registry.csv", index=False)
    ds_df.to_csv(csv_dir / "dataset_provenance_registry.csv", index=False)
    sch_df.to_csv(csv_dir / "schema_provenance_registry.csv", index=False)

    md_prov = build_provider_provenance_markdown_report(prov_sum, prov_df)
    (md_dir / "provider_provenance_registry.md").write_text(md_prov, encoding="utf-8")
    (txt_dir / "provider_provenance_registry.txt").write_text(md_prov, encoding="utf-8")

    md_ds = build_dataset_provenance_markdown_report(ds_sum, ds_df)
    (md_dir / "dataset_provenance_registry.md").write_text(md_ds, encoding="utf-8")
    (txt_dir / "dataset_provenance_registry.txt").write_text(md_ds, encoding="utf-8")

    print(f"Provider and dataset provenance registries built successfully: {len(prov_df)} providers, {len(ds_df)} datasets, {len(sch_df)} schemas.")


if __name__ == "__main__":
    main()
