import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)

def validate_weights(weights: dict[str, float]) -> dict:
    warnings = []
    if not weights:
        warnings.append("Empty weights dictionary.")
        return warnings

    total = sum(weights.values())
    if not np.isclose(total, 1.0, atol=1e-5):
        warnings.append(f"Weights do not sum to 1.0. Total: {total}")

    for symbol, weight in weights.items():
        if weight < 0:
            warnings.append(f"Negative weight found for {symbol}: {weight}")

    return warnings

def calculate_equal_weights(symbols: list[str]) -> dict[str, float]:
    if not symbols:
        return {}
    weight = 1.0 / len(symbols)
    return {symbol: weight for symbol in symbols}

def calculate_inverse_volatility_weights(returns_df: pd.DataFrame, max_single_weight: float = 0.35) -> tuple[dict[str, float], dict]:
    summary = {"warnings": [], "method": "inverse_volatility_weight"}

    if returns_df.empty:
        summary["warnings"].append("Empty returns dataframe.")
        return {}, summary

    volatilities = returns_df.std()

    # Handle zero or NaN volatility
    volatilities = volatilities.replace(0, np.nan)
    if volatilities.isna().all():
        summary["warnings"].append("All volatilities are zero or NaN. Falling back to equal weight.")
        symbols = returns_df.columns.tolist()
        return calculate_equal_weights(symbols), summary

    volatilities = volatilities.fillna(volatilities.max()) # assign highest vol to missing

    inverse_vols = 1.0 / volatilities
    raw_weights = (inverse_vols / inverse_vols.sum()).to_dict()

    capped_weights = cap_and_redistribute_weights(raw_weights, max_single_weight)

    return capped_weights, summary

def calculate_research_score_weights(ranking_df: pd.DataFrame, symbols: list[str], max_single_weight: float = 0.35) -> tuple[dict[str, float], dict]:
    summary = {"warnings": [], "method": "research_score_weight"}

    if ranking_df.empty or "research_score" not in ranking_df.columns:
        summary["warnings"].append("No research_score found. Falling back to equal weight.")
        return calculate_equal_weights(symbols), summary

    ranking_df = ranking_df[ranking_df["symbol"].isin(symbols)]

    if ranking_df.empty:
        summary["warnings"].append("No symbols matched in ranking. Falling back to equal weight.")
        return calculate_equal_weights(symbols), summary

    # Ensure scores are positive
    scores = ranking_df.set_index("symbol")["research_score"]
    min_score = scores.min()
    if min_score < 0:
        scores = scores - min_score + 0.01

    raw_weights = (scores / scores.sum()).to_dict()

    # Fill missing symbols with 0
    for sym in symbols:
        if sym not in raw_weights:
            raw_weights[sym] = 0.0

    capped_weights = cap_and_redistribute_weights(raw_weights, max_single_weight)

    return capped_weights, summary

def calculate_risk_adjusted_weights(ranking_df: pd.DataFrame, returns_df: pd.DataFrame, symbols: list[str], max_single_weight: float = 0.35) -> tuple[dict[str, float], dict]:
    summary = {"warnings": [], "method": "risk_adjusted_weight"}

    # Simple proxy: Combine research score and inverse volatility
    score_weights, score_summary = calculate_research_score_weights(ranking_df, symbols, max_single_weight=1.0) # no cap yet
    vol_weights, vol_summary = calculate_inverse_volatility_weights(returns_df[symbols], max_single_weight=1.0) # no cap yet

    summary["warnings"].extend(score_summary["warnings"])
    summary["warnings"].extend(vol_summary["warnings"])

    raw_weights = {}
    for sym in symbols:
        sw = score_weights.get(sym, 0.0)
        vw = vol_weights.get(sym, 0.0)
        raw_weights[sym] = sw * vw

    total = sum(raw_weights.values())
    if total == 0:
         return calculate_equal_weights(symbols), summary

    raw_weights = {k: v/total for k,v in raw_weights.items()}
    capped_weights = cap_and_redistribute_weights(raw_weights, max_single_weight)

    return capped_weights, summary

def cap_and_redistribute_weights(weights: dict[str, float], max_single_weight: float) -> dict[str, float]:
    if not weights:
        return {}

    w = pd.Series(weights)

    if w.max() <= max_single_weight:
        return weights

    capped = w.copy()
    num_iterations = 0
    max_iterations = 10

    while capped.max() > max_single_weight and num_iterations < max_iterations:
        # Cap the oversized weights
        oversized_mask = capped > max_single_weight
        excess = capped[oversized_mask] - max_single_weight
        total_excess = excess.sum()

        capped[oversized_mask] = max_single_weight

        # Distribute excess to others
        eligible_mask = capped < max_single_weight
        if not eligible_mask.any():
            break # All weights are at max cap, cannot redistribute (should not happen if max_single_weight * N > 1)

        eligible_sum = capped[eligible_mask].sum()
        if eligible_sum == 0:
            # If remaining weights are 0, distribute equally
            capped[eligible_mask] = total_excess / eligible_mask.sum()
        else:
             capped[eligible_mask] += total_excess * (capped[eligible_mask] / eligible_sum)

        num_iterations += 1

    return capped.to_dict()
