import pandas as pd
from backtesting.backtest_models import SimulatedTrade, simulated_trade_to_dict


class TradeLedger:
    def __init__(self):
        self.trades: list[SimulatedTrade] = []

    def add(self, trade: SimulatedTrade) -> None:
        self.trades.append(trade)

    def extend(self, trades: list[SimulatedTrade]) -> None:
        self.trades.extend(trades)

    def to_dataframe(self) -> pd.DataFrame:
        if not self.trades:
            return pd.DataFrame()
        return pd.DataFrame([simulated_trade_to_dict(t) for t in self.trades])

    @classmethod
    def from_dataframe(cls, df: pd.DataFrame) -> "TradeLedger":
        ledger = cls()
        if df.empty:
            return ledger
        for _, row in df.iterrows():
            t = SimulatedTrade(**row.to_dict())
            ledger.add(t)
        return ledger

    def summarize(self) -> dict:
        if not self.trades:
            return {}

        df = self.to_dataframe()
        return {
            "trade_count": len(df),
            "closed_trade_count": len(df[df["lifecycle_status"] == "simulated_closed"]),
            "open_trade_count": len(df[df["lifecycle_status"] == "simulated_open"]),
            "win_count": len(df[df["result_label"] == "win"]),
            "loss_count": len(df[df["result_label"] == "loss"]),
            "breakeven_count": len(df[df["result_label"] == "breakeven"]),
            "win_rate": len(df[df["result_label"] == "win"])
            / max(1, len(df[df["lifecycle_status"] == "simulated_closed"])),
            "total_gross_pnl": df["gross_pnl"].sum(),
            "total_net_pnl": df["net_pnl"].sum(),
            "avg_return_pct": df["return_pct"].mean(),
            "avg_holding_bars": df["holding_bars"].mean(),
            "by_symbol": df.groupby("symbol").size().to_dict(),
            "by_exit_reason": df.groupby("exit_reason").size().to_dict(),
        }
