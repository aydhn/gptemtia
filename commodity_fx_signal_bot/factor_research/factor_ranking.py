import pandas as pd
import numpy as np
from .factor_config import FactorResearchProfile

def build_factor_rank_table(score_df: pd.DataFrame, profile: FactorResearchProfile) -> pd.DataFrame:
    """
    Input: DataFrame created by build_factor_score_table
    Output: The same table filtered/sorted, ready for storage.
    """
    if score_df.empty:
        return pd.DataFrame()

    return score_df.sort_values(by=["factor_id", "rank"]).reset_index(drop=True)

def calculate_composite_factor_score(score_df: pd.DataFrame, factor_weights: dict[str, float] | None = None) -> pd.Series:
    """
    Calculates a composite score across all available factors for each symbol.
    Expects score_df to be the output of build_factor_score_table.
    """
    if score_df.empty:
         return pd.Series(dtype=float)

    # Pivot so symbols are index, factors are columns, and values are normalized_score
    pivot_df = score_df.pivot(index="symbol", columns="factor_id", values="normalized_score")

    if factor_weights:
        # Normalize weights
        total_weight = sum(factor_weights.values())
        if total_weight == 0:
             return pivot_df.mean(axis=1, skipna=True)

        weighted_sum = pd.Series(0.0, index=pivot_df.index)
        weight_sum = pd.Series(0.0, index=pivot_df.index)

        for factor_id, weight in factor_weights.items():
             if factor_id in pivot_df.columns:
                 norm_weight = weight / total_weight
                 # Only add weight where data exists
                 valid_mask = ~pivot_df[factor_id].isna()
                 weighted_sum[valid_mask] += pivot_df[factor_id][valid_mask] * norm_weight
                 weight_sum[valid_mask] += norm_weight

        # Adjust for missing data
        result = weighted_sum / weight_sum
        return result.replace([np.inf, -np.inf], np.nan)

    else:
        return pivot_df.mean(axis=1, skipna=True)

def build_composite_factor_ranking(score_df: pd.DataFrame, profile: FactorResearchProfile) -> pd.DataFrame:
    if score_df.empty:
        return pd.DataFrame()

    composite_scores = calculate_composite_factor_score(score_df)

    records = []
    for symbol in composite_scores.index:
        comp_score = composite_scores.loc[symbol]
        if pd.isna(comp_score):
            continue

        symbol_df = score_df[score_df["symbol"] == symbol]
        top_count = len(symbol_df[symbol_df["bucket_label"] == "top_factor_bucket"])
        bottom_count = len(symbol_df[symbol_df["bucket_label"] == "bottom_factor_bucket"])
        warning_count = symbol_df["warnings"].apply(lambda x: len(x) if isinstance(x, list) else 0).sum()

        records.append({
            "symbol": symbol,
            "composite_factor_score": float(comp_score),
            "top_factor_bucket_count": int(top_count),
            "bottom_factor_bucket_count": int(bottom_count),
            "warning_count": int(warning_count)
        })

    df = pd.DataFrame(records)
    if df.empty:
        return df

    # Rank them
    df["composite_rank"] = df["composite_factor_score"].rank(ascending=False, method="min").astype(int)
    df["composite_percentile"] = df["composite_factor_score"].rank(pct=True, ascending=True)

    return df.sort_values("composite_rank").reset_index(drop=True)

def summarize_factor_ranking(rank_df: pd.DataFrame) -> dict:
    if rank_df.empty:
        return {"total_symbols": 0}

    return {
        "total_symbols": len(rank_df),
        "top_symbol": rank_df.iloc[0]["symbol"] if len(rank_df) > 0 else None,
        "bottom_symbol": rank_df.iloc[-1]["symbol"] if len(rank_df) > 0 else None,
        "average_score": float(rank_df["composite_factor_score"].mean()) if len(rank_df) > 0 else None
    }
