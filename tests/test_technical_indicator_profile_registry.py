from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile
from advanced_technical_indicators.technical_indicator_profile_registry import build_technical_indicator_profile_registry


def test_technical_indicator_profile_registry():
    prof = get_default_technical_indicator_profile()
    df, summary = build_technical_indicator_profile_registry(prof)

    assert not df.empty
    assert len(df) >= 3
    assert summary["current_phase"] == 117
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 118
    assert summary["non_signal_guaranteed"] is True
