from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.data_lineage_profile_registry import build_data_lineage_profile_registry
from advanced_data_lineage.data_lineage_domain_registry import build_data_lineage_domain_registry
from advanced_data_lineage.data_lineage_report_builder import (
    build_data_lineage_profile_markdown_report,
    build_domain_lineage_markdown_report,
)


def main():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
    profile = get_default_data_lineage_profile()

    prof_df, prof_sum = build_data_lineage_profile_registry(profile)
    dom_df, dom_sum = build_data_lineage_domain_registry(profile)

    data_lake.save_data_lineage_profile_registry(prof_df, prof_sum)
    data_lake.save_data_lineage_domain_registry(dom_df, dom_sum)

    out_dir = project_root / "reports" / "output" / "advanced_data_lineage"
    csv_dir = out_dir / "csv"
    md_dir = out_dir / "markdown"
    txt_dir = out_dir / "txt"

    for d in [csv_dir, md_dir, txt_dir]:
        d.mkdir(parents=True, exist_ok=True)

    prof_df.to_csv(csv_dir / "data_lineage_profile_registry.csv", index=False)
    dom_df.to_csv(csv_dir / "data_lineage_domain_registry.csv", index=False)

    md_prof = build_data_lineage_profile_markdown_report(prof_sum, prof_df)
    (md_dir / "data_lineage_profile_registry.md").write_text(md_prof, encoding="utf-8")
    (txt_dir / "data_lineage_profile_registry.txt").write_text(md_prof, encoding="utf-8")

    md_dom = build_domain_lineage_markdown_report(dom_sum, dom_df)
    (md_dir / "data_lineage_domain_registry.md").write_text(md_dom, encoding="utf-8")
    (txt_dir / "data_lineage_domain_registry.txt").write_text(md_dom, encoding="utf-8")

    print(f"Data lineage profile & domain registries built successfully: {len(prof_df)} profiles, {len(dom_df)} domains.")


if __name__ == "__main__":
    main()
