import pandas as pd
from paper.paper_models import VirtualPosition, VirtualPortfolioSnapshot, virtual_portfolio_snapshot_to_dict
from paper.paper_config import PaperTradingProfile

class VirtualPortfolio:
    def __init__(self, initial_equity: float, base_currency: str = "TRY"):
        self.initial_equity = initial_equity
        self.base_currency = base_currency
        self.cash_balance = initial_equity
        self.equity = initial_equity

        self.open_positions: list[VirtualPosition] = []
        self.closed_positions: list[VirtualPosition] = []
        self.snapshots: list[VirtualPortfolioSnapshot] = []

        self.realized_pnl = 0.0
        self.total_fees = 0.0
        self.total_slippage = 0.0

    def can_open_position(self, symbol: str, profile: PaperTradingProfile) -> tuple[bool, list[str]]:
        reasons = []
        if len(self.open_positions) >= profile.max_open_positions:
            reasons.append("Max open positions limit reached.")

        same_symbol_count = sum(1 for p in self.open_positions if p.symbol == symbol)
        if same_symbol_count >= profile.max_open_positions_per_symbol:
            reasons.append(f"Max open positions for symbol {symbol} reached.")

        return len(reasons) == 0, reasons

    def open_position(self, position: VirtualPosition) -> tuple[bool, list[str]]:
        self.open_positions.append(position)
        # Deduct initial fees from cash
        self.cash_balance -= position.fee_cost
        self.total_fees += position.fee_cost
        return True, []

    def close_position(self, position: VirtualPosition) -> None:
        self.open_positions = [p for p in self.open_positions if p.position_id != position.position_id]
        self.closed_positions.append(position)

        if position.net_pnl is not None:
            self.realized_pnl += position.net_pnl
            self.cash_balance += position.net_pnl

        # Add the exit fees (already accounted in net_pnl but tracking total)
        # Assuming position.fee_cost contains total round-trip fee by now
        if position.fee_cost:
            # We already deducted entry fee. Need to track exit fee somehow if we want to be exact,
            # but usually it's easier to just sum all total fees from closed positions
            pass

        self.equity = self.cash_balance # Update base equity

    def get_open_positions(self) -> list[VirtualPosition]:
        return self.open_positions

    def get_closed_positions(self) -> list[VirtualPosition]:
        return self.closed_positions

    def mark_to_market(self, timestamp: str, price_map: dict[str, float]) -> VirtualPortfolioSnapshot:
        unrealized_pnl = 0.0
        exposure_notional = 0.0

        for p in self.open_positions:
            current_price = price_map.get(p.symbol)
            if current_price and p.entry_price:
                direction = 1 if p.order_side == "virtual_long_bias" else -1
                gross = (current_price - p.entry_price) * p.units * direction
                net = gross - p.fee_cost - p.slippage_cost
                unrealized_pnl += net
                exposure_notional += (current_price * p.units)

        current_equity = self.cash_balance + unrealized_pnl

        peak_equity = max([s.equity for s in self.snapshots] + [self.initial_equity])
        drawdown_pct = 0.0
        if peak_equity > 0:
            drawdown_pct = min(0.0, (current_equity - peak_equity) / peak_equity)

        snapshot = VirtualPortfolioSnapshot(
            timestamp=timestamp,
            cash_balance=self.cash_balance,
            equity=current_equity,
            open_position_count=len(self.open_positions),
            closed_position_count=len(self.closed_positions),
            unrealized_pnl=unrealized_pnl,
            realized_pnl=self.realized_pnl,
            total_fees=self.total_fees,
            total_slippage=self.total_slippage,
            exposure_notional=exposure_notional,
            drawdown_pct=drawdown_pct,
            warnings=[]
        )
        self.snapshots.append(snapshot)
        return snapshot

    def to_positions_dataframe(self) -> pd.DataFrame:
        from paper.paper_models import virtual_position_to_dict
        all_positions = self.closed_positions + self.open_positions
        if not all_positions:
            return pd.DataFrame()
        return pd.DataFrame([virtual_position_to_dict(p) for p in all_positions])

    def to_equity_curve_dataframe(self) -> pd.DataFrame:
        if not self.snapshots:
            return pd.DataFrame()
        return pd.DataFrame([virtual_portfolio_snapshot_to_dict(s) for s in self.snapshots])

    def summarize(self) -> dict:
        wins = sum(1 for p in self.closed_positions if p.result_label == "virtual_win")
        total_closed = len(self.closed_positions)
        win_rate = (wins / total_closed) if total_closed > 0 else 0.0

        drawdowns = [s.drawdown_pct for s in self.snapshots]
        max_dd = min(drawdowns) if drawdowns else 0.0

        current_equity = self.snapshots[-1].equity if self.snapshots else self.initial_equity
        return {
            "initial_equity": self.initial_equity,
            "current_equity": current_equity,
            "cash_balance": self.cash_balance,
            "realized_pnl": self.realized_pnl,
            "unrealized_pnl": self.snapshots[-1].unrealized_pnl if self.snapshots else 0.0,
            "open_positions": len(self.open_positions),
            "closed_positions": total_closed,
            "win_rate": win_rate,
            "total_fees": self.total_fees,
            "total_slippage": self.total_slippage,
            "max_drawdown_pct": max_dd
        }
