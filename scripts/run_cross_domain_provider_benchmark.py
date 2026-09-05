from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.cross_domain_provider_benchmark import build_cross_domain_provider_benchmark_report
from advanced_provider_benchmark.provider_benchmark_report_builder import (
    build_cross_domain_provider_benchmark_markdown_report,
)


def main():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
    profile = get_default_provider_benchmark_profile()

    cd_df, cd_sum = build_cross_domain_provider_benchmark_report(profile)
    data_lake.save_cross_domain_provider_benchmark_report(cd_df, cd_sum)

    out_dir = project_root / "reports" / "output" / "advanced_provider_benchmark"
    csv_dir = out_dir / "csv"
    md_dir = out_dir / "markdown"
    txt_dir = out_dir / "txt"

    for d in [csv_dir, md_dir, txt_dir]:
        d.mkdir(parents=True, exist_ok=True)

    cd_df.to_csv(csv_dir / "cross_domain_report.csv", index=False)
    md_text = build_cross_domain_provider_benchmark_markdown_report(cd_sum, cd_df)
    (md_dir / "cross_domain_report.md").write_text(md_text, encoding="utf-8")
    (txt_dir / "cross_domain_report.txt").write_text(md_text, encoding="utf-8")

    print(f"Cross-domain provider benchmark built successfully: {len(cd_df)} cross-domain alignments.")


if __name__ == "__main__":
    main()
