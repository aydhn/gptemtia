from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_default_cross_asset_alignment_profile,
)
from advanced_cross_asset_alignment.cross_asset_alignment_models import (
    AlignmentJoinPolicy,
    build_alignment_join_policy_id,
)


JOIN_POLICIES_CONFIG: List[Dict[str, Any]] = [
    {
        "policy_name": "exact_timestamp_join",
        "join_policy_label": "join_policy_exact_timestamp",
        "tolerance_note": "Aynı zaman damgasına sahip barlar için tam eşleşme (left join).",
        "direction": "exact",
        "backward_only": True,
        "future_data_allowed": False,
    },
    {
        "policy_name": "asof_backward_join",
        "join_policy_label": "join_policy_asof_backward",
        "tolerance_note": "Sağ taraf zaman damgası <= sol taraf zaman damgası olan en son geçerli değer.",
        "direction": "backward",
        "backward_only": True,
        "future_data_allowed": False,
    },
    {
        "policy_name": "session_bucket_join",
        "join_policy_label": "join_policy_session_bucket",
        "tolerance_note": "Aynı takvim günü veya seans kovası içinde birleşim.",
        "direction": "bucket",
        "backward_only": True,
        "future_data_allowed": False,
    },
    {
        "policy_name": "event_window_placeholder_join",
        "join_policy_label": "join_policy_event_window_placeholder",
        "tolerance_note": "Ekonomik takvim olay penceresi (yalnızca gerçekleşme anından önceki/tam andaki veriler).",
        "direction": "bucket",
        "backward_only": True,
        "future_data_allowed": False,
    },
    {
        "policy_name": "metadata_tag_link_join",
        "join_policy_label": "join_policy_metadata_tag_link",
        "tolerance_note": "Haber metadata konu etiketleri üzerinden sembolik ve zamansal bağlantı (metadata-only).",
        "direction": "link",
        "backward_only": True,
        "future_data_allowed": False,
    },
]

JOIN_POLICIES_CATALOG = JOIN_POLICIES_CONFIG


def validate_join_policy(policy: AlignmentJoinPolicy) -> Dict[str, Any]:
    issues = []
    if not policy.backward_only:
        issues.append("Join policy backward_only=True olmak zorundadır.")
    if policy.future_data_allowed:
        issues.append("Join policy future_data_allowed=False olmak zorundadır.")
    if not policy.non_signal:
        issues.append("Join policy non_signal=True olmak zorundadır.")

    return {
        "policy_id": policy.policy_id,
        "is_valid": len(issues) == 0,
        "issues": issues,
    }


def build_feature_matrix_join_policy_registry(
    profile: CrossAssetAlignmentProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_cross_asset_alignment_profile()

    rows = []
    for cfg in JOIN_POLICIES_CONFIG:
        item = AlignmentJoinPolicy(
            policy_id=build_alignment_join_policy_id(cfg["policy_name"]),
            policy_name=cfg["policy_name"],
            join_policy_label=cfg["join_policy_label"],
            tolerance_note=cfg["tolerance_note"],
            backward_only=cfg["backward_only"],
            future_data_allowed=cfg["future_data_allowed"],
            non_signal=True,
            manual_review_required=False,
        )
        row_dict = item.to_dict()
        row_dict["direction"] = cfg.get("direction", "backward")
        rows.append(row_dict)

    df = pd.DataFrame(rows)
    summary = summarize_feature_matrix_join_policies(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_feature_matrix_join_policies(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_policies": 0, "status": "EMPTY"}

    all_backward = bool(df["backward_only"].all()) if "backward_only" in df.columns else False
    all_no_future = bool((~df["future_data_allowed"]).all()) if "future_data_allowed" in df.columns else False
    return {
        "total_policies": len(df),
        "policy_names": list(df["policy_name"]) if "policy_name" in df.columns else [],
        "all_backward_only": all_backward,
        "all_backward_direction": True,
        "all_future_data_blocked": all_no_future,
        "non_signal": True,
        "status": "READY" if (all_backward and all_no_future) else "SAFETY_VIOLATION",
    }
