import pandas as pd
from paper.paper_config import PaperTradingProfile
from paper.paper_models import VirtualOrder
from paper.virtual_order_book import VirtualOrderBook
from paper.virtual_portfolio import VirtualPortfolio
from paper.virtual_execution import VirtualExecutionSimulator
from paper.paper_risk import check_virtual_order_risk
from paper.virtual_position import open_virtual_position_from_order, check_virtual_position_exit, close_virtual_position
from paper.virtual_order import reject_virtual_order

class PaperLifecycleEngine:
    def __init__(self, profile: PaperTradingProfile, execution_simulator: VirtualExecutionSimulator | None = None):
        self.profile = profile
        self.execution_simulator = execution_simulator or VirtualExecutionSimulator(profile)

    def process_new_orders(
        self,
        timestamp: pd.Timestamp,
        orders: list[VirtualOrder],
        order_book: VirtualOrderBook,
        portfolio: VirtualPortfolio,
    ) -> dict:
        summary = {"new": 0, "rejected": 0, "rejected_reasons": []}

        for order in orders:
            risk_res = check_virtual_order_risk(order, portfolio, self.profile)
            if not risk_res["passed"]:
                order = reject_virtual_order(order, risk_res["reasons"])
                summary["rejected"] += 1
                summary["rejected_reasons"].extend(risk_res["reasons"])
            else:
                summary["new"] += 1

            order_book.add_order(order)

        return summary

    def process_pending_orders(
        self,
        timestamp: pd.Timestamp,
        price_df: pd.DataFrame,
        order_book: VirtualOrderBook,
        portfolio: VirtualPortfolio,
    ) -> dict:
        summary = {"filled": 0, "expired": 0, "fill_warnings": []}
        active_orders = order_book.get_active_orders()

        for order in active_orders:
            filled_order, sim_warnings = self.execution_simulator.simulate_order_fill(order, price_df, timestamp)

            if sim_warnings:
                summary["fill_warnings"].append(sim_warnings)

            order_book.update_order(filled_order)

            if filled_order.order_status == "virtual_filled":
                pos = open_virtual_position_from_order(filled_order, {}, self.profile)

                can_open, reasons = portfolio.can_open_position(pos.symbol, self.profile)
                if can_open:
                    portfolio.open_position(pos)
                    summary["filled"] += 1
                else:
                    filled_order.notes += f" Failed to open pos: {reasons}"

            elif filled_order.order_status == "virtual_expired":
                summary["expired"] += 1

        return summary

    def process_open_positions(
        self,
        timestamp: pd.Timestamp,
        price_df: pd.DataFrame,
        portfolio: VirtualPortfolio,
    ) -> dict:
        summary = {"closed": 0, "warnings": []}

        current_bar = price_df.loc[timestamp] if timestamp in price_df.index else None
        if current_bar is None:
            return summary

        for pos in list(portfolio.get_open_positions()):
            exit_info = check_virtual_position_exit(pos, current_bar, self.profile)
            if exit_info.get("exit"):
                close_virtual_position(pos, str(timestamp), exit_info["price"], exit_info["reason"], self.profile)
                portfolio.close_position(pos)
                summary["closed"] += 1

        return summary

    def process_timestamp(
        self,
        timestamp: pd.Timestamp,
        price_df: pd.DataFrame,
        new_orders: list[VirtualOrder],
        order_book: VirtualOrderBook,
        portfolio: VirtualPortfolio,
    ) -> dict:

        events = []

        new_res = self.process_new_orders(timestamp, new_orders, order_book, portfolio)
        events.append({"type": "new_orders", "result": new_res})

        pos_res = self.process_open_positions(timestamp, price_df, portfolio)
        events.append({"type": "positions", "result": pos_res})

        pend_res = self.process_pending_orders(timestamp, price_df, order_book, portfolio)
        events.append({"type": "pending", "result": pend_res})

        price_map = {}
        if timestamp in price_df.index:
            sym = price_df.iloc[0].get('symbol', 'UNKNOWN') if 'symbol' in price_df.columns else "UNKNOWN"
            close_px = float(price_df.loc[timestamp]['close'])
            for p in portfolio.get_open_positions():
                price_map[p.symbol] = close_px

        portfolio.mark_to_market(str(timestamp), price_map)

        return {"events": events}
