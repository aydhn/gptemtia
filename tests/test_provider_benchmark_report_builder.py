from advanced_provider_benchmark.provider_benchmark_report_builder import (
    build_provider_benchmark_disclaimer,
    build_provider_benchmark_profile_markdown_report,
    build_provider_benchmark_score_markdown_report,
    build_phase_116_handoff_markdown_report,
)


def test_provider_benchmark_report_builder():
    disclaimer = build_provider_benchmark_disclaimer()
    assert "Phase 115 Data Provider Benchmark Report" in disclaimer
    assert "Canlı emir" in disclaimer

    prof_md = build_provider_benchmark_profile_markdown_report({"total_profiles": 3})
    assert "Provider Benchmark Profile Registry" in prof_md
    assert "Phase 115 Data Provider Benchmark Report" in prof_md

    score_md = build_provider_benchmark_score_markdown_report({"total_providers_scored": 5, "mean_benchmark_score": 0.88})
    assert "Provider Benchmark Score Report" in score_md

    handoff_md = build_phase_116_handoff_markdown_report({"total_handoff_items": 7})
    assert "Phase 116" in handoff_md
