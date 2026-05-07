import pytest
from backtesting.backtest_labels import (
    list_trade_lifecycle_statuses,
    list_entry_reason_labels,
    list_exit_reason_labels,
    list_backtest_result_labels,
    validate_lifecycle_status,
    validate_entry_reason,
    validate_exit_reason,
    validate_backtest_result,
)


def test_list_labels_not_empty():
    assert len(list_trade_lifecycle_statuses()) > 0
    assert len(list_entry_reason_labels()) > 0
    assert len(list_exit_reason_labels()) > 0
    assert len(list_backtest_result_labels()) > 0


def test_validate_labels():
    validate_lifecycle_status("simulated_open")
    with pytest.raises(ValueError):
        validate_lifecycle_status("invalid")

    validate_entry_reason("candidate_entry")
    with pytest.raises(ValueError):
        validate_entry_reason("invalid")
