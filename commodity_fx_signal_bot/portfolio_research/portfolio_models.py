import hashlib
from dataclasses import dataclass, field
import pandas as pd


@dataclass
class VirtualBasketDefinition:
    basket_id: str
    basket_name: str
    basket_type: str
    timeframe: str
    symbols: list[str]
    weights: dict[str, float]
    created_at_utc: str
    methodology: str
    warnings: list[str] = field(default_factory=list)


@dataclass
class VirtualBasketPerformance:
    basket_id: str
    timeframe: str
    start_date: str | None
    end_date: str | None
    observation_count: int
    total_return_pct: float | None
    annualized_return_pct: float | None
    annualized_volatility_pct: float | None
    max_drawdown_pct: float | None
    sharpe_like_score: float | None
    diversification_score: float | None
    concentration_score: float | None
    warnings: list[str] = field(default_factory=list)


@dataclass
class PortfolioResearchReport:
    report_id: str
    profile_name: str
    timeframe: str
    symbols: list[str]
    created_at_utc: str
    portfolio_summary: dict
    tables: dict[str, pd.DataFrame]
    markdown: str
    warnings: list[str] = field(default_factory=list)


def build_virtual_basket_id(basket_type: str, timeframe: str, symbols: list[str]) -> str:
    sorted_symbols = sorted(symbols)
    content = f"{basket_type}_{timeframe}_{','.join(sorted_symbols)}"
    hash_obj = hashlib.sha256(content.encode("utf-8"))
    return f"vb_{hash_obj.hexdigest()[:12]}"


def build_portfolio_report_id(profile_name: str, timeframe: str, symbols: list[str]) -> str:
    sorted_symbols = sorted(symbols)
    content = f"{profile_name}_{timeframe}_{','.join(sorted_symbols)}"
    hash_obj = hashlib.sha256(content.encode("utf-8"))
    return f"pr_{hash_obj.hexdigest()[:12]}"


def virtual_basket_definition_to_dict(basket: VirtualBasketDefinition) -> dict:
    return {
        "basket_id": basket.basket_id,
        "basket_name": basket.basket_name,
        "basket_type": basket.basket_type,
        "timeframe": basket.timeframe,
        "symbols": basket.symbols,
        "weights": basket.weights,
        "created_at_utc": basket.created_at_utc,
        "methodology": basket.methodology,
        "warnings": basket.warnings,
    }


def virtual_basket_performance_to_dict(perf: VirtualBasketPerformance) -> dict:
    return {
        "basket_id": perf.basket_id,
        "timeframe": perf.timeframe,
        "start_date": perf.start_date,
        "end_date": perf.end_date,
        "observation_count": perf.observation_count,
        "total_return_pct": perf.total_return_pct,
        "annualized_return_pct": perf.annualized_return_pct,
        "annualized_volatility_pct": perf.annualized_volatility_pct,
        "max_drawdown_pct": perf.max_drawdown_pct,
        "sharpe_like_score": perf.sharpe_like_score,
        "diversification_score": perf.diversification_score,
        "concentration_score": perf.concentration_score,
        "warnings": perf.warnings,
    }


def portfolio_research_report_to_dict(report: PortfolioResearchReport, include_markdown: bool = False) -> dict:
    data = {
        "report_id": report.report_id,
        "profile_name": report.profile_name,
        "timeframe": report.timeframe,
        "symbols": report.symbols,
        "created_at_utc": report.created_at_utc,
        "portfolio_summary": report.portfolio_summary,
        "warnings": report.warnings,
    }
    if include_markdown:
        data["markdown"] = report.markdown
    return data


def normalize_weights(weights: dict[str, float]) -> dict[str, float]:
    total_weight = sum(weights.values())
    if total_weight <= 0:
        return {sym: 0.0 for sym in weights}
    return {sym: weight / total_weight for sym, weight in weights.items()}
