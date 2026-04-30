import pytest
from indicators.indicator_config import (
    list_indicator_specs,
    get_indicator_spec,
    validate_indicator_specs,
)


def test_validate_indicator_specs():
    errors = validate_indicator_specs()
    assert len(errors) == 0, f"Indicator specs validation failed: {errors}"


def test_list_indicator_specs_contains_mean_reversion_advanced():
    specs = list_indicator_specs()
    names = [s.name for s in specs]
    assert "multi_zscore_close" in names
    assert "multi_sma_distance" in names
    assert "compact_mean_reversion_feature_set" in names
    assert "mean_reversion_event_frame" in names
