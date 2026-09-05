from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.provider_benchmark_validation import (
    build_provider_benchmark_validation_report,
    validate_no_forbidden_benchmark_claims,
)
from advanced_provider_benchmark.provider_benchmark_profile_registry import (
    build_provider_benchmark_profile_registry,
)
from advanced_provider_benchmark.provider_benchmark_metric_registry import (
    build_provider_benchmark_metric_registry,
)
from advanced_provider_benchmark.provider_benchmark_scoring import (
    build_provider_benchmark_score_report,
)
from advanced_provider_benchmark.provider_ranking_research import (
    build_provider_ranking_research_report,
)
from advanced_provider_benchmark.provider_benchmark_manual_review_queue import (
    build_provider_benchmark_manual_review_queue,
)
from advanced_provider_benchmark.provider_benchmark_safety_boundary import (
    build_provider_benchmark_safety_boundary,
)


def test_provider_benchmark_validation():
    profile = get_default_provider_benchmark_profile()
    prof_df, _ = build_provider_benchmark_profile_registry(profile)
    met_df, _ = build_provider_benchmark_metric_registry(profile)
    scr_df, _ = build_provider_benchmark_score_report(profile)
    rnk_df, _ = build_provider_ranking_research_report(profile)
    rev_df, _ = build_provider_benchmark_manual_review_queue(None, profile)
    safe_df, _ = build_provider_benchmark_safety_boundary(profile)

    tables = {
        "profiles": prof_df,
        "metrics": met_df,
        "scores": scr_df,
        "ranking": rnk_df,
        "manual_review": rev_df,
        "safety": safe_df,
    }
    df, summary = build_provider_benchmark_validation_report(tables, profile)

    assert not df.empty
    assert summary["validation_status"] == "VALID"
    assert summary["forbidden_claims_found"] is False
    assert summary["scores_valid"] is True
    assert summary["current_phase"] == 115
    assert summary["target_final_phase"] == 160


def test_validate_forbidden_claims():
    assert validate_no_forbidden_benchmark_claims(summary={"official_approval_guarantee": True})["valid"] is False
    assert validate_no_forbidden_benchmark_claims(summary={"production_ready_guarantee": True})["valid"] is False
    assert validate_no_forbidden_benchmark_claims(summary={"broker_ready_guarantee": True})["valid"] is False
