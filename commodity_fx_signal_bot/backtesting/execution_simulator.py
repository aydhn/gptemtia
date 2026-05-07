import pandas as pd
from backtesting.backtest_config import BacktestProfile


class ExecutionSimulator:
    def __init__(self, profile: BacktestProfile):
        self.profile = profile

    def simulate_entry(
        self,
        price_df: pd.DataFrame,
        signal_ts: pd.Timestamp,
        directional_bias: str,
    ) -> dict:
        try:
            loc = price_df.index.get_loc(signal_ts)
            target_loc = loc + self.profile.entry_delay_bars
            if target_loc >= len(price_df):
                return {"status": "rejected", "reason": "not_enough_future_bars"}

            entry_bar_ts = price_df.index[target_loc]
            entry_bar = price_df.iloc[target_loc]

            if self.profile.use_next_bar_open_for_entry:
                entry_price = entry_bar["open"]
            else:
                entry_price = entry_bar["close"]

            return {
                "status": "success",
                "entry_timestamp": entry_bar_ts,
                "entry_price": entry_price,
                "reason": (
                    "next_bar_open_entry"
                    if self.profile.use_next_bar_open_for_entry
                    else "candidate_entry"
                ),
            }
        except KeyError:
            return {"status": "rejected", "reason": "timestamp_not_found"}

    def simulate_exit(
        self,
        price_df: pd.DataFrame,
        entry_ts: pd.Timestamp,
        exit_ts: pd.Timestamp,
        exit_reason: str,
    ) -> dict:
        try:
            loc = price_df.index.get_loc(exit_ts)
            target_loc = loc + self.profile.exit_delay_bars

            if target_loc >= len(price_df):
                # End of data scenario
                exit_bar_ts = price_df.index[-1]
                exit_bar = price_df.iloc[-1]
                exit_price = exit_bar["close"]
            else:
                exit_bar_ts = price_df.index[target_loc]
                exit_bar = price_df.iloc[target_loc]
                if self.profile.use_next_bar_open_for_exit:
                    exit_price = exit_bar["open"]
                else:
                    exit_price = exit_bar["close"]

            return {
                "status": "success",
                "exit_timestamp": exit_bar_ts,
                "exit_price": exit_price,
                "reason": exit_reason,
            }
        except KeyError:
            return {"status": "rejected", "reason": "timestamp_not_found"}

    def apply_transaction_costs(
        self,
        price: float,
        units: float,
        notional: float | None,
    ) -> dict:
        if (
            not self.profile.include_transaction_costs
            or notional is None
            or notional == 0
        ):
            return {"fee": 0.0, "slippage": 0.0}

        fee = notional * (self.profile.fee_bps / 10000.0)
        slippage = notional * (self.profile.slippage_bps / 10000.0)
        return {"fee": fee, "slippage": slippage}
