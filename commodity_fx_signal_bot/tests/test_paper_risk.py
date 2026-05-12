import pytest
from paper.paper_risk import check_virtual_order_risk, build_paper_risk_audit
from paper.paper_config import get_default_paper_trading_profile
from paper.paper_models import VirtualOrder
from paper.virtual_portfolio import VirtualPortfolio

def test_paper_risk():
    profile = get_default_paper_trading_profile()
    port = VirtualPortfolio(100000.0)

    order = VirtualOrder(
        order_id="o1", symbol="GC=F", timeframe="1d", created_timestamp="2024-01-01",
        expiry_timestamp=None, source_level_id="l1", source_sizing_id="s1",
        source_risk_id="r1", strategy_family="f1", order_side="virtual_long_bias",
        order_status="virtual_pending", requested_price=100.0, theoretical_units=1.0,
        adjusted_theoretical_units=1.0, theoretical_notional=100.0, stop_level=90.0,
        target_level=110.0, risk_label="r", sizing_label="s", level_label="l"
    )

    res = check_virtual_order_risk(order, port, profile)
    assert res["passed"]

    audit = build_paper_risk_audit(order, port, profile)
    assert audit["passed"]
    assert audit["current_equity"] == 100000.0
