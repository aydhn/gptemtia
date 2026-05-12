import pytest
import pandas as pd
from paper.virtual_position import open_virtual_position_from_order, check_virtual_position_exit, update_virtual_position_mark_to_market
from paper.paper_config import get_default_paper_trading_profile
from paper.paper_models import VirtualOrder

@pytest.fixture
def profile():
    return get_default_paper_trading_profile()

@pytest.fixture
def order():
    return VirtualOrder(
        order_id="o1", symbol="GC=F", timeframe="1d", created_timestamp="2024-01-01",
        expiry_timestamp=None, source_level_id="l1", source_sizing_id="s1",
        source_risk_id="r1", strategy_family="f1", order_side="virtual_long_bias",
        order_status="virtual_filled", requested_price=100.0, theoretical_units=1.0,
        adjusted_theoretical_units=1.0, theoretical_notional=100.0, stop_level=90.0,
        target_level=110.0, risk_label="r", sizing_label="s", level_label="l"
    )

def test_position_lifecycle(order, profile):
    pos = open_virtual_position_from_order(order, {}, profile)
    assert pos.position_status == "virtual_open"
    assert pos.entry_price == 100.0

    # MTM
    bar_mtm = pd.Series({'close': 105.0})
    update_virtual_position_mark_to_market(pos, bar_mtm)
    assert pos.gross_pnl == 5.0

    # Check target touch
    bar_exit = pd.Series({'high': 115.0, 'low': 105.0, 'close': 110.0})
    exit_res = check_virtual_position_exit(pos, bar_exit, profile)
    assert exit_res.get('exit')
    assert exit_res.get('reason') == "virtual_target_touch"

def test_intrabar_ambiguity(order, profile):
    pos = open_virtual_position_from_order(order, {}, profile)
    bar = pd.Series({'high': 120.0, 'low': 80.0, 'close': 100.0}) # both stop and target touched

    exit_res = check_virtual_position_exit(pos, bar, profile)
    assert exit_res.get('exit')
    assert exit_res.get('reason') == "virtual_stop_touch" # conservative assumption
    assert len(pos.warnings) > 0
