from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.rolling_window_contracts import (
    build_rolling_window_contract_registry,
    validate_rolling_window,
    summarize_rolling_window_contracts,
    STANDARD_ROLLING_WINDOWS,
)


def test_rolling_window_contracts():
    profile = get_default_feature_engine_profile()
    df, summary = build_rolling_window_contract_registry(profile)

    assert not df.empty
    assert len(df) == len(STANDARD_ROLLING_WINDOWS)
    assert summary["all_lookahead_guarded"] is True

    # Validate window helper
    assert validate_rolling_window(20)["valid"] is True
    assert validate_rolling_window(1)["valid"] is False
    assert validate_rolling_window("20")["valid"] is False
