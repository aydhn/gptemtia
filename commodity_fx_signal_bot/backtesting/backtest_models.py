from dataclasses import dataclass, asdict
import hashlib


@dataclass
class SimulatedTrade:
    symbol: str
    timeframe: str
    trade_id: str
    source_level_id: str
    source_sizing_id: str
    source_risk_id: str
    strategy_family: str
    directional_bias: str
    entry_timestamp: str | None
    entry_price: float | None
    exit_timestamp: str | None
    exit_price: float | None
    theoretical_stop_level: float | None
    theoretical_target_level: float | None
    theoretical_units: float
    adjusted_theoretical_units: float
    theoretical_notional: float | None
    gross_pnl: float | None
    fee_cost: float
    slippage_cost: float
    net_pnl: float | None
    return_pct: float | None
    holding_bars: int
    lifecycle_status: str
    entry_reason: str
    exit_reason: str
    result_label: str
    warnings: list[str]
    notes: str = ""


@dataclass
class BacktestRunSummary:
    run_id: str
    profile_name: str
    symbol_count: int
    trade_count: int
    initial_equity: float
    final_equity: float
    total_return_pct: float
    win_rate: float
    avg_trade_return: float
    max_drawdown_pct: float
    profit_factor: float
    warnings: list[str]


def build_backtest_run_id(profile_name: str, timeframe: str, symbols: list[str]) -> str:
    sorted_symbols = sorted(symbols)
    sym_str = ",".join(sorted_symbols)
    raw = f"{profile_name}_{timeframe}_{sym_str}"
    return hashlib.md5(raw.encode()).hexdigest()


def build_trade_id(symbol: str, timeframe: str, source_level_id: str) -> str:
    raw = f"{symbol}_{timeframe}_{source_level_id}"
    return hashlib.md5(raw.encode()).hexdigest()


def simulated_trade_to_dict(trade: SimulatedTrade) -> dict:
    return asdict(trade)


def backtest_summary_to_dict(summary: BacktestRunSummary) -> dict:
    return asdict(summary)


def clamp_return(value: float | None) -> float | None:
    if value is None:
        return None
    # clamp arbitrarily large values (like infinite or extremely large)
    # usually seen due to div by 0 or close to 0 entry prices
    if value > 1000.0:
        return 1000.0
    if value < -1000.0:
        return -1000.0
    return value
