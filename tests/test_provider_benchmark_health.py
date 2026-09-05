from pathlib import Path
from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.provider_benchmark_health import (
    build_provider_benchmark_health_check,
    summarize_provider_benchmark_health,
)


def test_provider_benchmark_health():
    project_root = Path(__file__).resolve().parent.parent
    profile = get_default_provider_benchmark_profile()
    df, summary = build_provider_benchmark_health_check(project_root, profile)

    assert not df.empty
    assert summary["overall_status"] == "PASS"
    assert summary["failed_checks"] == 0
    assert summary["current_phase"] == 115
    assert summary["target_final_phase"] == 160
