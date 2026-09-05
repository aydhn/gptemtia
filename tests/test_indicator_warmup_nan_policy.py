from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile
from advanced_technical_indicators.indicator_warmup_nan_policy import (
    build_indicator_warmup_nan_policy_registry,
    estimate_warmup_nan_count,
    summarize_indicator_warmup_nan_policy,
)


def test_indicator_warmup_nan_policy():
    prof = get_default_technical_indicator_profile()
    df, summary = build_indicator_warmup_nan_policy_registry(prof)
    assert not df.empty
    assert summary["policy_action"] == "preserve_nan"

    assert estimate_warmup_nan_count("sma", {"window": 20}) == 19
    assert estimate_warmup_nan_count("rsi", {"window": 14}) == 14
    assert estimate_warmup_nan_count("candle_body_size", {}) == 0
    assert estimate_warmup_nan_count("true_range", {}) == 1
