from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.provider_benchmark_health import build_provider_benchmark_health_check
from advanced_provider_benchmark.provider_benchmark_report_builder import (
    build_provider_benchmark_health_markdown_report,
)


def main():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
    profile = get_default_provider_benchmark_profile()

    hlth_df, hlth_sum = build_provider_benchmark_health_check(project_root, profile)
    data_lake.save_provider_benchmark_health_check(hlth_df, hlth_sum)

    out_dir = project_root / "reports" / "output" / "advanced_provider_benchmark"
    csv_dir = out_dir / "csv"
    md_dir = out_dir / "markdown"
    txt_dir = out_dir / "txt"

    for d in [csv_dir, md_dir, txt_dir]:
        d.mkdir(parents=True, exist_ok=True)

    hlth_df.to_csv(csv_dir / "provider_benchmark_health_check.csv", index=False)
    md_hlth = build_provider_benchmark_health_markdown_report(hlth_sum, hlth_df)
    (md_dir / "provider_benchmark_health_check.md").write_text(md_hlth, encoding="utf-8")
    (txt_dir / "provider_benchmark_health_check.txt").write_text(md_hlth, encoding="utf-8")

    print(f"Provider benchmark health check complete: {hlth_sum['overall_status']} ({hlth_sum['passed_checks']}/{hlth_sum['total_checks']} passed).")


if __name__ == "__main__":
    main()
