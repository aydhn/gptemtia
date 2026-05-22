import pytest
from synthetic_indices.index_labels import (
    list_synthetic_index_type_labels,
    list_weighting_scheme_labels,
    list_relative_strength_labels,
    list_rotation_labels,
    validate_synthetic_index_type,
    validate_relative_strength_label,
    validate_rotation_label,
    LabelError
)

def test_label_lists_not_empty():
    assert len(list_synthetic_index_type_labels()) > 0
    assert len(list_weighting_scheme_labels()) > 0
    assert len(list_relative_strength_labels()) > 0
    assert len(list_rotation_labels()) > 0

def test_validate_synthetic_index_type():
    validate_synthetic_index_type("metals_composite_index")
    with pytest.raises(LabelError):
        validate_synthetic_index_type("invalid_label")

def test_validate_relative_strength_label():
    validate_relative_strength_label("strong_leader")
    with pytest.raises(LabelError):
        validate_relative_strength_label("invalid_label")

def test_no_trade_signals_in_labels():
    # Ensure leader/laggard are not trade signals
    with pytest.raises(LabelError):
        validate_relative_strength_label("buy_leader")
    with pytest.raises(LabelError):
        validate_rotation_label("trade_rotation")
