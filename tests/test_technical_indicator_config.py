import pytest
from advanced_technical_indicators.technical_indicator_config import (
    TechnicalIndicatorProfile,
    get_technical_indicator_profile,
    list_technical_indicator_profiles,
    validate_technical_indicator_profiles,
    get_default_technical_indicator_profile,
    ConfigError,
)


def test_technical_indicator_config():
    validate_technical_indicator_profiles()
    profiles = list_technical_indicator_profiles()
    assert len(profiles) >= 3

    default_prof = get_default_technical_indicator_profile()
    assert default_prof.name == "balanced_local_technical_indicators"
    assert default_prof.current_phase == 117
    assert default_prof.target_final_phase == 160
    assert default_prof.next_phase == 118
    assert default_prof.local_only is True
    assert default_prof.non_production is True
    assert default_prof.research_only is True
    assert default_prof.allow_indicator_as_signal is False
    assert default_prof.allow_live_trading is False
    assert default_prof.allow_broker_integration is False


def test_unknown_profile_error():
    with pytest.raises(ConfigError):
        get_technical_indicator_profile("non_existent_profile_12345")
