import pandas as pd
from portfolio_research.portfolio_models import VirtualBasketDefinition
from portfolio_research.portfolio_config import PortfolioResearchProfile
from portfolio_research.exposure_analysis import build_symbol_metadata_table
from config.symbols import SymbolSpec
from portfolio_research.concentration_risk import calculate_hhi_concentration

def build_virtual_allocation_table(baskets: list[VirtualBasketDefinition]) -> pd.DataFrame:
    rows = []
    for basket in baskets:
        for sym, weight in basket.weights.items():
            rows.append({
                "basket_id": basket.basket_id,
                "basket_type": basket.basket_type,
                "symbol": sym,
                "weight": weight
            })
    if not rows:
        return pd.DataFrame()
    return pd.DataFrame(rows)

def calculate_allocation_quality(weights: dict[str, float], corr_df: pd.DataFrame | None, metadata_df: pd.DataFrame | None, profile: PortfolioResearchProfile) -> dict:
    if not weights:
        return {"quality_score": 0.0, "warnings": ["Empty weights"]}

    warnings = []
    score = 1.0

    hhi = calculate_hhi_concentration(weights)
    if hhi > 0.25:
        score -= 0.2
        warnings.append("High HHI concentration.")

    max_weight = max(weights.values()) if weights else 0
    if max_weight > profile.max_single_symbol_weight:
        score -= 0.3
        warnings.append("Max single symbol weight exceeded.")

    return {
        "quality_score": max(0.0, score),
        "hhi": hhi,
        "max_weight": max_weight,
        "warnings": warnings,
        "note": "Quality score is a research metric, not investment advice."
    }

def compare_virtual_allocations(basket_tables: dict[str, pd.DataFrame], performance_df: pd.DataFrame | None = None) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"warnings": ["compare_virtual_allocations not fully implemented."]}

def build_allocation_research_report(baskets: list[VirtualBasketDefinition], corr_df: pd.DataFrame | None, specs: list[SymbolSpec], profile: PortfolioResearchProfile) -> tuple[pd.DataFrame, dict]:
    metadata_df = build_symbol_metadata_table(specs)
    alloc_df = build_virtual_allocation_table(baskets)

    quality_scores = {}
    warnings = []

    for basket in baskets:
        q = calculate_allocation_quality(basket.weights, corr_df, metadata_df, profile)
        quality_scores[basket.basket_id] = q["quality_score"]
        if q["warnings"]:
            warnings.extend([f"[{basket.basket_id}] {w}" for w in q["warnings"]])

    summary = {
        "basket_count": len(baskets),
        "quality_scores": quality_scores,
        "warnings": warnings,
        "note": "Allocation table gercek allocation onerisi degildir. En yuksek quality score yatirim tavsiyesi degildir."
    }

    return alloc_df, summary
