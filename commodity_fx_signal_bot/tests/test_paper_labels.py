import pytest
from paper.paper_labels import (
    list_virtual_order_statuses,
    list_virtual_order_sides,
    list_virtual_position_statuses,
    list_virtual_exit_reasons,
    list_paper_result_labels,
    validate_virtual_order_status,
    validate_virtual_position_status,
    validate_virtual_exit_reason
)

def test_label_lists_not_empty():
    assert len(list_virtual_order_statuses()) > 0
    assert len(list_virtual_order_sides()) > 0
    assert len(list_virtual_position_statuses()) > 0
    assert len(list_virtual_exit_reasons()) > 0
    assert len(list_paper_result_labels()) > 0

def test_validate_order_status():
    validate_virtual_order_status("virtual_pending")
    with pytest.raises(ValueError):
        validate_virtual_order_status("real_pending")

def test_validate_position_status():
    validate_virtual_position_status("virtual_open")
    with pytest.raises(ValueError):
        validate_virtual_position_status("live_open")

def test_validate_exit_reason():
    validate_virtual_exit_reason("virtual_target_touch")
    with pytest.raises(ValueError):
        validate_virtual_exit_reason("real_target_hit")
