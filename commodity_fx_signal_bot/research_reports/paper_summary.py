from research_reports.research_config import ResearchReportProfile

def summarize_paper_orders(inputs: dict) -> dict:
    return {
        "virtual_order_count": 0,
        "virtual_filled_order_count": 0,
        "virtual_rejected_order_count": 0
    }

def summarize_paper_positions(inputs: dict) -> dict:
    return {
        "virtual_open_positions": 0,
        "virtual_closed_positions": 0
    }

def summarize_paper_portfolio(inputs: dict) -> dict:
    return {
        "virtual_equity": 0.0,
        "virtual_return_pct": 0.0,
        "virtual_win_rate": 0.0,
        "virtual_max_drawdown_pct": 0.0
    }

def summarize_paper_quality(inputs: dict) -> dict:
    return {
        "paper_quality_passed": True
    }

def build_paper_research_summary(inputs: dict, profile: ResearchReportProfile) -> dict:
    orders = summarize_paper_orders(inputs)
    positions = summarize_paper_positions(inputs)
    portfolio = summarize_paper_portfolio(inputs)
    quality = summarize_paper_quality(inputs)

    return {
        **orders,
        **positions,
        **portfolio,
        **quality,
        "warnings": []
    }
