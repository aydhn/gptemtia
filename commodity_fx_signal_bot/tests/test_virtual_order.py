import pytest
from paper.paper_models import VirtualOrder
from paper.virtual_order import validate_virtual_order, reject_virtual_order, expire_virtual_order, mark_virtual_order_filled, virtual_order_is_active

@pytest.fixture
def mock_order():
    return VirtualOrder(
        order_id="o1", symbol="GC=F", timeframe="1d", created_timestamp="2024-01-01",
        expiry_timestamp=None, source_level_id="l1", source_sizing_id="s1",
        source_risk_id="r1", strategy_family="f1", order_side="virtual_long_bias",
        order_status="virtual_pending", requested_price=100.0, theoretical_units=1.0,
        adjusted_theoretical_units=1.0, theoretical_notional=100.0, stop_level=90.0,
        target_level=110.0, risk_label="r", sizing_label="s", level_label="l"
    )

def test_validate_order(mock_order):
    w = validate_virtual_order(mock_order)
    assert not w

    mock_order.adjusted_theoretical_units = 0.0
    w2 = validate_virtual_order(mock_order)
    assert "units" in w2

def test_order_transitions(mock_order):
    assert virtual_order_is_active(mock_order)

    reject_virtual_order(mock_order, ["test"])
    assert mock_order.order_status == "virtual_rejected"
    assert "test" in mock_order.rejection_reasons

    expire_virtual_order(mock_order, "2024-01-02", "test exp")
    assert mock_order.order_status == "virtual_expired"
    assert mock_order.expiry_timestamp == "2024-01-02"

    mark_virtual_order_filled(mock_order, "2024-01-03", 101.0)
    assert mock_order.order_status == "virtual_filled"
    assert mock_order.requested_price == 101.0
