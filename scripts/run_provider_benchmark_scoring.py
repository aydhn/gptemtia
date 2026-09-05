from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.provider_benchmark_scoring import build_provider_benchmark_score_report
from advanced_provider_benchmark.provider_ranking_research import build_provider_ranking_research_report
from advanced_provider_benchmark.provider_benchmark_findings import build_provider_benchmark_findings_registry
from advanced_provider_benchmark.provider_benchmark_manual_review_queue import build_provider_benchmark_manual_review_queue
from advanced_provider_benchmark.phase_116_handoff import build_phase_116_indicator_feature_factor_engine_handoff_report
from advanced_provider_benchmark.provider_benchmark_report_builder import (
    build_provider_benchmark_score_markdown_report,
    build_provider_ranking_research_markdown_report,
    build_provider_benchmark_findings_markdown_report,
    build_provider_benchmark_manual_review_markdown_report,
    build_phase_116_handoff_markdown_report,
)


def main():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
    profile = get_default_provider_benchmark_profile()

    scr_df, scr_sum = build_provider_benchmark_score_report(profile)
    rnk_df, rnk_sum = build_provider_ranking_research_report(profile)
    fnd_df, fnd_sum = build_provider_benchmark_findings_registry(profile)
    rev_df, rev_sum = build_provider_benchmark_manual_review_queue(fnd_df, profile)
    h116_df, h116_sum = build_phase_116_indicator_feature_factor_engine_handoff_report(profile)

    data_lake.save_provider_benchmark_score_report(scr_df, scr_sum)
    data_lake.save_provider_ranking_research_report(rnk_df, rnk_sum)
    data_lake.save_provider_benchmark_findings_registry(fnd_df, fnd_sum)
    data_lake.save_provider_benchmark_manual_review_queue(rev_df, rev_sum)
    data_lake.save_phase_116_indicator_feature_factor_engine_handoff_report(h116_df, h116_sum)

    out_dir = project_root / "reports" / "output" / "advanced_provider_benchmark"
    csv_dir = out_dir / "csv"
    md_dir = out_dir / "markdown"
    txt_dir = out_dir / "txt"

    for d in [csv_dir, md_dir, txt_dir]:
        d.mkdir(parents=True, exist_ok=True)

    scr_df.to_csv(csv_dir / "provider_benchmark_score_report.csv", index=False)
    rnk_df.to_csv(csv_dir / "provider_ranking_research_report.csv", index=False)
    fnd_df.to_csv(csv_dir / "provider_benchmark_findings_registry.csv", index=False)
    rev_df.to_csv(csv_dir / "provider_benchmark_manual_review_queue.csv", index=False)
    h116_df.to_csv(csv_dir / "phase_116_handoff_report.csv", index=False)

    md_scr = build_provider_benchmark_score_markdown_report(scr_sum, scr_df)
    (md_dir / "provider_benchmark_score_report.md").write_text(md_scr, encoding="utf-8")
    (txt_dir / "provider_benchmark_score_report.txt").write_text(md_scr, encoding="utf-8")

    md_rnk = build_provider_ranking_research_markdown_report(rnk_sum, rnk_df)
    (md_dir / "provider_ranking_research_report.md").write_text(md_rnk, encoding="utf-8")
    (txt_dir / "provider_ranking_research_report.txt").write_text(md_rnk, encoding="utf-8")

    md_fnd = build_provider_benchmark_findings_markdown_report(fnd_sum, fnd_df)
    (md_dir / "provider_benchmark_findings_registry.md").write_text(md_fnd, encoding="utf-8")
    (txt_dir / "provider_benchmark_findings_registry.txt").write_text(md_fnd, encoding="utf-8")

    md_rev = build_provider_benchmark_manual_review_markdown_report(rev_sum, rev_df)
    (md_dir / "provider_benchmark_manual_review_queue.md").write_text(md_rev, encoding="utf-8")
    (txt_dir / "provider_benchmark_manual_review_queue.txt").write_text(md_rev, encoding="utf-8")

    md_h116 = build_phase_116_handoff_markdown_report(h116_sum, h116_df)
    (md_dir / "phase_116_handoff_report.md").write_text(md_h116, encoding="utf-8")
    (txt_dir / "phase_116_handoff_report.txt").write_text(md_h116, encoding="utf-8")

    print(f"Provider scoring, ranking, findings, review queue, and Phase 116 handoff built successfully: {len(scr_df)} scored.")


if __name__ == "__main__":
    main()
