import pandas as pd
import numpy as np
import logging
from synthetic_indices.index_config import SyntheticIndexProfile

logger = logging.getLogger(__name__)

def calculate_multi_window_momentum(returns_df: pd.DataFrame, windows: tuple[int, ...]) -> pd.DataFrame:
    records = []

    for symbol in returns_df.columns:
        row = {"symbol": symbol}
        for window in windows:
            if len(returns_df) >= window:
                 mom = returns_df[symbol].iloc[-window:].sum() # Assuming log returns
            else:
                 mom = np.nan
            row[f"momentum_{window}"] = mom
        records.append(row)

    return pd.DataFrame(records)

def calculate_momentum_consistency(momentum_df: pd.DataFrame) -> pd.DataFrame:
    if momentum_df.empty:
        return momentum_df

    df = momentum_df.copy()
    mom_cols = [c for c in df.columns if c.startswith("momentum_")]

    if not mom_cols:
        df["momentum_consistency"] = np.nan
        return df

    def calc_consistency(row):
        vals = [row[c] for c in mom_cols if not pd.isna(row[c])]
        if not vals:
            return np.nan
        pos_count = sum(1 for v in vals if v > 0)
        return pos_count / len(vals)

    df["momentum_consistency"] = df.apply(calc_consistency, axis=1)
    return df

def calculate_relative_momentum_score(momentum_df: pd.DataFrame) -> pd.DataFrame:
    if momentum_df.empty:
        return momentum_df

    df = momentum_df.copy()
    mom_cols = [c for c in df.columns if c.startswith("momentum_")]

    if not mom_cols:
        return df

    # Standardize momentum across universe for each window
    scores = []
    for col in mom_cols:
        series = df[col]
        # Z-score roughly
        if series.std() > 0:
            z = (series - series.mean()) / series.std()
        else:
            z = series * 0
        scores.append(z)

    # Average Z-score
    if scores:
        df["relative_momentum_score"] = pd.concat(scores, axis=1).mean(axis=1)
        df["momentum_rank"] = df["relative_momentum_score"].rank(ascending=False, method="min").astype("Int64")

        # Labels
        def label_mom(rank, total):
            if pd.isna(rank) or total == 0:
                return "insufficient_data"
            pct = 1.0 - (rank - 1) / total
            if pct >= 0.8: return "strong_momentum"
            if pct >= 0.6: return "positive_momentum"
            if pct >= 0.4: return "neutral_momentum"
            if pct >= 0.2: return "negative_momentum"
            return "weak_momentum"

        total_valid = df["momentum_rank"].notna().sum()
        df["momentum_label"] = df["momentum_rank"].apply(lambda r: label_mom(r, total_valid))
    else:
        df["relative_momentum_score"] = np.nan
        df["momentum_rank"] = pd.NA
        df["momentum_label"] = "insufficient_data"

    return df

def build_relative_momentum_report(returns_df: pd.DataFrame, profile: SyntheticIndexProfile) -> tuple[pd.DataFrame, dict]:
    summary = {"warnings": [], "symbols_processed": 0}

    if returns_df.empty:
        summary["warnings"].append("Empty returns data.")
        return pd.DataFrame(), summary

    mom_df = calculate_multi_window_momentum(returns_df, profile.relative_strength_windows)
    mom_df = calculate_momentum_consistency(mom_df)
    mom_df = calculate_relative_momentum_score(mom_df)

    if "momentum_rank" in mom_df.columns:
         mom_df = mom_df.sort_values("momentum_rank")

    summary["symbols_processed"] = len(mom_df)

    return mom_df, summary
