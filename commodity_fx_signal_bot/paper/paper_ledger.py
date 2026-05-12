import pandas as pd
from paper.paper_models import VirtualOrder, VirtualPosition

class PaperLedger:
    def __init__(self):
        self.events = []

    def add_event(self, event: dict) -> None:
        self.events.append(event)

    def add_order_event(self, order: VirtualOrder, event_type: str, timestamp: str, extra: dict | None = None) -> None:
        event = {
            "timestamp": timestamp,
            "event_type": event_type,
            "entity_type": "order",
            "entity_id": order.order_id,
            "symbol": order.symbol,
            "status": order.order_status,
            "side": order.order_side,
            "price": order.requested_price,
            "units": order.adjusted_theoretical_units,
            "message": order.notes
        }
        if extra:
            event.update(extra)
        self.add_event(event)

    def add_position_event(self, position: VirtualPosition, event_type: str, timestamp: str, extra: dict | None = None) -> None:
        event = {
            "timestamp": timestamp,
            "event_type": event_type,
            "entity_type": "position",
            "entity_id": position.position_id,
            "symbol": position.symbol,
            "status": position.position_status,
            "side": position.order_side,
            "price": position.exit_price if event_type == "virtual_position_closed" else position.entry_price,
            "units": position.units,
            "pnl": position.net_pnl,
            "message": position.notes
        }
        if extra:
            event.update(extra)
        self.add_event(event)

    def to_dataframe(self) -> pd.DataFrame:
        if not self.events:
            return pd.DataFrame()
        return pd.DataFrame(self.events)

    def summarize(self) -> dict:
        if not self.events:
            return {}
        df = pd.DataFrame(self.events)
        return {
            "total_events": len(df),
            "event_types": df['event_type'].value_counts().to_dict() if 'event_type' in df else {}
        }
