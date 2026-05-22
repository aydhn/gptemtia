import pandas as pd
import numpy as np
from .factor_config import FactorResearchProfile

def calculate_forward_returns(returns_df: pd.DataFrame, horizon: int) -> pd.DataFrame:
    """
    Calculates forward returns over a given horizon.
    Uses cumulative sum for log returns, or compound for simple.
    Assuming log returns for simplicity based on project defaults.
    The forward return at time t is the sum of returns from t+1 to t+horizon.
    """
    if len(returns_df) <= horizon:
        return pd.DataFrame(index=returns_df.index, columns=returns_df.columns, dtype=float)

    forward_rets = returns_df.rolling(window=horizon).sum().shift(-horizon)
    return forward_rets

def build_factor_bucket_forward_returns(
    score_history_df: pd.DataFrame,
    forward_returns_df: pd.DataFrame,
    profile: FactorResearchProfile
) -> pd.DataFrame:
    """
    Maps historical factor scores to future returns to calculate average forward returns per bucket.
    score_history_df needs columns: symbol, timestamp, factor_id, bucket_label
    """
    if score_history_df.empty or forward_returns_df.empty:
        return pd.DataFrame()

    records = []

    # Ensure timestamp is datetime
    score_history_df['timestamp'] = pd.to_datetime(score_history_df['timestamp'])

    for factor_id, group in score_history_df.groupby('factor_id'):
         for bucket_label in ["top_factor_bucket", "middle_factor_bucket", "bottom_factor_bucket"]:
             bucket_group = group[group['bucket_label'] == bucket_label]

             returns = []
             for _, row in bucket_group.iterrows():
                  sym = row['symbol']
                  ts = row['timestamp']

                  if sym in forward_returns_df.columns and ts in forward_returns_df.index:
                      ret = forward_returns_df.loc[ts, sym]
                      if pd.notna(ret):
                           returns.append(ret)

             avg_ret = float(np.mean(returns)) if returns else None
             records.append({
                 "factor_id": factor_id,
                 "bucket_label": bucket_label,
                 "forward_return": avg_ret,
                 "observation_count": len(returns)
             })

    return pd.DataFrame(records)

def calculate_top_bottom_spread(bucket_returns_df: pd.DataFrame) -> pd.DataFrame:
    if bucket_returns_df.empty:
         return pd.DataFrame()

    spreads = []
    for factor_id, group in bucket_returns_df.groupby('factor_id'):
         top = group[group['bucket_label'] == 'top_factor_bucket']['forward_return'].values
         bottom = group[group['bucket_label'] == 'bottom_factor_bucket']['forward_return'].values

         top_ret = top[0] if len(top) > 0 else None
         bottom_ret = bottom[0] if len(bottom) > 0 else None

         spread = None
         if top_ret is not None and bottom_ret is not None:
              spread = top_ret - bottom_ret

         spreads.append({
             "factor_id": factor_id,
             "spread_return": spread
         })

    return pd.DataFrame(spreads)

def build_factor_backtest_results(
    bucket_returns_df: pd.DataFrame,
    spread_df: pd.DataFrame,
    profile: FactorResearchProfile
) -> pd.DataFrame:

    if bucket_returns_df.empty:
         return pd.DataFrame()

    results = []
    for factor_id in bucket_returns_df['factor_id'].unique():
         factor_buckets = bucket_returns_df[bucket_returns_df['factor_id'] == factor_id]

         top_row = factor_buckets[factor_buckets['bucket_label'] == 'top_factor_bucket']
         bottom_row = factor_buckets[factor_buckets['bucket_label'] == 'bottom_factor_bucket']

         spread_row = spread_df[spread_df['factor_id'] == factor_id]

         top_ret = top_row['forward_return'].values[0] if not top_row.empty else None
         bottom_ret = bottom_row['forward_return'].values[0] if not bottom_row.empty else None
         spread_ret = spread_row['spread_return'].values[0] if not spread_row.empty else None
         obs_count = int(factor_buckets['observation_count'].sum())

         # Hit rate requires individual trade logic, use simplified proxy for now
         hit_rate = 0.5 if spread_ret is not None and spread_ret > 0 else (0.0 if spread_ret is not None else None)

         results.append({
             "factor_id": str(factor_id),
             "timeframe": "1d",
             "horizon": profile.forward_return_horizon,
             "top_bucket_return": float(top_ret) if top_ret is not None else None,
             "bottom_bucket_return": float(bottom_ret) if bottom_ret is not None else None,
             "spread_return": float(spread_ret) if spread_ret is not None else None,
             "hit_rate": hit_rate,
             "observation_count": obs_count,
             "ic_proxy": None,
             "stability_score": None,
             "warnings": []
         })

    return pd.DataFrame(results)

def summarize_factor_backtest(results_df: pd.DataFrame) -> dict:
    if results_df.empty:
        return {"total_factors_tested": 0}

    positive_spreads = len(results_df[results_df['spread_return'] > 0])

    return {
        "total_factors_tested": len(results_df),
        "positive_spread_factors": positive_spreads,
        "average_spread": float(results_df['spread_return'].mean(skipna=True))
    }
