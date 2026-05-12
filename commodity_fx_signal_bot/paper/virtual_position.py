import pandas as pd
from paper.paper_models import VirtualOrder, VirtualPosition, build_virtual_position_id
from paper.paper_config import PaperTradingProfile

def open_virtual_position_from_order(order: VirtualOrder, fill_info: dict, profile: PaperTradingProfile) -> VirtualPosition:
    entry_price = order.requested_price
    if entry_price is None or entry_price <= 0:
        entry_price = 1.0 # Safe fallback

    actual_notional = entry_price * order.adjusted_theoretical_units
    fee = actual_notional * (profile.fee_bps / 10000.0)

    pos = VirtualPosition(
        position_id=build_virtual_position_id(order.order_id),
        order_id=order.order_id,
        symbol=order.symbol,
        timeframe=order.timeframe,
        opened_timestamp=order.notes.split(" Filled at ")[-1].split(" price ")[0] if " Filled at " in order.notes else order.created_timestamp,
        closed_timestamp=None,
        order_side=order.order_side,
        position_status="virtual_open",
        entry_price=entry_price,
        exit_price=None,
        units=order.adjusted_theoretical_units,
        notional=actual_notional,
        stop_level=order.stop_level,
        target_level=order.target_level,
        gross_pnl=0.0,
        fee_cost=fee,
        slippage_cost=0.0,
        net_pnl=0.0,
        return_pct=0.0,
        holding_bars=0,
        exit_reason="",
        result_label="virtual_unknown_result",
        warnings=[],
        notes="Generated via virtual execution."
    )
    return pos

def update_virtual_position_mark_to_market(position: VirtualPosition, bar: pd.Series) -> dict:
    if position.position_status != "virtual_open" or pd.isna(bar.get('close')):
        return {}

    current_price = float(bar['close'])
    direction = 1 if position.order_side == "virtual_long_bias" else -1

    if position.entry_price and position.entry_price > 0:
        price_diff = current_price - position.entry_price
        position.gross_pnl = price_diff * position.units * direction
        position.net_pnl = position.gross_pnl - position.fee_cost - position.slippage_cost
        position.return_pct = (position.net_pnl / position.notional) if position.notional else 0.0

    return {"unrealized_pnl": position.net_pnl}

def check_virtual_position_exit(position: VirtualPosition, bar: pd.Series, profile: PaperTradingProfile) -> dict:
    result = {}
    if position.position_status != "virtual_open":
        return result

    position.holding_bars += 1

    high = float(bar.get('high', bar.get('close')))
    low = float(bar.get('low', bar.get('close')))
    close = float(bar.get('close'))

    hit_stop = False
    hit_target = False

    if position.order_side == "virtual_long_bias":
        if position.stop_level and low <= position.stop_level: hit_stop = True
        if position.target_level and high >= position.target_level: hit_target = True
    elif position.order_side == "virtual_short_bias":
        if position.stop_level and high >= position.stop_level: hit_stop = True
        if position.target_level and low <= position.target_level: hit_target = True

    if hit_stop and hit_target:
        position.warnings.append("Intrabar ambiguity: both stop and target hit.")
        hit_target = False # Conservative approach

    if hit_stop:
        result['exit'] = True
        result['reason'] = "virtual_stop_touch"
        result['price'] = position.stop_level
    elif hit_target:
        result['exit'] = True
        result['reason'] = "virtual_target_touch"
        result['price'] = position.target_level
    elif position.holding_bars >= profile.max_holding_bars:
        result['exit'] = True
        result['reason'] = "virtual_max_holding"
        result['price'] = close

    return result

def close_virtual_position(position: VirtualPosition, exit_timestamp: str, exit_price: float, exit_reason: str, profile: PaperTradingProfile) -> VirtualPosition:
    position.position_status = "virtual_closed"
    position.closed_timestamp = exit_timestamp
    position.exit_price = exit_price
    position.exit_reason = exit_reason

    pnl_info = calculate_virtual_position_pnl(position, exit_price, profile)
    position.gross_pnl = pnl_info['gross_pnl']
    position.fee_cost += pnl_info['exit_fee']
    position.net_pnl = position.gross_pnl - position.fee_cost - position.slippage_cost
    if position.notional and position.notional > 0:
        position.return_pct = position.net_pnl / position.notional
    else:
        position.return_pct = 0.0

    if position.net_pnl > 0:
        position.result_label = "virtual_win"
    elif position.net_pnl < 0:
        position.result_label = "virtual_loss"
    else:
        position.result_label = "virtual_breakeven"

    return position

def calculate_virtual_position_pnl(position: VirtualPosition, exit_price: float, profile: PaperTradingProfile) -> dict:
    direction = 1 if position.order_side == "virtual_long_bias" else -1

    entry_price = position.entry_price if position.entry_price else exit_price
    gross_pnl = (exit_price - entry_price) * position.units * direction

    exit_notional = exit_price * position.units
    exit_fee = exit_notional * (profile.fee_bps / 10000.0)

    return {
        "gross_pnl": gross_pnl,
        "exit_fee": exit_fee
    }
