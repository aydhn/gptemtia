from typing import Tuple, Dict, Any, Optional, List
import pandas as pd

from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_default_cross_asset_alignment_profile,
)


ASOF_JOIN_POLICIES_INFO: List[Dict[str, Any]] = [
    {
        "policy_name": "safe_backward_asof_standard",
        "direction": "backward",
        "allow_exact_matches": True,
        "future_data_allowed": False,
        "description": "Standart geriye dönük asof birleşimi; sağ taraf zamanı sol tarafa eşit veya geçmiş olmalıdır.",
    },
    {
        "policy_name": "safe_backward_asof_macro_lag",
        "direction": "backward",
        "allow_exact_matches": True,
        "future_data_allowed": False,
        "description": "Makro duyuruları için geriye dönük asof; açıklanmamış veri asla geçmişe bağlanamaz.",
    },
    {
        "policy_name": "safe_backward_asof_calendar_window",
        "direction": "backward",
        "allow_exact_matches": True,
        "future_data_allowed": False,
        "description": "Ekonomik takvim olayları için geriye dönük pencere; olay öncesi ve anı hizalanır.",
    },
]


def safe_asof_join_backward(
    left_df: pd.DataFrame,
    right_df: pd.DataFrame,
    left_on: str,
    right_on: str,
    by: Optional[str] = None,
    tolerance: Optional[Any] = None,
) -> pd.DataFrame:
    """Safe backward-only asof join protecting against lookahead bias.
    
    Guarantees:
    - Never mutates input dataframes (works on copies).
    - direction='backward' is strictly enforced.
    - No forward looking or nearest forward values allowed.
    """
    if left_df.empty:
        return left_df.copy()
    if right_df.empty:
        return left_df.copy()

    # Work strictly on copies to prevent mutation
    l_df = left_df.copy()
    r_df = right_df.copy()

    # Convert timestamps to datetime for accurate merge_asof if strings
    left_is_str = False
    right_is_str = False
    if pd.api.types.is_string_dtype(l_df[left_on]):
        left_is_str = True
        l_df["_join_left_ts"] = pd.to_datetime(l_df[left_on], utc=True)
        join_left_on = "_join_left_ts"
    else:
        join_left_on = left_on

    if pd.api.types.is_string_dtype(r_df[right_on]):
        right_is_str = True
        r_df["_join_right_ts"] = pd.to_datetime(r_df[right_on], utc=True)
        join_right_on = "_join_right_ts"
    else:
        join_right_on = right_on

    # merge_asof requires both dataframes to be sorted on the join key
    l_df = l_df.sort_values(join_left_on).reset_index(drop=True)
    r_df = r_df.sort_values(join_right_on).reset_index(drop=True)

    # Perform backward-only asof join
    kwargs: Dict[str, Any] = {
        "left_on": join_left_on,
        "right_on": join_right_on,
        "direction": "backward",
    }
    if by is not None and by in l_df.columns and by in r_df.columns:
        kwargs["by"] = by
    if tolerance is not None:
        kwargs["tolerance"] = tolerance

    merged = pd.merge_asof(l_df, r_df, **kwargs)

    # Clean up temporary timestamp helper columns if created
    if left_is_str and "_join_left_ts" in merged.columns:
        merged = merged.drop(columns=["_join_left_ts"])
    if right_is_str and "_join_right_ts" in merged.columns:
        merged = merged.drop(columns=["_join_right_ts"])

    return merged


def build_asof_join_policy_registry(
    profile: CrossAssetAlignmentProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_cross_asset_alignment_profile()
    df = pd.DataFrame(ASOF_JOIN_POLICIES_INFO)
    summary = summarize_asof_join_policies(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_asof_join_policies(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_asof_policies": 0, "status": "EMPTY"}

    all_backward = bool((df["direction"] == "backward").all()) if "direction" in df.columns else False
    return {
        "total_asof_policies": len(df),
        "all_direction_backward": all_backward,
        "future_data_allowed": False,
        "non_signal": True,
        "status": "READY" if all_backward else "SAFETY_VIOLATION",
    }
