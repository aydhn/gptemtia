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


MACRO_LAG_POLICIES: List[Dict[str, Any]] = [
    {
        "policy_name": "strict_release_timestamp_availability_policy",
        "policy_type": "macro_lag",
        "description": "Makro veri değeri sadece release_timestamp <= base_timestamp olduğunda kullanılabilir.",
        "future_data_allowed": False,
        "full_text_allowed": False,
        "destructive_action_allowed": False,
        "non_signal": True,
        "manual_review_required": False,
    },
    {
        "policy_name": "revision_effective_timestamp_tracking_policy",
        "policy_type": "macro_lag",
        "description": "Revize edilmiş makro veri değeri sadece revision_timestamp sonrasında devreye girer.",
        "future_data_allowed": False,
        "full_text_allowed": False,
        "destructive_action_allowed": False,
        "non_signal": True,
        "manual_review_required": False,
    },
    {
        "policy_name": "unknown_release_lag_manual_review_policy",
        "policy_type": "macro_lag",
        "description": "Eğer release gecikmesi veya yayın saati bilinmiyorsa otomatik join engellenir ve manuel inceleme gerekir.",
        "future_data_allowed": False,
        "full_text_allowed": False,
        "destructive_action_allowed": False,
        "non_signal": True,
        "manual_review_required": True,
    },
]


def build_macro_release_lag_policy_registry(
    profile: FusionFeatureProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_fusion_feature_profile()
    rows = []
    for spec in MACRO_LAG_POLICIES:
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
    summary = summarize_macro_release_lag_policies(df)
    summary["active_profile"] = active_profile.name
    summary["status"] = "READY"
    return df, summary


def validate_macro_release_available_at(
    row: Dict[str, Any],
    base_timestamp_field: str = "timestamp",
    release_timestamp_field: str = "release_timestamp",
) -> Dict[str, Any]:
    base_ts = row.get(base_timestamp_field)
    rel_ts = row.get(release_timestamp_field)

    if base_ts is None or rel_ts is None:
        return {
            "available": False,
            "reason": "Missing base or release timestamp",
            "manual_review_required": True,
        }

    base_dt = pd.to_datetime(base_ts)
    rel_dt = pd.to_datetime(rel_ts)

    if rel_dt <= base_dt:
        return {
            "available": True,
            "reason": "Release timestamp is on or before base timestamp (no lookahead)",
            "manual_review_required": False,
        }
    else:
        return {
            "available": False,
            "reason": "Release timestamp is in future relative to base timestamp (lookahead violation)",
            "manual_review_required": True,
        }


def summarize_macro_release_lag_policies(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_policies": 0, "status": "EMPTY"}
    return {
        "total_policies": len(df),
        "zero_future_data_enforced": bool((~df["future_data_allowed"]).all()),
        "manual_review_count": int(df["manual_review_required"].sum()),
        "status": "READY",
    }


def get_macro_release_lag_policies() -> List[Dict[str, Any]]:
    """Return list of macro release lag policies."""
    return [dict(p) for p in MACRO_LAG_POLICIES]


def get_macro_release_lag_policies_summary() -> Dict[str, Any]:
    """Return summary dictionary of macro release lag policies."""
    df, summary = build_macro_release_lag_policy_registry()
    summary["policy_count"] = len(df)
    summary["no_lookahead_mandate"] = True
    return summary
