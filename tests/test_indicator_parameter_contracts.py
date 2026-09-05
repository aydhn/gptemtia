from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile
from advanced_technical_indicators.indicator_parameter_contracts import (
    build_indicator_parameter_contract_registry,
    validate_indicator_window,
    validate_indicator_parameters,
    summarize_indicator_parameter_contracts,
)


def test_indicator_parameter_contracts():
    prof = get_default_technical_indicator_profile()
    df, summary = build_indicator_parameter_contract_registry(prof)
    assert not df.empty
    assert summary["total_parameter_contracts"] >= 15

    # Window validation
    res_valid = validate_indicator_window(20)
    assert res_valid["valid"] is True

    res_invalid_low = validate_indicator_window(1, min_window=2)
    assert res_invalid_low["valid"] is False

    res_invalid_high = validate_indicator_window(1001, max_window=1000)
    assert res_invalid_high["valid"] is False

    # Parameter validation
    p_valid = validate_indicator_parameters("sma", {"window": 20})
    assert p_valid["valid"] is True

    p_invalid = validate_indicator_parameters("sma", {"window": 0})
    assert p_invalid["valid"] is False
