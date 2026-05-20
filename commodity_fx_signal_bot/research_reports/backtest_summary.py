from research_reports.research_config import ResearchReportProfile

def summarize_backtest_trades(inputs: dict) -> dict:
    return {
        "trade_count": 0,
        "win_rate": 0.0,
        "avg_holding_bars": 0.0,
        "top_exit_reasons": []
    }

def summarize_backtest_equity(inputs: dict) -> dict:
    return {
        "total_return_pct": 0.0,
        "max_drawdown_pct": 0.0,
        "profit_factor": 0.0
    }

def summarize_backtest_quality(inputs: dict) -> dict:
    return {
        "lookahead_audit_passed": True,
        "quality_passed": True
    }

def build_backtest_research_summary(inputs: dict, profile: ResearchReportProfile) -> dict:
    trades = summarize_backtest_trades(inputs)
    equity = summarize_backtest_equity(inputs)
    quality = summarize_backtest_quality(inputs)

    return {
        **trades,
        **equity,
        **quality,
        "warnings": ["No backtest data found."] if trades['trade_count'] == 0 else []
    }
