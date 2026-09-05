from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_fusion.fusion_feature_config import (
    FusionFeatureProfile,
    get_default_fusion_feature_profile,
)
from advanced_feature_fusion.fusion_feature_models import (
    FusionPolicy,
    build_fusion_policy_id,
)


ASOF_JOIN_POLICIES: List[Dict[str, Any]] = [
    {
        "policy_name": "strict_backward_asof_direction_policy",
        "policy_type": "asof_join",
        "description": "Asof join yönü kesinlikle 'backward' olmalıdır; 'forward' veya 'nearest' kesinlikle yasaktır.",
        "future_data_allowed": False,
        "full_text_allowed": False,
        "destructive_action_allowed": False,
        "non_signal": True,
        "manual_review_required": False,
    },
    {
        "policy_name": "non_mutating_dataframe_policy",
        "policy_type": "asof_join",
        "description": "Join işlemleri girdi DataFrame'lerini in-place mutate etmez, daima kopya üzerinde çalışır.",
        "future_data_allowed": False,
        "full_text_allowed": False,
        "destructive_action_allowed": False,
        "non_signal": True,
        "manual_review_required": False,
    },
    {
        "policy_name": "deterministic_sorted_timestamp_policy",
        "policy_type": "asof_join",
        "description": "Join öncesinde hem sol hem sağ DataFrame deterministik olarak zaman damgasına göre sıralanır.",
        "future_data_allowed": False,
        "full_text_allowed": False,
        "destructive_action_allowed": False,
        "non_signal": True,
        "manual_review_required": False,
    },
]


def build_fusion_asof_join_policy_registry(
    profile: FusionFeatureProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_fusion_feature_profile()
    rows = []
    for spec in ASOF_JOIN_POLICIES:
        p = FusionPolicy(
            policy_id=build_fusion_policy_id(spec["policy_name"], spec["policy_type"]),
            policy_name=spec["policy_name"],
            policy_type=spec["policy_type"],
            description=spec["description"],
            future_data_allowed=spec["future_data_allowed"],
            full_text_allowed=spec["full_text_allowed"],
            destructive_action_allowed=spec["destructive_action_allowed"],
            non_signal=spec["non_signal"],
            manual_review_required=spec["manual_review_required"],
        )
        rows.append(p.to_dict())

    df = pd.DataFrame(rows)
    summary = summarize_fusion_asof_join_policies(df)
    summary["active_profile"] = active_profile.name
    summary["status"] = "READY"
    return df, summary


def safe_fusion_asof_join_backward(
    left_df: pd.DataFrame,
    right_df: pd.DataFrame,
    left_on: str,
    right_on: str,
    by: str | None = None,
    tolerance: str | None = None,
) -> pd.DataFrame:
    """Perform deterministic backward-only asof join without mutating inputs."""
    if left_df.empty:
        return left_df.copy()
    if right_df.empty:
        return left_df.copy()

    # Copies to ensure immutability of inputs
    l_copy = left_df.copy()
    r_copy = right_df.copy()

    # Convert timestamps
    l_copy[left_on] = pd.to_datetime(l_copy[left_on])
    r_copy[right_on] = pd.to_datetime(r_copy[right_on])

    # Sort deterministically
    l_copy = l_copy.sort_values(by=left_on).reset_index(drop=True)
    r_copy = r_copy.sort_values(by=right_on).reset_index(drop=True)

    # Perform backward-only asof join
    tol = pd.Timedelta(tolerance) if tolerance is not None else None
    merged = pd.merge_asof(
        l_copy,
        r_copy,
        left_on=left_on,
        right_on=right_on,
        by=by,
        direction="backward",
        tolerance=tol,
    )
    return merged


def summarize_fusion_asof_join_policies(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_policies": 0, "status": "EMPTY"}
    return {
        "total_policies": len(df),
        "backward_only_enforced": True,
        "zero_future_data_enforced": bool((~df["future_data_allowed"]).all()),
        "status": "READY",
    }


def get_asof_join_policies() -> List[Dict[str, Any]]:
    """Return list of asof join policies."""
    return [dict(p) for p in ASOF_JOIN_POLICIES]


def get_asof_join_policies_summary() -> Dict[str, Any]:
    """Return summary dictionary of asof join policies."""
    df, summary = build_fusion_asof_join_policy_registry()
    summary["policy_count"] = len(df)
    summary["join_direction"] = "backward"
    return summary
