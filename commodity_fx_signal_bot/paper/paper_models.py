from dataclasses import dataclass, field
import hashlib

@dataclass
class VirtualOrder:
    order_id: str
    symbol: str
    timeframe: str
    created_timestamp: str
    expiry_timestamp: str | None
    source_level_id: str
    source_sizing_id: str
    source_risk_id: str
    strategy_family: str
    order_side: str
    order_status: str
    requested_price: float | None
    theoretical_units: float
    adjusted_theoretical_units: float
    theoretical_notional: float | None
    stop_level: float | None
    target_level: float | None
    risk_label: str
    sizing_label: str
    level_label: str
    rejection_reasons: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    notes: str = ""

@dataclass
class VirtualPosition:
    position_id: str
    order_id: str
    symbol: str
    timeframe: str
    opened_timestamp: str | None
    closed_timestamp: str | None
    order_side: str
    position_status: str
    entry_price: float | None
    exit_price: float | None
    units: float
    notional: float | None
    stop_level: float | None
    target_level: float | None
    gross_pnl: float | None
    fee_cost: float
    slippage_cost: float
    net_pnl: float | None
    return_pct: float | None
    holding_bars: int
    exit_reason: str
    result_label: str
    warnings: list[str] = field(default_factory=list)
    notes: str = ""

@dataclass
class VirtualPortfolioSnapshot:
    timestamp: str
    cash_balance: float
    equity: float
    open_position_count: int
    closed_position_count: int
    unrealized_pnl: float
    realized_pnl: float
    total_fees: float
    total_slippage: float
    exposure_notional: float
    drawdown_pct: float
    warnings: list[str] = field(default_factory=list)

def build_virtual_order_id(symbol: str, timeframe: str, timestamp: str, source_level_id: str) -> str:
    raw = f"{symbol}_{timeframe}_{timestamp}_{source_level_id}"
    return "vo_" + hashlib.md5(raw.encode()).hexdigest()[:12]

def build_virtual_position_id(order_id: str) -> str:
    return "vp_" + hashlib.md5(order_id.encode()).hexdigest()[:12]

def virtual_order_to_dict(order: VirtualOrder) -> dict:
    return {
        "order_id": order.order_id,
        "symbol": order.symbol,
        "timeframe": order.timeframe,
        "created_timestamp": order.created_timestamp,
        "expiry_timestamp": order.expiry_timestamp,
        "source_level_id": order.source_level_id,
        "source_sizing_id": order.source_sizing_id,
        "source_risk_id": order.source_risk_id,
        "strategy_family": order.strategy_family,
        "order_side": order.order_side,
        "order_status": order.order_status,
        "requested_price": order.requested_price,
        "theoretical_units": order.theoretical_units,
        "adjusted_theoretical_units": order.adjusted_theoretical_units,
        "theoretical_notional": order.theoretical_notional,
        "stop_level": order.stop_level,
        "target_level": order.target_level,
        "risk_label": order.risk_label,
        "sizing_label": order.sizing_label,
        "level_label": order.level_label,
        "rejection_reasons": ";".join(order.rejection_reasons) if order.rejection_reasons else "",
        "warnings": ";".join(order.warnings) if order.warnings else "",
        "notes": order.notes
    }

def virtual_position_to_dict(position: VirtualPosition) -> dict:
    return {
        "position_id": position.position_id,
        "order_id": position.order_id,
        "symbol": position.symbol,
        "timeframe": position.timeframe,
        "opened_timestamp": position.opened_timestamp,
        "closed_timestamp": position.closed_timestamp,
        "order_side": position.order_side,
        "position_status": position.position_status,
        "entry_price": position.entry_price,
        "exit_price": position.exit_price,
        "units": position.units,
        "notional": position.notional,
        "stop_level": position.stop_level,
        "target_level": position.target_level,
        "gross_pnl": position.gross_pnl,
        "fee_cost": position.fee_cost,
        "slippage_cost": position.slippage_cost,
        "net_pnl": position.net_pnl,
        "return_pct": position.return_pct,
        "holding_bars": position.holding_bars,
        "exit_reason": position.exit_reason,
        "result_label": position.result_label,
        "warnings": ";".join(position.warnings) if position.warnings else "",
        "notes": position.notes
    }

def virtual_portfolio_snapshot_to_dict(snapshot: VirtualPortfolioSnapshot) -> dict:
    return {
        "timestamp": snapshot.timestamp,
        "cash_balance": snapshot.cash_balance,
        "equity": snapshot.equity,
        "open_position_count": snapshot.open_position_count,
        "closed_position_count": snapshot.closed_position_count,
        "unrealized_pnl": snapshot.unrealized_pnl,
        "realized_pnl": snapshot.realized_pnl,
        "total_fees": snapshot.total_fees,
        "total_slippage": snapshot.total_slippage,
        "exposure_notional": snapshot.exposure_notional,
        "drawdown_pct": snapshot.drawdown_pct,
        "warnings": ";".join(snapshot.warnings) if snapshot.warnings else ""
    }
