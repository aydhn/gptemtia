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
from advanced_data_normalization.data_normalization_report_builder import (
    build_data_normalization_profile_markdown_report,
)


def main():
    ensure_project_directories()
    settings = Settings()
    profile = get_default_data_normalization_profile()
    lake = DataLake()
    pipeline = DataNormalizationPipeline(data_lake=lake, settings=settings, project_root=root, profile=profile)

    tables, summary = pipeline.build_normalization_profiles_and_domains(save=True)
    prof_df = tables.get("profile_registry")
    dom_df = tables.get("domain_registry")
    stat_df = tables.get("status_registry")

    out_dir = root / "reports" / "output" / "advanced_data_normalization"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "csv").mkdir(exist_ok=True)
    (out_dir / "markdown").mkdir(exist_ok=True)
    (out_dir / "txt").mkdir(exist_ok=True)

    if prof_df is not None:
        prof_df.to_csv(out_dir / "csv" / "profile_registry.csv", index=False)
    if dom_df is not None:
        dom_df.to_csv(out_dir / "csv" / "domain_registry.csv", index=False)
    if stat_df is not None:
        stat_df.to_csv(out_dir / "csv" / "status_registry.csv", index=False)

    md = build_data_normalization_profile_markdown_report(summary.get("profile_summary", {}), prof_df)
    with open(out_dir / "markdown" / "profile_registry_report.md", "w", encoding="utf-8") as f:
        f.write(md)

    with open(out_dir / "txt" / "profile_registry_summary.txt", "w", encoding="utf-8") as f:
        f.write(f"Data Normalization Profiles: {summary.get('profile_summary', {}).get('total_profiles', 0)}\n")
        f.write(f"Normalization Domains: {summary.get('domain_summary', {}).get('total_domains', 0)}\n")

    print(f"Data normalization profile & domain registry generated successfully. Profiles: {len(prof_df) if prof_df is not None else 0}")


if __name__ == "__main__":
    main()
