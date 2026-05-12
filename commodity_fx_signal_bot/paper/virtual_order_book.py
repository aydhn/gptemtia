import pandas as pd
from paper.paper_models import VirtualOrder, virtual_order_to_dict

class VirtualOrderBook:
    def __init__(self):
        self.orders: list[VirtualOrder] = []

    def add_order(self, order: VirtualOrder) -> None:
        # Check if exists
        for i, o in enumerate(self.orders):
            if o.order_id == order.order_id:
                self.orders[i] = order
                return
        self.orders.append(order)

    def add_orders(self, orders: list[VirtualOrder]) -> None:
        for o in orders:
            self.add_order(o)

    def get_active_orders(self) -> list[VirtualOrder]:
        return [o for o in self.orders if o.order_status == "virtual_pending"]

    def get_orders_by_symbol(self, symbol: str) -> list[VirtualOrder]:
        return [o for o in self.orders if o.symbol == symbol]

    def update_order(self, order: VirtualOrder) -> None:
        self.add_order(order)

    def to_dataframe(self) -> pd.DataFrame:
        if not self.orders:
            return pd.DataFrame()
        records = [virtual_order_to_dict(o) for o in self.orders]
        return pd.DataFrame(records)

    def summarize(self) -> dict:
        summary = {
            "total_orders": len(self.orders),
            "pending_orders": sum(1 for o in self.orders if o.order_status == "virtual_pending"),
            "filled_orders": sum(1 for o in self.orders if o.order_status == "virtual_filled"),
            "rejected_orders": sum(1 for o in self.orders if o.order_status == "virtual_rejected"),
            "expired_orders": sum(1 for o in self.orders if o.order_status == "virtual_expired"),
            "by_symbol": {},
            "by_order_side": {},
            "by_strategy_family": {}
        }

        for o in self.orders:
            summary["by_symbol"][o.symbol] = summary["by_symbol"].get(o.symbol, 0) + 1
            summary["by_order_side"][o.order_side] = summary["by_order_side"].get(o.order_side, 0) + 1
            summary["by_strategy_family"][o.strategy_family] = summary["by_strategy_family"].get(o.strategy_family, 0) + 1

        return summary
