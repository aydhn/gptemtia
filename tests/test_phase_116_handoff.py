from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.phase_116_handoff import (
    build_phase_116_indicator_feature_factor_engine_handoff_report,
    summarize_phase_116_handoff,
)


def test_phase_116_handoff():
    profile = get_default_provider_benchmark_profile()
    df, summary = build_phase_116_indicator_feature_factor_engine_handoff_report(profile)

    assert not df.empty
    assert len(df) >= 7
    assert "feature_engine_input_area" in df.columns
    assert "source_provider_domain" in df.columns
    assert "required_benchmark_input" in df.columns
    assert summary["target_phase"] == 116
    assert summary["readiness_status"] == "READY"
    assert summary["current_phase"] == 115
    assert summary["target_final_phase"] == 160
