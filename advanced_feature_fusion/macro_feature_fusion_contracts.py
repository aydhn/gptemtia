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


MACRO_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_name": "macro_timeseries_context_contract",
        "fusion_family": "fusion_family_macro",
        "source_domains": ["macro_providers", "cross_asset_alignment"],
        "required_fields": ["indicator_id", "value", "release_timestamp"],
        "optional_fields": ["previous_value", "period_name"],
        "timestamp_field": "release_timestamp",
        "join_policy": "fusion_join_policy_backward_asof",
    },
    {
        "contract_name": "macro_release_context_contract",
        "fusion_family": "fusion_family_macro",
        "source_domains": ["macro_providers", "economic_calendar"],
        "required_fields": ["indicator_id", "release_lag_days", "is_preliminary"],
        "optional_fields": ["source_organization", "calendar_linked"],
        "timestamp_field": "release_timestamp",
        "join_policy": "fusion_join_policy_release_time_only",
    },
    {
        "contract_name": "macro_revision_context_contract",
        "fusion_family": "fusion_family_macro",
        "source_domains": ["macro_providers"],
        "required_fields": ["indicator_id", "revised_value", "revision_timestamp"],
        "optional_fields": ["revision_delta", "revision_count"],
        "timestamp_field": "revision_timestamp",
        "join_policy": "fusion_join_policy_release_time_only",
    },
    {
        "contract_name": "macro_frequency_unit_context_contract",
        "fusion_family": "fusion_family_macro",
        "source_domains": ["macro_providers"],
        "required_fields": ["indicator_id", "frequency", "unit_of_measure"],
        "optional_fields": ["seasonal_adjustment", "multiplier"],
        "timestamp_field": "metadata_effective_timestamp",
        "join_policy": "fusion_join_policy_backward_asof",
    },
]


def build_macro_feature_fusion_contract_registry(
    profile: FusionFeatureProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_fusion_feature_profile()
    rows = []
    for spec in MACRO_CONTRACTS:
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
    summary = summarize_macro_feature_fusion_contracts(df)
    summary["active_profile"] = active_profile.name
    summary["status"] = "READY"
    return df, summary


def summarize_macro_feature_fusion_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_contracts": 0, "status": "EMPTY"}
    return {
        "total_contracts": len(df),
        "backward_asof_count": int((df["join_policy"] == "fusion_join_policy_backward_asof").sum()),
        "non_signal_guaranteed": bool(df["non_signal"].all()),
        "status": "READY",
    }


def get_macro_timeseries_contracts() -> List[Dict[str, Any]]:
    """Return list of macro timeseries fusion contracts."""
    return [dict(c) for c in MACRO_CONTRACTS]
