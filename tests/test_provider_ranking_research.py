from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.provider_ranking_research import (
    build_provider_ranking_research_report,
    summarize_provider_ranking_research,
)


def test_provider_ranking_research():
    profile = get_default_provider_benchmark_profile()
    df, summary = build_provider_ranking_research_report(profile)

    assert not df.empty
    assert "research_rank" in df.columns
    assert "research_tier" in df.columns
    assert (df["official_approval"] == False).all()
    assert summary["official_approval_guarantee"] is False
    assert summary["production_ready_guarantee"] is False
    assert summary["current_phase"] == 115
    assert summary["target_final_phase"] == 160
