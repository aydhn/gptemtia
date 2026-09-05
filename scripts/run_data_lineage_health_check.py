from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.data_lineage_health import build_data_lineage_health_check
from advanced_data_lineage.data_lineage_report_builder import build_data_lineage_health_markdown_report


def main():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
    profile = get_default_data_lineage_profile()

    hlth_df, hlth_sum = build_data_lineage_health_check(project_root, profile)
    data_lake.save_data_lineage_health_check(hlth_df, hlth_sum)

    out_dir = project_root / "reports" / "output" / "advanced_data_lineage"
    csv_dir = out_dir / "csv"
    md_dir = out_dir / "markdown"
    txt_dir = out_dir / "txt"

    for d in [csv_dir, md_dir, txt_dir]:
        d.mkdir(parents=True, exist_ok=True)

    hlth_df.to_csv(csv_dir / "data_lineage_health_check.csv", index=False)
    md_hlth = build_data_lineage_health_markdown_report(hlth_sum, hlth_df)
    (md_dir / "data_lineage_health_check.md").write_text(md_hlth, encoding="utf-8")
    (txt_dir / "data_lineage_health_check.txt").write_text(md_hlth, encoding="utf-8")

    print(f"Data lineage health check completed: {hlth_sum['passed_checks']}/{hlth_sum['total_checks']} checks passed. Overall status: {hlth_sum['overall_status']}")


if __name__ == "__main__":
    main()
