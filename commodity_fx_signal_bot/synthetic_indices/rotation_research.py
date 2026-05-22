import pandas as pd
import numpy as np
import logging
from synthetic_indices.index_config import SyntheticIndexProfile
from synthetic_indices.index_models import RotationRecord
from synthetic_indices.relative_momentum import calculate_multi_window_momentum, calculate_relative_momentum_score

logger = logging.getLogger(__name__)

def calculate_rotation_scores(returns_df: pd.DataFrame, profile: SyntheticIndexProfile) -> pd.DataFrame:
    if returns_df.empty:
        return pd.DataFrame()

    records = []
    lookback = profile.rotation_lookback

    # Calculate simple momentum for rotation lookback
    for symbol in returns_df.columns:
        if len(returns_df) >= lookback:
            ret_series = returns_df[symbol].iloc[-lookback:]
            total_ret = ret_series.sum()
            volatility = ret_series.std()

            if pd.isna(volatility) or volatility == 0:
                 vol_penalty = 0.0
            else:
                 vol_penalty = volatility

            # Simple Sharpe-like score
            score = total_ret / vol_penalty if vol_penalty > 0 else 0

            records.append({
                "symbol": symbol,
                "recent_return": total_ret,
                "volatility_penalty": vol_penalty,
                "base_rotation_score": score
            })
        else:
             records.append({
                "symbol": symbol,
                "recent_return": np.nan,
                "volatility_penalty": np.nan,
                "base_rotation_score": np.nan
            })

    df = pd.DataFrame(records)

    # Cross-sectional rank
    if not df.empty and "base_rotation_score" in df.columns:
         df["rotation_score"] = df["base_rotation_score"]
         df["rotation_rank"] = df["rotation_score"].rank(ascending=False, method="min").astype("Int64")

    return df

def build_rotation_records(rotation_df: pd.DataFrame, previous_rotation_df: pd.DataFrame | None, timeframe: str, profile: SyntheticIndexProfile) -> list[RotationRecord]:
    records = []

    if rotation_df.empty:
        return records

    prev_map = {}
    if previous_rotation_df is not None and not previous_rotation_df.empty and "rotation_rank" in previous_rotation_df.columns:
         prev_map = previous_rotation_df.set_index("symbol")["rotation_rank"].to_dict()

    total_symbols = rotation_df["rotation_rank"].notna().sum()

    for _, row in rotation_df.iterrows():
        sym = row["symbol"]
        rank = row.get("rotation_rank", pd.NA)
        score = row.get("rotation_score", np.nan)

        prev_rank = prev_map.get(sym, pd.NA)

        rank_delta = None
        if pd.notna(rank) and pd.notna(prev_rank):
            rank_delta = int(prev_rank) - int(rank) # Positive means improvement (lower rank number)

        # Determine label
        label = "unknown_rotation"
        if pd.isna(rank):
            label = "insufficient_rotation_data"
        else:
            if rank <= profile.rotation_top_n:
                label = "rotation_candidate_leader"
            elif rank > total_symbols - profile.rotation_bottom_n:
                label = "rotation_candidate_laggard"
            elif rank_delta is not None:
                if rank_delta > 0:
                    label = "rotation_candidate_improving"
                elif rank_delta < 0:
                    label = "rotation_candidate_weakening"
                else:
                     label = "rotation_candidate_neutral"
            else:
                 label = "rotation_candidate_neutral"

        records.append(RotationRecord(
            symbol=sym,
            timeframe=timeframe,
            lookback=profile.rotation_lookback,
            rotation_score=score,
            rotation_rank=rank,
            rotation_label=label,
            previous_rank=prev_rank,
            rank_delta=rank_delta,
            warnings=[]
        ))

    return records

def rotation_records_to_dataframe(records: list[RotationRecord]) -> pd.DataFrame:
    if not records:
        return pd.DataFrame()
    return pd.DataFrame([vars(r) for r in records])

def calculate_rotation_stability(current_df: pd.DataFrame, previous_df: pd.DataFrame | None) -> dict:
    summary = {
        "stability_score": np.nan,
        "avg_rank_delta": np.nan,
        "turnover_proxy": np.nan
    }

    if current_df.empty or previous_df is None or previous_df.empty:
        return summary

    if "rank_delta" in current_df.columns:
         deltas = current_df["rank_delta"].dropna().abs()
         if not deltas.empty:
              summary["avg_rank_delta"] = float(deltas.mean())
              summary["turnover_proxy"] = float(deltas.sum())

              # Mock stability score: 1.0 means no changes, lower means more churn
              max_churn = len(current_df) * len(current_df) / 2
              churn = deltas.sum()
              summary["stability_score"] = float(max(0, 1.0 - (churn / max_churn)))

    return summary

def build_universe_rotation_report(returns_df: pd.DataFrame, previous_rotation_df: pd.DataFrame | None, timeframe: str, profile: SyntheticIndexProfile) -> tuple[pd.DataFrame, dict]:
    summary = {"warnings": [], "symbols_processed": 0}

    if returns_df.empty:
        summary["warnings"].append("Empty returns data.")
        return pd.DataFrame(), summary

    rot_df = calculate_rotation_scores(returns_df, profile)
    records = build_rotation_records(rot_df, previous_rotation_df, timeframe, profile)
    final_df = rotation_records_to_dataframe(records)

    if "rotation_rank" in final_df.columns:
         final_df = final_df.sort_values("rotation_rank")

    stab = calculate_rotation_stability(final_df, previous_rotation_df)
    summary.update(stab)
    summary["symbols_processed"] = len(final_df)

    return final_df, summary
