from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_fusion.fusion_feature_config import (
    FusionFeatureProfile,
    get_default_fusion_feature_profile,
)
from advanced_feature_fusion.fusion_feature_models import (
    FusionContract,
    build_fusion_contract_id,
)


CALENDAR_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_name": "economic_calendar_event_context_contract",
        "fusion_family": "fusion_family_calendar",
        "source_domains": ["economic_calendar", "cross_asset_alignment"],
        "required_fields": ["event_id", "event_name", "country_code", "scheduled_time"],
        "optional_fields": ["currency", "period"],
        "timestamp_field": "scheduled_time",
        "join_policy": "fusion_join_policy_event_window_placeholder",
    },
    {
        "contract_name": "pre_event_window_context_contract",
        "fusion_family": "fusion_family_calendar",
        "source_domains": ["economic_calendar"],
        "required_fields": ["event_id", "pre_window_active", "hours_to_event"],
        "optional_fields": ["window_size_hours"],
        "timestamp_field": "scheduled_time",
        "join_policy": "fusion_join_policy_event_window_placeholder",
    },
    {
        "contract_name": "post_event_window_context_contract",
        "fusion_family": "fusion_family_calendar",
        "source_domains": ["economic_calendar"],
        "required_fields": ["event_id", "post_window_active", "hours_since_release"],
        "optional_fields": ["actual_release_time"],
        "timestamp_field": "actual_release_time",
        "join_policy": "fusion_join_policy_release_time_only",
    },
    {
        "contract_name": "event_importance_context_contract",
        "fusion_family": "fusion_family_calendar",
        "source_domains": ["economic_calendar"],
        "required_fields": ["event_id", "importance_tier", "importance_weight_norm"],
        "optional_fields": ["historical_volatility_impact"],
        "timestamp_field": "scheduled_time",
        "join_policy": "fusion_join_policy_backward_asof",
    },
]


def build_calendar_event_fusion_contract_registry(
    profile: FusionFeatureProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_fusion_feature_profile()
    rows = []
    for spec in CALENDAR_CONTRACTS:
        c = FusionContract(
            contract_id=build_fusion_contract_id(spec["contract_name"], spec["fusion_family"]),
            contract_name=spec["contract_name"],
            fusion_family=spec["fusion_family"],
            source_domains=spec["source_domains"],
            required_fields=spec["required_fields"],
            optional_fields=spec["optional_fields"],
            timestamp_field=spec["timestamp_field"],
            join_policy=spec["join_policy"],
            no_lookahead_policy="strictly_enforced_no_future_data",
            metadata_only_required=True,
            non_signal=True,
            manual_review_required=False,
        )
        rows.append(c.to_dict())

    df = pd.DataFrame(rows)
    summary = summarize_calendar_event_fusion_contracts(df)
    summary["active_profile"] = active_profile.name
    summary["status"] = "READY"
    return df, summary


def summarize_calendar_event_fusion_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_contracts": 0, "status": "EMPTY"}
    return {
        "total_contracts": len(df),
        "event_window_count": int((df["join_policy"] == "fusion_join_policy_event_window_placeholder").sum()),
        "non_signal_guaranteed": bool(df["non_signal"].all()),
        "status": "READY",
    }


def get_calendar_event_contracts() -> List[Dict[str, Any]]:
    """Return list of calendar event fusion contracts."""
    return [dict(c) for c in CALENDAR_CONTRACTS]
