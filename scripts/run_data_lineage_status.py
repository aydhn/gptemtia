from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.data_lineage_pipeline import DataLineagePipeline


def main():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
    profile = get_default_data_lineage_profile()

    pipeline = DataLineagePipeline(
        data_lake=data_lake,
        settings=settings,
        project_root=project_root,
        profile=profile,
    )

    status_df, summary = pipeline.build_data_lineage_status(save=True)

    out_dir = project_root / "reports" / "output" / "advanced_data_lineage"
    csv_dir = out_dir / "csv"
    txt_dir = out_dir / "txt"

    for d in [csv_dir, txt_dir]:
        d.mkdir(parents=True, exist_ok=True)

    status_df.to_csv(csv_dir / "data_lineage_status_report.csv", index=False)

    lines = [
        "============================================================",
        "PHASE 114 DATA LINEAGE AND PROVENANCE - STATUS REPORT",
        "============================================================",
        f"Phase: {summary.get('current_phase')} ({summary.get('phase_name')})",
        f"Next Phase: {summary.get('next_phase')}",
        f"Target Final Phase: {summary.get('target_final_phase')}",
        f"Total Subsystems: {summary.get('total_subsystems')}",
        f"All Subsystems Ready: {summary.get('all_subsystems_ready')}",
        "------------------------------------------------------------",
        status_df.to_string(index=False),
        "============================================================",
    ]
    txt_content = "\n".join(lines)
    (txt_dir / "data_lineage_status_report.txt").write_text(txt_content, encoding="utf-8")

    print(txt_content)


if __name__ == "__main__":
    main()
