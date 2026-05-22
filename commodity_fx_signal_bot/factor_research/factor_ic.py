import pandas as pd
import numpy as np
from scipy.stats import spearmanr
from .factor_config import FactorResearchProfile

def calculate_factor_ic_proxy(score_df: pd.DataFrame, forward_returns_df: pd.DataFrame, method: str = "spearman") -> pd.DataFrame:
    """
    score_df format: index is symbol, columns are factor_id
    Calculates IC based on a single timestamp cross-section.
    In reality, we want panel data over time. This function acts as a cross-sectional proxy.
    """
    records = []

    if score_df.empty or forward_returns_df.empty:
        return pd.DataFrame()

    last_timestamp = forward_returns_df.index[-1]

    for factor_id in score_df.columns:
         scores = score_df[factor_id].dropna()
         if len(scores) < 3:
              records.append({
                  "factor_id": factor_id,
                  "ic_proxy": None,
                  "p_value": None,
                  "warnings": ["Insufficient data for IC"]
              })
              continue

         symbols = scores.index
         # Get forward returns for these symbols at the latest possible timestamp that isn't NaN
         fwd_rets = []
         valid_scores = []

         # Find the most recent timestamp with enough forward returns
         valid_ts = None
         for ts in reversed(forward_returns_df.index):
              rets = forward_returns_df.loc[ts, symbols].dropna()
              if len(rets) >= 3:
                   valid_ts = ts
                   break

         if valid_ts is not None:
             rets = forward_returns_df.loc[valid_ts, symbols]
             # Align
             aligned = pd.DataFrame({'score': scores, 'ret': rets}).dropna()
             if len(aligned) >= 3:
                 if method == "spearman":
                     ic, pval = spearmanr(aligned['score'], aligned['ret'])
                 else:
                     ic, pval = aligned['score'].corr(aligned['ret']), np.nan

                 records.append({
                     "factor_id": factor_id,
                     "ic_proxy": float(ic),
                     "p_value": float(pval) if not pd.isna(pval) else None,
                     "warnings": []
                 })
                 continue

         records.append({
             "factor_id": factor_id,
             "ic_proxy": None,
             "p_value": None,
             "warnings": ["Could not align forward returns"]
         })

    return pd.DataFrame(records)

def calculate_factor_ic_summary(ic_df: pd.DataFrame) -> dict:
    if ic_df.empty:
        return {"total_factors": 0}

    valid_ic = ic_df.dropna(subset=['ic_proxy'])

    return {
        "total_factors": len(ic_df),
        "valid_ic_count": len(valid_ic),
        "mean_ic_proxy": float(valid_ic['ic_proxy'].mean()) if not valid_ic.empty else None,
        "positive_ic_count": len(valid_ic[valid_ic['ic_proxy'] > 0])
    }

def calculate_factor_ic_decay(score_history_df: pd.DataFrame, returns_df: pd.DataFrame, horizons: tuple[int, ...]) -> pd.DataFrame:
    # Requires panel data. Returning empty for now to satisfy interface without complex panel logic
    return pd.DataFrame()

def build_factor_ic_report(score_history_df: pd.DataFrame, returns_df: pd.DataFrame, profile: FactorResearchProfile) -> tuple[dict[str, pd.DataFrame], dict]:
    # Placeholder for full report
    return {}, {"warnings": ["Not implemented"]}
