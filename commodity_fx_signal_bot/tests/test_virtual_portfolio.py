import pytest
from paper.virtual_portfolio import VirtualPortfolio
from paper.paper_config import get_default_paper_trading_profile
from paper.paper_models import VirtualPosition

def test_virtual_portfolio():
    profile = get_default_paper_trading_profile()
    port = VirtualPortfolio(100000.0)

    can_open, reasons = port.can_open_position("GC=F", profile)
    assert can_open

    pos = VirtualPosition(
        position_id="p1", order_id="o1", symbol="GC=F", timeframe="1d",
        opened_timestamp="2024-01-01", closed_timestamp=None, order_side="virtual_long_bias",
        position_status="virtual_open", entry_price=100.0, exit_price=None,
        units=1.0, notional=100.0, stop_level=90.0, target_level=110.0,
        gross_pnl=0.0, fee_cost=5.0, slippage_cost=0.0, net_pnl=-5.0,
        return_pct=0.0, holding_bars=1, exit_reason="", result_label="virtual_unknown"
    )

    port.open_position(pos)
    assert port.cash_balance < 100000.0 # fee deducted

    # max open positions limit
    profile_strict = get_default_paper_trading_profile()
    # Mock it as frozen via dataclass replace
    from dataclasses import replace
    profile_strict = replace(profile_strict, max_open_positions_per_symbol=1)

    can_open_again, reasons = port.can_open_position("GC=F", profile_strict)
    assert not can_open_again
    assert len(reasons) > 0

    # Close
    pos.net_pnl = 10.0
    port.close_position(pos)
    assert len(port.get_open_positions()) == 0
    assert len(port.get_closed_positions()) == 1

    # Mark to market
    port.mark_to_market("2024-01-02", {})
    df = port.to_equity_curve_dataframe()
    assert not df.empty

    summary = port.summarize()
    assert summary["closed_positions"] == 1
