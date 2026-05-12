import pytest
from paper.paper_models import VirtualOrder, VirtualPosition, VirtualPortfolioSnapshot
from paper.paper_models import build_virtual_order_id, build_virtual_position_id
from paper.paper_models import virtual_order_to_dict, virtual_position_to_dict, virtual_portfolio_snapshot_to_dict

def test_build_ids_deterministic():
    id1 = build_virtual_order_id("GC=F", "1d", "2024-01-01", "level_1")
    id2 = build_virtual_order_id("GC=F", "1d", "2024-01-01", "level_1")
    assert id1 == id2
    assert id1.startswith("vo_")

    pid1 = build_virtual_position_id(id1)
    pid2 = build_virtual_position_id(id2)
    assert pid1 == pid2
    assert pid1.startswith("vp_")

def test_to_dict_methods():
    order = VirtualOrder(
        order_id="o1", symbol="GC=F", timeframe="1d", created_timestamp="2024-01-01",
        expiry_timestamp=None, source_level_id="l1", source_sizing_id="s1",
        source_risk_id="r1", strategy_family="f1", order_side="virtual_long_bias",
        order_status="virtual_pending", requested_price=100.0, theoretical_units=1.0,
        adjusted_theoretical_units=1.0, theoretical_notional=100.0, stop_level=90.0,
        target_level=110.0, risk_label="r", sizing_label="s", level_label="l"
    )
    d = virtual_order_to_dict(order)
    assert d["order_id"] == "o1"

    pos = VirtualPosition(
        position_id="p1", order_id="o1", symbol="GC=F", timeframe="1d",
        opened_timestamp="2024-01-01", closed_timestamp=None, order_side="virtual_long_bias",
        position_status="virtual_open", entry_price=100.0, exit_price=None,
        units=1.0, notional=100.0, stop_level=90.0, target_level=110.0,
        gross_pnl=0.0, fee_cost=5.0, slippage_cost=0.0, net_pnl=-5.0,
        return_pct=0.0, holding_bars=1, exit_reason="", result_label="virtual_unknown"
    )
    pd = virtual_position_to_dict(pos)
    assert pd["position_id"] == "p1"
