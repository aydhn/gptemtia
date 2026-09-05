from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.provider_benchmark_safety_boundary import build_provider_benchmark_safety_boundary
from advanced_provider_benchmark.provider_benchmark_validation import build_provider_benchmark_validation_report
from advanced_provider_benchmark.provider_benchmark_profile_registry import build_provider_benchmark_profile_registry
from advanced_provider_benchmark.provider_benchmark_metric_registry import build_provider_benchmark_metric_registry
from advanced_provider_benchmark.provider_benchmark_scoring import build_provider_benchmark_score_report
from advanced_provider_benchmark.provider_ranking_research import build_provider_ranking_research_report
from advanced_provider_benchmark.provider_benchmark_manual_review_queue import build_provider_benchmark_manual_review_queue
from advanced_provider_benchmark.provider_benchmark_report_builder import (
    build_provider_benchmark_validation_markdown_report,
    build_provider_benchmark_safety_markdown_report,
)


def main():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
    profile = get_default_provider_benchmark_profile()

    prof_df, _ = build_provider_benchmark_profile_registry(profile)
    met_df, _ = build_provider_benchmark_metric_registry(profile)
    scr_df, _ = build_provider_benchmark_score_report(profile)
    rnk_df, _ = build_provider_ranking_research_report(profile)
    rev_df, _ = build_provider_benchmark_manual_review_queue(None, profile)
    safe_df, safe_sum = build_provider_benchmark_safety_boundary(profile)

    tables_to_validate = {
        "profiles": prof_df,
        "metrics": met_df,
        "scores": scr_df,
        "ranking": rnk_df,
        "manual_review": rev_df,
        "safety": safe_df,
    }
    val_df, val_sum = build_provider_benchmark_validation_report(tables_to_validate, profile)

    data_lake.save_provider_benchmark_validation_report(val_df, val_sum)
    data_lake.save_provider_benchmark_safety_boundary(safe_df, safe_sum)

    out_dir = project_root / "reports" / "output" / "advanced_provider_benchmark"
    csv_dir = out_dir / "csv"
    md_dir = out_dir / "markdown"
    txt_dir = out_dir / "txt"

    for d in [csv_dir, md_dir, txt_dir]:
        d.mkdir(parents=True, exist_ok=True)

    val_df.to_csv(csv_dir / "provider_benchmark_validation_report.csv", index=False)
    safe_df.to_csv(csv_dir / "provider_benchmark_safety_boundary.csv", index=False)

    md_val = build_provider_benchmark_validation_markdown_report(val_sum, val_df)
    (md_dir / "provider_benchmark_validation_report.md").write_text(md_val, encoding="utf-8")
    (txt_dir / "provider_benchmark_validation_report.txt").write_text(md_val, encoding="utf-8")

    md_safe = build_provider_benchmark_safety_markdown_report(safe_sum, safe_df)
    (md_dir / "provider_benchmark_safety_boundary.md").write_text(md_safe, encoding="utf-8")
    (txt_dir / "provider_benchmark_safety_boundary.txt").write_text(md_safe, encoding="utf-8")

    print(f"Validation & safety boundary reports built successfully: {val_sum['validation_status']}, Safety: {safe_sum['safety_status']}.")


if __name__ == "__main__":
    main()
