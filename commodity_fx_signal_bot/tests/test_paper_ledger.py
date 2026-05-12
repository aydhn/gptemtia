import pytest
from paper.paper_ledger import PaperLedger
from paper.paper_models import VirtualOrder

def test_paper_ledger():
    ledger = PaperLedger()
    order = VirtualOrder(
        order_id="o1", symbol="GC=F", timeframe="1d", created_timestamp="2024-01-01",
        expiry_timestamp=None, source_level_id="l1", source_sizing_id="s1",
        source_risk_id="r1", strategy_family="f1", order_side="virtual_long_bias",
        order_status="virtual_pending", requested_price=100.0, theoretical_units=1.0,
        adjusted_theoretical_units=1.0, theoretical_notional=100.0, stop_level=90.0,
        target_level=110.0, risk_label="r", sizing_label="s", level_label="l"
    )

    ledger.add_order_event(order, "virtual_order_created", "2024-01-01")
    df = ledger.to_dataframe()
    assert not df.empty

    summ = ledger.summarize()
    assert summ["total_events"] == 1
