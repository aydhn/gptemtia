import pandas as pd
import numpy as np
from portfolio_research.portfolio_models import VirtualBasketDefinition
from portfolio_research.portfolio_config import PortfolioResearchProfile
from portfolio_research.exposure_analysis import calculate_asset_class_exposure

def calculate_hhi_concentration(weights: dict[str, float]) -> float:
    if not weights:
        return 0.0
    w = np.array(list(weights.values()))
    return float(np.sum(w**2))

def calculate_top_n_weight(weights: dict[str, float], n: int = 3) -> float:
    if not weights:
        return 0.0
    sorted_weights = sorted(list(weights.values()), reverse=True)
    return float(sum(sorted_weights[:n]))

def identify_concentration_warnings(weights: dict[str, float], metadata_df: pd.DataFrame | None, profile: PortfolioResearchProfile) -> list[str]:
    warnings = []

    hhi = calculate_hhi_concentration(weights)
    if hhi > 0.25:
        warnings.append(f"High HHI Concentration ({hhi:.2f}). Indicates a highly concentrated portfolio.")

    top_3 = calculate_top_n_weight(weights, 3)
    if top_3 > 0.6:
        warnings.append(f"High Top-3 Concentration ({top_3:.1%}). Top 3 assets dominate the portfolio.")

    if metadata_df is not None and not metadata_df.empty:
        ac_exp = calculate_asset_class_exposure(weights, metadata_df)
        if not ac_exp.empty:
            max_ac = ac_exp.iloc[0]
            if max_ac['exposure_weight'] > profile.max_asset_class_weight:
                warnings.append(f"Asset Class Concentration: {max_ac['asset_class']} ({max_ac['exposure_weight']:.1%}) exceeds limit ({profile.max_asset_class_weight:.1%}).")

    max_w = max(weights.values()) if weights else 0
    if max_w > profile.max_single_symbol_weight:
        warnings.append(f"Single Symbol Concentration: Max weight ({max_w:.1%}) exceeds limit ({profile.max_single_symbol_weight:.1%}).")

    return warnings

def build_concentration_risk_report(weights: dict[str, float], metadata_df: pd.DataFrame | None, profile: PortfolioResearchProfile) -> dict:
    hhi = calculate_hhi_concentration(weights)
    top_3 = calculate_top_n_weight(weights, 3)
    warnings = identify_concentration_warnings(weights, metadata_df, profile)

    return {
        "hhi": hhi,
        "top_3_weight": top_3,
        "warnings": warnings,
        "note": "Concentration risk gercek portfoy riski degildir; sanal arastirma metrigidir. Warning trade talimati degildir."
    }

def build_concentration_risk_table(baskets: list[VirtualBasketDefinition], metadata_df: pd.DataFrame | None, profile: PortfolioResearchProfile) -> pd.DataFrame:
    rows = []
    for basket in baskets:
        hhi = calculate_hhi_concentration(basket.weights)
        top_3 = calculate_top_n_weight(basket.weights, 3)
        warnings = identify_concentration_warnings(basket.weights, metadata_df, profile)

        rows.append({
            "basket_id": basket.basket_id,
            "basket_type": basket.basket_type,
            "hhi": hhi,
            "top_3_weight": top_3,
            "warning_count": len(warnings)
        })

    if not rows:
        return pd.DataFrame()
    return pd.DataFrame(rows)
