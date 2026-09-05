from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.provider_quality_benchmark import build_provider_quality_benchmark_report
from advanced_provider_benchmark.provider_normalization_benchmark import build_provider_normalization_benchmark_report
from advanced_provider_benchmark.provider_traceability_benchmark import build_provider_traceability_benchmark_report
from advanced_provider_benchmark.provider_manual_review_benchmark import build_provider_manual_review_benchmark_report
from advanced_provider_benchmark.provider_benchmark_report_builder import (
    build_provider_quality_markdown_report,
    build_provider_normalization_markdown_report,
    build_provider_traceability_markdown_report,
    build_provider_benchmark_manual_review_markdown_report,
)


def main():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
    profile = get_default_provider_benchmark_profile()

    qual_df, qual_sum = build_provider_quality_benchmark_report(profile)
    norm_df, norm_sum = build_provider_normalization_benchmark_report(profile)
    trace_df, trace_sum = build_provider_traceability_benchmark_report(profile)
    rev_df, rev_sum = build_provider_manual_review_benchmark_report(profile)

    data_lake.save_provider_quality_benchmark_report(qual_df, qual_sum)
    data_lake.save_provider_normalization_benchmark_report(norm_df, norm_sum)
    data_lake.save_provider_traceability_benchmark_report(trace_df, trace_sum)
    data_lake.save_provider_manual_review_benchmark_report(rev_df, rev_sum)

    out_dir = project_root / "reports" / "output" / "advanced_provider_benchmark"
    csv_dir = out_dir / "csv"
    md_dir = out_dir / "markdown"
    txt_dir = out_dir / "txt"

    for d in [csv_dir, md_dir, txt_dir]:
        d.mkdir(parents=True, exist_ok=True)

    qual_df.to_csv(csv_dir / "provider_quality_benchmark_report.csv", index=False)
    norm_df.to_csv(csv_dir / "provider_normalization_benchmark_report.csv", index=False)
    trace_df.to_csv(csv_dir / "provider_traceability_benchmark_report.csv", index=False)
    rev_df.to_csv(csv_dir / "provider_manual_review_benchmark_report.csv", index=False)

    md_qual = build_provider_quality_markdown_report(qual_sum, qual_df)
    (md_dir / "provider_quality_benchmark_report.md").write_text(md_qual, encoding="utf-8")
    (txt_dir / "provider_quality_benchmark_report.txt").write_text(md_qual, encoding="utf-8")

    md_norm = build_provider_normalization_markdown_report(norm_sum, norm_df)
    (md_dir / "provider_normalization_benchmark_report.md").write_text(md_norm, encoding="utf-8")
    (txt_dir / "provider_normalization_benchmark_report.txt").write_text(md_norm, encoding="utf-8")

    md_trace = build_provider_traceability_markdown_report(trace_sum, trace_df)
    (md_dir / "provider_traceability_benchmark_report.md").write_text(md_trace, encoding="utf-8")
    (txt_dir / "provider_traceability_benchmark_report.txt").write_text(md_trace, encoding="utf-8")

    md_rev = build_provider_benchmark_manual_review_markdown_report(rev_sum, rev_df)
    (md_dir / "provider_manual_review_benchmark_report.md").write_text(md_rev, encoding="utf-8")
    (txt_dir / "provider_manual_review_benchmark_report.txt").write_text(md_rev, encoding="utf-8")

    print(f"Quality, normalization, traceability, and review benchmarks built successfully: {len(qual_df)} providers evaluated.")


if __name__ == "__main__":
    main()
