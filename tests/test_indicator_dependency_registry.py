from advanced_technical_indicators.indicator_dependency_registry import (
    build_indicator_dependency_registry,
    summarize_indicator_dependency_registry,
)
from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile


def test_indicator_dependency_registry():
    prof = get_default_technical_indicator_profile()
    df, summary = build_indicator_dependency_registry(prof)
    assert not df.empty
    assert summary["total_dependency_mappings"] >= 8
    assert "atr" in df["target_indicator"].values
    assert "macd" in df["target_indicator"].values
