import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

from config.settings import Settings
from config.paths import ensure_project_directories
from data.storage.data_lake import DataLake
from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile
from advanced_data_normalization.data_normalization_pipeline import DataNormalizationPipeline


def main():
    ensure_project_directories()
    settings = Settings()
    profile = get_default_data_normalization_profile()
    lake = DataLake()
    pipeline = DataNormalizationPipeline(data_lake=lake, settings=settings, project_root=root, profile=profile)

    status_df, summary = pipeline.build_data_normalization_status(save=True)

    out_dir = root / "reports" / "output" / "advanced_data_normalization"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "csv").mkdir(exist_ok=True)
    (out_dir / "txt").mkdir(exist_ok=True)

    status_df.to_csv(out_dir / "csv" / "data_normalization_status_report.csv", index=False)

    with open(out_dir / "txt" / "data_normalization_status.txt", "w", encoding="utf-8") as f:
        f.write("=== PHASE 113 DATA NORMALIZATION LAYER STATUS ===\n")
        f.write(f"Total Components: {summary.get('total_components', 0)}\n")
        f.write(f"All Ready: {summary.get('all_ready', False)}\n")
        f.write(f"Non-Destructive: {summary.get('all_non_destructive', True)}\n")
        f.write(f"Current Phase: {summary.get('current_phase', 113)}\n")
        f.write(f"Target Final Phase: {summary.get('target_final_phase', 160)}\n\n")
        for _, row in status_df.iterrows():
            f.write(f"- {row['component']}: {row['status']} (non_destructive={row['non_destructive']})\n")

    print(f"Data normalization status report generated: {summary.get('total_components', 0)} components verified.")


if __name__ == "__main__":
    main()
