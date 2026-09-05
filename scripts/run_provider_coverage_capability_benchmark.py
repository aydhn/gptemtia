from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.provider_coverage_benchmark import build_provider_coverage_benchmark_report
from advanced_provider_benchmark.provider_capability_benchmark import build_provider_capability_benchmark_report
from advanced_provider_benchmark.provider_license_provenance_benchmark import build_provider_license_provenance_benchmark_report
from advanced_provider_benchmark.provider_no_scraping_compliance import build_provider_no_scraping_compliance_report
from advanced_provider_benchmark.provider_metadata_only_compliance import build_provider_metadata_only_compliance_report
from advanced_provider_benchmark.provider_benchmark_report_builder import (
    build_provider_coverage_markdown_report,
    build_provider_capability_markdown_report,
    build_provider_compliance_markdown_report,
)


def main():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
    profile = get_default_provider_benchmark_profile()

    cov_df, cov_sum = build_provider_coverage_benchmark_report(profile)
    cap_df, cap_sum = build_provider_capability_benchmark_report(profile)
    lic_df, lic_sum = build_provider_license_provenance_benchmark_report(profile)
    noscrap_df, noscrap_sum = build_provider_no_scraping_compliance_report(profile)
    meta_df, meta_sum = build_provider_metadata_only_compliance_report(profile)

    data_lake.save_provider_coverage_benchmark_report(cov_df, cov_sum)
    data_lake.save_provider_capability_benchmark_report(cap_df, cap_sum)
    data_lake.save_provider_license_provenance_benchmark_report(lic_df, lic_sum)
    data_lake.save_provider_no_scraping_compliance_report(noscrap_df, noscrap_sum)
    data_lake.save_provider_metadata_only_compliance_report(meta_df, meta_sum)

    out_dir = project_root / "reports" / "output" / "advanced_provider_benchmark"
    csv_dir = out_dir / "csv"
    md_dir = out_dir / "markdown"
    txt_dir = out_dir / "txt"

    for d in [csv_dir, md_dir, txt_dir]:
        d.mkdir(parents=True, exist_ok=True)

    cov_df.to_csv(csv_dir / "provider_coverage_benchmark_report.csv", index=False)
    cap_df.to_csv(csv_dir / "provider_capability_benchmark_report.csv", index=False)
    lic_df.to_csv(csv_dir / "provider_license_provenance_benchmark_report.csv", index=False)
    noscrap_df.to_csv(csv_dir / "provider_no_scraping_compliance_report.csv", index=False)
    meta_df.to_csv(csv_dir / "provider_metadata_only_compliance_report.csv", index=False)

    md_cov = build_provider_coverage_markdown_report(cov_sum, cov_df)
    (md_dir / "provider_coverage_benchmark_report.md").write_text(md_cov, encoding="utf-8")
    (txt_dir / "provider_coverage_benchmark_report.txt").write_text(md_cov, encoding="utf-8")

    md_cap = build_provider_capability_markdown_report(cap_sum, cap_df)
    (md_dir / "provider_capability_benchmark_report.md").write_text(md_cap, encoding="utf-8")
    (txt_dir / "provider_capability_benchmark_report.txt").write_text(md_cap, encoding="utf-8")

    md_comp = build_provider_compliance_markdown_report({**noscrap_sum, **meta_sum}, noscrap_df)
    (md_dir / "provider_compliance_benchmark_report.md").write_text(md_comp, encoding="utf-8")
    (txt_dir / "provider_compliance_benchmark_report.txt").write_text(md_comp, encoding="utf-8")

    print(f"Coverage, capability, and compliance benchmarks built successfully: {len(cov_df)} providers evaluated.")


if __name__ == "__main__":
    main()
