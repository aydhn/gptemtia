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


RELEASE_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_name": "release_actual_forecast_previous_context_contract",
        "fusion_family": "fusion_family_release_event",
        "source_domains": ["economic_calendar", "macro_providers"],
        "required_fields": ["event_id", "actual", "forecast", "previous"],
        "optional_fields": ["unit", "scale"],
        "timestamp_field": "actual_release_time",
        "join_policy": "fusion_join_policy_release_time_only",
    },
    {
        "contract_name": "release_surprise_placeholder_contract",
        "fusion_family": "fusion_family_release_event",
        "source_domains": ["economic_calendar"],
        "required_fields": ["event_id", "surprise_raw", "surprise_direction_neutral"],
        "optional_fields": ["surprise_std_placeholder"],
        "timestamp_field": "actual_release_time",
        "join_policy": "fusion_join_policy_release_time_only",
    },
    {
        "contract_name": "revised_previous_context_contract",
        "fusion_family": "fusion_family_release_event",
        "source_domains": ["economic_calendar"],
        "required_fields": ["event_id", "revised_previous", "is_previous_revised"],
        "optional_fields": ["revision_delta"],
        "timestamp_field": "actual_release_time",
        "join_policy": "fusion_join_policy_release_time_only",
    },
    {
        "contract_name": "release_delay_context_contract",
        "fusion_family": "fusion_family_release_event",
        "source_domains": ["economic_calendar"],
        "required_fields": ["event_id", "scheduled_time", "actual_release_time", "delay_minutes"],
        "optional_fields": ["delay_category"],
        "timestamp_field": "actual_release_time",
        "join_policy": "fusion_join_policy_release_time_only",
    },
]


def build_release_event_fusion_contract_registry(
    profile: FusionFeatureProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_fusion_feature_profile()
    rows = []
    for spec in RELEASE_CONTRACTS:
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
    summary = summarize_release_event_fusion_contracts(df)
    summary["active_profile"] = active_profile.name
    summary["status"] = "READY"
    return df, summary


def summarize_release_event_fusion_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_contracts": 0, "status": "EMPTY"}
    return {
        "total_contracts": len(df),
        "release_time_only_contracts": int((df["join_policy"] == "fusion_join_policy_release_time_only").sum()),
        "non_signal_guaranteed": bool(df["non_signal"].all()),
        "status": "READY",
    }


def get_release_event_contracts() -> List[Dict[str, Any]]:
    """Return list of release event fusion contracts."""
    return [dict(c) for c in RELEASE_CONTRACTS]
