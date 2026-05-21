import pandas as pd
import numpy as np
from portfolio_research.portfolio_models import VirtualBasketDefinition

def calculate_diversification_score(corr_df: pd.DataFrame) -> float:
    if corr_df.empty or corr_df.shape[0] < 2:
        return 0.0

    upper_tri = corr_df.where(np.triu(np.ones(corr_df.shape), k=1).astype(bool))
    avg_corr = upper_tri.mean().mean()

    if pd.isna(avg_corr):
        return 0.0

    score = 1.0 - max(0.0, avg_corr)
    return float(np.clip(score, 0.0, 1.0))

def calculate_effective_number_of_assets(weights: dict[str, float]) -> float:
    if not weights:
        return 0.0

    w = np.array(list(weights.values()))
    w_sum_sq = np.sum(w**2)

    if w_sum_sq == 0:
        return 0.0

    return float(1.0 / w_sum_sq)

def infer_diversification_label(diversification_score: float, effective_assets: float, symbol_count: int) -> str:
    if symbol_count < 2:
        return "insufficient_data"

    eff_ratio = effective_assets / symbol_count if symbol_count > 0 else 0

    if diversification_score > 0.6 and eff_ratio > 0.6:
        return "well_diversified"
    elif diversification_score > 0.4 and eff_ratio > 0.4:
        return "moderately_diversified"
    elif eff_ratio < 0.2:
        return "highly_concentrated"
    else:
        return "concentrated"

def build_diversification_report(corr_df: pd.DataFrame, weights: dict[str, float] | None = None) -> dict:
    score = calculate_diversification_score(corr_df)

    summary = {
        "diversification_score": score,
        "warnings": [],
        "note": "well_diversified is not investment advice."
    }

    if weights:
        eff_assets = calculate_effective_number_of_assets(weights)
        label = infer_diversification_label(score, eff_assets, len(weights))
        summary["effective_number_of_assets"] = eff_assets
        summary["diversification_label"] = label

    return summary

def build_diversification_table(baskets: list[VirtualBasketDefinition], corr_df: pd.DataFrame) -> pd.DataFrame:
    rows = []

    for basket in baskets:
        valid_symbols = [s for s in basket.symbols if s in corr_df.columns]

        if len(valid_symbols) < 2:
            score = 0.0
            eff_assets = len(valid_symbols)
            label = "insufficient_data"
        else:
            sub_corr = corr_df.loc[valid_symbols, valid_symbols]
            score = calculate_diversification_score(sub_corr)
            eff_assets = calculate_effective_number_of_assets(basket.weights)
            label = infer_diversification_label(score, eff_assets, len(valid_symbols))

        rows.append({
            "basket_id": basket.basket_id,
            "basket_name": basket.basket_name,
            "symbol_count": len(valid_symbols),
            "diversification_score": score,
            "effective_assets": eff_assets,
            "diversification_label": label
        })

    if not rows:
        return pd.DataFrame()

    return pd.DataFrame(rows)
