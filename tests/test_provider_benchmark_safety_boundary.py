from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.provider_benchmark_safety_boundary import (
    build_provider_benchmark_safety_boundary,
    build_provider_benchmark_no_go_conditions,
    build_provider_benchmark_safe_go_conditions,
    summarize_provider_benchmark_safety_boundary,
)


def test_provider_benchmark_safety_boundary():
    profile = get_default_provider_benchmark_profile()
    df, summary = build_provider_benchmark_safety_boundary(profile)

    assert not df.empty
    assert summary["safety_status"] == "ACTIVE"
    assert summary["total_no_go_rules"] >= 30
    assert summary["total_safe_go_rules"] >= 15
    assert summary["all_no_go_enforced"] is True
    assert summary["current_phase"] == 115
    assert summary["target_final_phase"] == 160

    no_go = build_provider_benchmark_no_go_conditions(profile)
    assert not no_go.empty
    assert (no_go["enforced"] == True).all()

    safe_go = build_provider_benchmark_safe_go_conditions(profile)
    assert not safe_go.empty
    assert (safe_go["permitted"] == True).all()
