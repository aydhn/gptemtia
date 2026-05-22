import pandas as pd
import logging
from synthetic_indices.index_config import SyntheticIndexProfile

logger = logging.getLogger(__name__)

def identify_cross_asset_leaders(rs_df: pd.DataFrame, momentum_df: pd.DataFrame, top_n: int = 5) -> pd.DataFrame:
    if rs_df.empty or momentum_df.empty:
        return pd.DataFrame()

    df = pd.merge(rs_df, momentum_df, on="symbol", how="inner")

    # Leader criteria: high relative strength rank + high momentum rank
    if "relative_rank" in df.columns and "momentum_rank" in df.columns:
         df["leadership_score"] = df["relative_rank"] + df["momentum_rank"] # Lower score = higher rank = better
         df = df.sort_values("leadership_score")
         return df.head(top_n)

    return pd.DataFrame()

def identify_cross_asset_laggards(rs_df: pd.DataFrame, momentum_df: pd.DataFrame, bottom_n: int = 5) -> pd.DataFrame:
    if rs_df.empty or momentum_df.empty:
        return pd.DataFrame()

    df = pd.merge(rs_df, momentum_df, on="symbol", how="inner")

    # Laggard criteria: low relative strength rank + low momentum rank
    if "relative_rank" in df.columns and "momentum_rank" in df.columns:
         df["laggard_score"] = df["relative_rank"] + df["momentum_rank"] # Higher score = lower rank = worse
         df = df.sort_values("laggard_score", ascending=False)
         return df.head(bottom_n)

    return pd.DataFrame()

def build_leadership_laggard_table(rs_df: pd.DataFrame, momentum_df: pd.DataFrame, rotation_df: pd.DataFrame | None = None) -> pd.DataFrame:
    if rs_df.empty or momentum_df.empty:
        return pd.DataFrame()

    df = pd.merge(rs_df, momentum_df, on="symbol", how="outer")

    if rotation_df is not None and not rotation_df.empty:
         df = pd.merge(df, rotation_df[["symbol", "rotation_label", "rotation_rank"]], on="symbol", how="left")
    else:
         df["rotation_label"] = "unknown_rotation"
         df["rotation_rank"] = pd.NA

    if "relative_rank" in df.columns and "momentum_rank" in df.columns:
         df["leadership_score"] = df["relative_rank"] + df["momentum_rank"]

         # Define leadership group based on score
         def get_group(score, count):
             if pd.isna(score) or count == 0:
                 return "unknown"
             # lower score is better
             pct = score / (count * 2) # max score is roughly count * 2
             if pct <= 0.2: return "Leader"
             if pct <= 0.4: return "Upper Tier"
             if pct <= 0.6: return "Middle Tier"
             if pct <= 0.8: return "Lower Tier"
             return "Laggard"

         valid_count = df["relative_rank"].notna().sum()
         df["leadership_group"] = df["leadership_score"].apply(lambda s: get_group(s, valid_count))

         df = df.sort_values("leadership_score")

    return df

def summarize_leadership_laggard(table_df: pd.DataFrame) -> dict:
    summary = {"total_symbols": 0, "leaders": 0, "laggards": 0}
    if table_df.empty:
        return summary

    summary["total_symbols"] = len(table_df)
    if "leadership_group" in table_df.columns:
         summary["leaders"] = (table_df["leadership_group"] == "Leader").sum()
         summary["laggards"] = (table_df["leadership_group"] == "Laggard").sum()

    return summary

def build_leadership_laggard_report(rs_df: pd.DataFrame, momentum_df: pd.DataFrame, rotation_df: pd.DataFrame | None, profile: SyntheticIndexProfile) -> tuple[pd.DataFrame, dict]:
    summary = {"warnings": []}

    df = build_leadership_laggard_table(rs_df, momentum_df, rotation_df)

    if df.empty:
         summary["warnings"].append("Empty data provided for leadership report.")
         return df, summary

    metrics = summarize_leadership_laggard(df)
    summary.update(metrics)

    # Filter columns to return a cleaner report
    cols = ["symbol", "relative_strength_label", "momentum_label", "rotation_label", "leadership_score", "leadership_group"]
    available_cols = [c for c in cols if c in df.columns]

    return df[available_cols], summary
