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


TIMESTAMP_POLICIES: List[Dict[str, Any]] = [
    {
        "policy_name": "universal_utc_iso8601_fusion_policy",
        "policy_type": "timestamp_alignment",
        "description": "Tüm bağlamsal zaman damgaları (fiyat, makro, takvim, haber) UTC ISO-8601 formatına zorunlu hizalanır.",
        "future_data_allowed": False,
        "full_text_allowed": False,
        "destructive_action_allowed": False,
        "non_signal": True,
        "manual_review_required": False,
    },
    {
        "policy_name": "monotonic_timestamp_ordering_policy",
        "policy_type": "timestamp_alignment",
        "description": "Zaman serisi artan sırada olmalı ve context zaman damgası ana bar zaman damgasını aşamaz.",
        "future_data_allowed": False,
        "full_text_allowed": False,
        "destructive_action_allowed": False,
        "non_signal": True,
        "manual_review_required": False,
    },
    {
        "policy_name": "release_timestamp_precedence_policy",
        "policy_type": "timestamp_alignment",
        "description": "Makro ve takvim olaylarında dönem/referans tarihi değil resmi yayınlanma zaman damgası esas alınır.",
        "future_data_allowed": False,
        "full_text_allowed": False,
        "destructive_action_allowed": False,
        "non_signal": True,
        "manual_review_required": False,
    },
]

TIMESTAMP_ALIGNMENT_POLICIES = TIMESTAMP_POLICIES


def build_fusion_timestamp_alignment_policy_registry(
    profile: FusionFeatureProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_fusion_feature_profile()
    rows = []
    for spec in TIMESTAMP_POLICIES:
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
    summary = summarize_fusion_timestamp_alignment_policies(df)
    summary["active_profile"] = active_profile.name
    summary["status"] = "READY"
    return df, summary


def validate_fusion_timestamp_order(
    df: pd.DataFrame,
    base_ts: str = "timestamp",
    context_ts: str = "context_timestamp",
) -> Dict[str, Any]:
    if df.empty or base_ts not in df.columns:
        return {
            "valid": True,
            "violations_count": 0,
            "status": "PASS",
            "message": "Empty dataframe or missing base timestamp column.",
        }

    b_ts = pd.to_datetime(df[base_ts])
    if not b_ts.is_monotonic_increasing:
        return {
            "valid": False,
            "violations_count": 1,
            "status": "FAIL",
            "message": f"Base timestamp column '{base_ts}' is not monotonically increasing.",
        }

    if context_ts in df.columns:
        c_ts = pd.to_datetime(df[context_ts])
        violations = df[c_ts > b_ts]
        viol_count = len(violations)
        passed = viol_count == 0
        return {
            "valid": passed,
            "violations_count": viol_count,
            "status": "PASS" if passed else "FAIL",
            "message": "All context timestamps are on or prior to base timestamps." if passed else f"Gelecek zaman sızıntısı: {viol_count} satırda context zamanı ana bar zamanından ileride!",
        }

    return {
        "valid": True,
        "violations_count": 0,
        "status": "PASS",
        "message": "Base timestamp order verified (monotonic increasing).",
    }


def summarize_fusion_timestamp_alignment_policies(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_policies": 0, "status": "EMPTY"}
    return {
        "total_policies": len(df),
        "zero_future_data_enforced": bool((~df["future_data_allowed"]).all()),
        "status": "READY",
    }


def get_timestamp_alignment_policies() -> List[Dict[str, Any]]:
    """Return list of timestamp alignment policies."""
    return [dict(p) for p in TIMESTAMP_ALIGNMENT_POLICIES]


def get_timestamp_alignment_policies_summary() -> Dict[str, Any]:
    """Return summary dictionary of timestamp alignment policies."""
    df, summary = build_fusion_timestamp_alignment_policy_registry()
    summary["policy_count"] = len(df)
    return summary
