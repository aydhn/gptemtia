import sys
from pathlib import Path

# Add project root to sys.path
root = Path(__file__).resolve().parent.parent
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

from config.settings import Settings
from config.paths import ensure_project_directories
from data.storage.data_lake import DataLake
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.data_quality_pipeline import DataQualityPipeline
from advanced_data_quality.data_quality_report_builder import (
    build_data_quality_profile_markdown_report,
)


def main():
    ensure_project_directories()
    settings = Settings()
    profile = get_default_data_quality_profile()
    lake = DataLake()
    pipeline = DataQualityPipeline(data_lake=lake, settings=settings, project_root=root, profile=profile)

    tables, summary = pipeline.build_quality_profiles_and_domains(save=True)
    profile_df = tables.get("profile_registry")
    domain_df = tables.get("domain_registry")
    sev_df = tables.get("severity_registry")

    # Output reports
    out_dir = root / "reports" / "output" / "advanced_data_quality"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "csv").mkdir(exist_ok=True)
    (out_dir / "markdown").mkdir(exist_ok=True)
    (out_dir / "txt").mkdir(exist_ok=True)

    if profile_df is not None:
        profile_df.to_csv(out_dir / "csv" / "profile_registry.csv", index=False)
    if domain_df is not None:
        domain_df.to_csv(out_dir / "csv" / "domain_registry.csv", index=False)
    if sev_df is not None:
        sev_df.to_csv(out_dir / "csv" / "severity_registry.csv", index=False)

    md = build_data_quality_profile_markdown_report(summary.get("profile_summary", {}), profile_df)
    with open(out_dir / "markdown" / "profile_registry_report.md", "w", encoding="utf-8") as f:
        f.write(md)

    with open(out_dir / "txt" / "profile_registry_summary.txt", "w", encoding="utf-8") as f:
        f.write(f"Phase 112 Data Quality Profiles: {summary.get('profile_summary', {}).get('total_profiles')}\n")
        f.write(f"Domains: {summary.get('domain_summary', {}).get('total_domains')}\n")

    print(f"Data quality profile & domain registry generated successfully. Profiles: {len(profile_df) if profile_df is not None else 0}")


if __name__ == "__main__":
    main()
