import pytest
from advanced_provider_benchmark.provider_benchmark_config import (
    ProviderBenchmarkProfile,
    get_provider_benchmark_profile,
    list_provider_benchmark_profiles,
    validate_provider_benchmark_profiles,
    get_default_provider_benchmark_profile,
    ConfigError,
)


def test_provider_benchmark_profiles():
    validate_provider_benchmark_profiles()
    profiles = list_provider_benchmark_profiles()
    assert len(profiles) >= 3

    default_prof = get_default_provider_benchmark_profile()
    assert default_prof.name == "balanced_local_provider_benchmark"
    assert default_prof.current_phase == 115
    assert default_prof.target_final_phase == 160
    assert default_prof.next_phase == 116
    assert default_prof.local_only is True
    assert default_prof.non_production is True
    assert default_prof.research_only is True
    assert default_prof.dry_run_default is True
    assert default_prof.allow_live_trading is False
    assert default_prof.allow_broker_integration is False
    assert default_prof.allow_real_order is False
    assert default_prof.allow_investment_advice is False
    assert default_prof.allow_score_as_signal is False
    assert default_prof.allow_official_approval_claim is False
    assert default_prof.allow_production_ready_claim is False
    assert default_prof.allow_broker_ready_claim is False
    assert default_prof.allow_web_scraping is False
    assert default_prof.allow_credential_output is False
    assert default_prof.allow_source_overwrite is False
    assert default_prof.allow_auto_destructive_cleaning is False


def test_unknown_profile_raises():
    with pytest.raises(ConfigError):
        get_provider_benchmark_profile("non_existent_profile_xyz")
