from paper.paper_config import PaperTradingProfile
from paper.paper_models import VirtualOrder
from paper.virtual_portfolio import VirtualPortfolio

def check_symbol_position_limit(symbol: str, portfolio: VirtualPortfolio, profile: PaperTradingProfile) -> dict:
    open_pos = portfolio.get_open_positions()
    same_symbol_count = sum(1 for p in open_pos if p.symbol == symbol)
    if same_symbol_count >= profile.max_open_positions_per_symbol:
        return {"passed": False, "reason": "Max open positions for symbol reached"}
    return {"passed": True}

def check_total_position_limit(portfolio: VirtualPortfolio, profile: PaperTradingProfile) -> dict:
    open_pos = portfolio.get_open_positions()
    if len(open_pos) >= profile.max_open_positions:
        return {"passed": False, "reason": "Max total open positions reached"}
    return {"passed": True}

def check_virtual_exposure_limit(order: VirtualOrder, portfolio: VirtualPortfolio, profile: PaperTradingProfile) -> dict:
    if order.theoretical_notional and order.theoretical_notional > portfolio.equity * 2.0:
        return {"passed": False, "reason": "Order theoretical notional exceeds allowed exposure"}
    return {"passed": True}

def check_virtual_order_risk(order: VirtualOrder, portfolio: VirtualPortfolio, profile: PaperTradingProfile) -> dict:
    checks = []
    checks.append(check_total_position_limit(portfolio, profile))
    if not profile.allow_overlapping_positions:
        checks.append(check_symbol_position_limit(order.symbol, portfolio, profile))
    checks.append(check_virtual_exposure_limit(order, portfolio, profile))

    reasons = [c["reason"] for c in checks if not c["passed"]]
    passed = len(reasons) == 0

    return {"passed": passed, "reasons": reasons}

def build_paper_risk_audit(order: VirtualOrder, portfolio: VirtualPortfolio, profile: PaperTradingProfile) -> dict:
    result = check_virtual_order_risk(order, portfolio, profile)
    return {
        "order_id": order.order_id,
        "symbol": order.symbol,
        "passed": result["passed"],
        "reasons": result["reasons"],
        "current_equity": portfolio.equity,
        "open_positions": len(portfolio.get_open_positions())
    }
