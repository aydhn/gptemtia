import pytest
from decisions.decision_labels import (
    list_decision_labels,
    list_decision_reason_labels,
    validate_decision_label,
    is_directional_decision,
    is_no_trade_decision,
    is_warning_decision,
)


def test_list_labels():
    labels = list_decision_labels()
    assert len(labels) > 0
    assert "long_bias_candidate" in labels


def test_validate_decision_label():
    validate_decision_label("long_bias_candidate")
    with pytest.raises(ValueError):
        validate_decision_label("BUY")


def test_is_directional_decision():
    assert is_directional_decision("long_bias_candidate") is True
    assert is_directional_decision("short_bias_candidate") is True
    assert is_directional_decision("neutral_candidate") is False


def test_is_no_trade_decision():
    assert is_no_trade_decision("no_trade_candidate") is True
