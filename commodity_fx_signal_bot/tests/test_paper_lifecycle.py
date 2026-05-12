import pytest
import pandas as pd
from paper.paper_lifecycle import PaperLifecycleEngine
from paper.paper_config import get_default_paper_trading_profile
from paper.virtual_order_book import VirtualOrderBook
from paper.virtual_portfolio import VirtualPortfolio
from paper.paper_models import VirtualOrder

def test_paper_lifecycle():
    profile = get_default_paper_trading_profile()
    engine = PaperLifecycleEngine(profile)
    ob = VirtualOrderBook()
    port = VirtualPortfolio(100000.0)

    order = VirtualOrder(
        order_id="o1", symbol="GC=F", timeframe="1d", created_timestamp="2024-01-01",
        expiry_timestamp=None, source_level_id="l1", source_sizing_id="s1",
        source_risk_id="r1", strategy_family="f1", order_side="virtual_long_bias",
        order_status="virtual_pending", requested_price=100.0, theoretical_units=1.0,
        adjusted_theoretical_units=1.0, theoretical_notional=100.0, stop_level=90.0,
        target_level=110.0, risk_label="r", sizing_label="s", level_label="l"
    )

    # 1. Process new order
    ts1 = pd.to_datetime("2024-01-01")
    price_df = pd.DataFrame(
        {'open': [100.0, 102.0], 'high': [105.0, 105.0], 'low': [95.0, 95.0], 'close': [101.0, 103.0], 'symbol': ['GC=F', 'GC=F']},
        index=pd.to_datetime(['2024-01-01', '2024-01-02'])
    )

    res1 = engine.process_timestamp(ts1, price_df, [order], ob, port)
    assert len(ob.get_active_orders()) == 0

    # 2. Next bar, order should fill
    ts2 = pd.to_datetime("2024-01-02")
    res2 = engine.process_timestamp(ts2, price_df, [], ob, port)

    # After ts2 process, order should be filled (on open of ts2 normally)
    assert len(ob.get_active_orders()) == 0
    assert len(port.get_open_positions()) == 1
