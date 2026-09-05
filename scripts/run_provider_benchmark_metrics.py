from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.provider_benchmark_metric_registry import build_provider_benchmark_metric_registry
from advanced_provider_benchmark.provider_benchmark_weight_registry import build_provider_benchmark_weight_registry
from advanced_provider_benchmark.provider_benchmark_report_builder import (
    build_provider_benchmark_metric_markdown_report,
)


def main():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
    profile = get_default_provider_benchmark_profile()

    met_df, met_sum = build_provider_benchmark_metric_registry(profile)
    wgt_df, wgt_sum = build_provider_benchmark_weight_registry(profile)

    data_lake.save_provider_benchmark_metric_registry(met_df, met_sum)
    data_lake.save_provider_benchmark_weight_registry(wgt_df, wgt_sum)

    out_dir = project_root / "reports" / "output" / "advanced_provider_benchmark"
    csv_dir = out_dir / "csv"
    md_dir = out_dir / "markdown"
    txt_dir = out_dir / "txt"

    for d in [csv_dir, md_dir, txt_dir]:
        d.mkdir(parents=True, exist_ok=True)

    met_df.to_csv(csv_dir / "provider_benchmark_metric_registry.csv", index=False)
    wgt_df.to_csv(csv_dir / "provider_benchmark_weight_registry.csv", index=False)

    md_met = build_provider_benchmark_metric_markdown_report(met_sum, met_df)
    (md_dir / "provider_benchmark_metric_registry.md").write_text(md_met, encoding="utf-8")
    (txt_dir / "provider_benchmark_metric_registry.txt").write_text(md_met, encoding="utf-8")

    print(f"Provider benchmark metrics & weights built successfully: {len(met_df)} metrics, {len(wgt_df)} weights.")


if __name__ == "__main__":
    main()
