import pandas as pd
import numpy as np
from .factor_models import FactorNeutralBasket, build_factor_neutral_basket_id
from .factor_config import FactorResearchProfile

def demean_scores_by_group(score_df: pd.DataFrame, group_col: str = "asset_class") -> pd.DataFrame:
    """
    Asset class neutralization by subtracting group mean.
    Input requires score_df to have "asset_class", "factor_id", "normalized_score"
    """
    if score_df.empty or group_col not in score_df.columns:
        return score_df

    df = score_df.copy()

    # Calculate group means per factor
    group_means = df.groupby([group_col, "factor_id"])["normalized_score"].transform('mean')
    df["normalized_score"] = df["normalized_score"] - group_means

    return df

def neutralize_scores_by_volatility(score_df: pd.DataFrame, volatility_df: pd.DataFrame | None = None) -> pd.DataFrame:
    """
    Placeholder for vol neutralization. In a real scenario, divide score by vol.
    """
    return score_df.copy()

def build_factor_neutral_weights(score_df: pd.DataFrame, profile: FactorResearchProfile) -> tuple[dict[str, float], dict]:
    summary = {"warnings": []}

    if score_df.empty:
        return {}, summary

    df = score_df.copy()

    if profile.neutralize_asset_class and "asset_class" in df.columns:
        df = demean_scores_by_group(df)

    if profile.neutralize_volatility:
        df = neutralize_scores_by_volatility(df)

    # Calculate composite on neutralized scores
    from .factor_ranking import calculate_composite_factor_score
    comp = calculate_composite_factor_score(df)

    # Convert to weights (e.g., rank-based or normalized score-based)
    # Simple approach: demeanor composite score
    comp_mean = comp.mean()
    weights = comp - comp_mean

    # Scale to max weight limits (absolute sum = 1, long/short symmetric ideally)
    pos_sum = weights[weights > 0].sum()
    neg_sum = weights[weights < 0].abs().sum()

    final_weights = {}
    for sym, w in weights.items():
        if pd.isna(w):
             continue
        if w > 0 and pos_sum > 0:
            val = (w / pos_sum) * 0.5
        elif w < 0 and neg_sum > 0:
            val = (w / neg_sum) * 0.5
        else:
            val = 0.0

        # Apply max cap heuristic
        val = np.clip(val, -profile.max_single_symbol_weight, profile.max_single_symbol_weight)
        final_weights[sym] = float(val)

    return final_weights, summary

def build_factor_neutral_basket(score_df: pd.DataFrame, timeframe: str, profile: FactorResearchProfile) -> FactorNeutralBasket:
    weights, summary = build_factor_neutral_weights(score_df, profile)
    symbols = list(weights.keys())

    basket_id = build_factor_neutral_basket_id(timeframe, symbols) if symbols else "empty_basket"

    return FactorNeutralBasket(
        basket_id=basket_id,
        timeframe=timeframe,
        symbols=symbols,
        weights=weights,
        neutralized_exposures={"asset_class": 0.0 if profile.neutralize_asset_class else 1.0},
        methodology="Demeaned composite score weighting",
        warnings=summary["warnings"]
    )

def compare_raw_vs_neutral_factor_scores(raw_df: pd.DataFrame, neutral_df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    summary = {"warnings": ["Comparison is placeholder"]}
    return pd.DataFrame(), summary
