import pandas as pd
from paper.paper_config import PaperTradingProfile
from paper.paper_models import VirtualOrder
from paper.virtual_order import expire_virtual_order, mark_virtual_order_filled, reject_virtual_order

class VirtualExecutionSimulator:
    def __init__(self, profile: PaperTradingProfile):
        self.profile = profile

    def simulate_order_fill(
        self,
        order: VirtualOrder,
        price_df: pd.DataFrame,
        current_timestamp: pd.Timestamp,
    ) -> tuple[VirtualOrder, dict]:

        warnings = {}
        # Ensure timestamp is comparable if string
        if isinstance(current_timestamp, str):
            current_timestamp = pd.to_datetime(current_timestamp)

        future_df = price_df[price_df.index > current_timestamp]

        if future_df.empty:
            return expire_virtual_order(order, str(current_timestamp), reason="End of data, cannot fill."), warnings

        next_bar = future_df.iloc[0]
        fill_price = next_bar['open'] if self.profile.use_next_bar_open_for_fill else next_bar['close']

        if pd.isna(fill_price):
            return reject_virtual_order(order, ["Missing fill price data."]), warnings

        fill_price = self.apply_virtual_slippage(fill_price, order.order_side, is_entry=True)
        filled_order = mark_virtual_order_filled(order, str(next_bar.name), fill_price)

        return filled_order, warnings

    def calculate_virtual_transaction_costs(
        self,
        price: float,
        units: float,
        notional: float | None,
    ) -> dict:
        actual_notional = notional if notional is not None else price * units
        fee_cost = actual_notional * (self.profile.fee_bps / 10000.0)
        return {
            "fee_cost": fee_cost,
            "slippage_cost": 0.0 # Slippage is built into the price diff
        }

    def apply_virtual_slippage(
        self,
        price: float,
        order_side: str,
        is_entry: bool = True,
    ) -> float:
        if self.profile.slippage_bps <= 0:
            return price

        slip_factor = self.profile.slippage_bps / 10000.0

        if is_entry:
            if order_side == "virtual_long_bias":
                return price * (1.0 + slip_factor)
            elif order_side == "virtual_short_bias":
                return price * (1.0 - slip_factor)
        else: # Exit
            if order_side == "virtual_long_bias": # Selling to close
                return price * (1.0 - slip_factor)
            elif order_side == "virtual_short_bias": # Buying to close
                return price * (1.0 + slip_factor)

        return price
