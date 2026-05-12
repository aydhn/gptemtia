import pytest
import pandas as pd
from paper.virtual_execution import VirtualExecutionSimulator
from paper.paper_config import get_default_paper_trading_profile
from paper.paper_models import VirtualOrder

@pytest.fixture
def simulator():
    return VirtualExecutionSimulator(get_default_paper_trading_profile())

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

def test_simulate_order_fill(simulator, mock_order):
    price_df = pd.DataFrame(
        {'open': [100.0, 102.0], 'close': [101.0, 103.0]},
        index=pd.to_datetime(['2024-01-01', '2024-01-02'])
    )

    filled, w = simulator.simulate_order_fill(mock_order, price_df, pd.to_datetime('2024-01-01'))
    assert filled.order_status == "virtual_filled"
    # Slippage applied
    assert filled.requested_price > 102.0

def test_simulate_order_fill_no_data(simulator, mock_order):
    price_df = pd.DataFrame(
        {'open': [100.0], 'close': [101.0]},
        index=pd.to_datetime(['2024-01-01'])
    )

    filled, w = simulator.simulate_order_fill(mock_order, price_df, pd.to_datetime('2024-01-01'))
    assert filled.order_status == "virtual_expired"
