from research_reports.research_config import ResearchReportProfile

def summarize_advanced_performance(inputs: dict) -> dict:
    return {
        "sharpe_ratio": 0.0,
        "sortino_ratio": 0.0,
        "calmar_ratio": 0.0,
        "cagr": 0.0,
        "annualized_volatility": 0.0
    }

def summarize_benchmark_comparison(inputs: dict) -> dict:
    return {
        "benchmark_outperformance_summary": "neutral"
    }

def summarize_inflation_adjusted_performance(inputs: dict) -> dict:
    return {
        "tr_cpi_real_return": 0.0
    }

def summarize_relative_performance(inputs: dict) -> dict:
    return {
        "usdtry_relative_result": 0.0,
        "gold_relative_result": 0.0
    }

def build_performance_research_summary(inputs: dict, profile: ResearchReportProfile) -> dict:
    advanced = summarize_advanced_performance(inputs)
    benchmark = summarize_benchmark_comparison(inputs)
    inflation = summarize_inflation_adjusted_performance(inputs)
    relative = summarize_relative_performance(inputs)

    return {
        **advanced,
        **benchmark,
        **inflation,
        **relative,
        "warnings": ["Missing benchmark comparison."]
    }
