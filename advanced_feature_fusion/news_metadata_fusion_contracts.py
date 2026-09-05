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


NEWS_METADATA_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_name": "news_topic_metadata_contract",
        "fusion_family": "fusion_family_news_metadata",
        "source_domains": ["news_metadata", "cross_asset_alignment"],
        "required_fields": ["news_id", "topic", "published_timestamp"],
        "optional_fields": ["subtopic", "topic_confidence"],
        "timestamp_field": "published_timestamp",
        "join_policy": "fusion_join_policy_backward_asof",
    },
    {
        "contract_name": "news_asset_tag_metadata_contract",
        "fusion_family": "fusion_family_news_metadata",
        "source_domains": ["news_metadata"],
        "required_fields": ["news_id", "asset_tags", "published_timestamp"],
        "optional_fields": ["primary_asset_symbol", "tag_count"],
        "timestamp_field": "published_timestamp",
        "join_policy": "fusion_join_policy_metadata_tag_link",
    },
    {
        "contract_name": "news_macro_tag_metadata_contract",
        "fusion_family": "fusion_family_news_metadata",
        "source_domains": ["news_metadata", "macro_providers"],
        "required_fields": ["news_id", "macro_tags", "published_timestamp"],
        "optional_fields": ["macro_category", "indicator_reference"],
        "timestamp_field": "published_timestamp",
        "join_policy": "fusion_join_policy_metadata_tag_link",
    },
    {
        "contract_name": "news_event_linkage_metadata_contract",
        "fusion_family": "fusion_family_news_metadata",
        "source_domains": ["news_metadata", "economic_calendar"],
        "required_fields": ["news_id", "event_reference", "published_timestamp"],
        "optional_fields": ["linked_event_id", "linkage_type"],
        "timestamp_field": "published_timestamp",
        "join_policy": "fusion_join_policy_metadata_tag_link",
    },
    {
        "contract_name": "news_source_reference_metadata_contract",
        "fusion_family": "fusion_family_news_metadata",
        "source_domains": ["news_metadata"],
        "required_fields": ["news_id", "source_reference_id", "source_category"],
        "optional_fields": ["source_tier", "is_official_feed"],
        "timestamp_field": "published_timestamp",
        "join_policy": "fusion_join_policy_backward_asof",
    },
    {
        "contract_name": "news_freshness_metadata_contract",
        "fusion_family": "fusion_family_news_metadata",
        "source_domains": ["news_metadata"],
        "required_fields": ["news_id", "age_minutes_at_join", "published_timestamp"],
        "optional_fields": ["decay_half_life_placeholder"],
        "timestamp_field": "published_timestamp",
        "join_policy": "fusion_join_policy_backward_asof",
    },
]


def build_news_metadata_fusion_contract_registry(
    profile: FusionFeatureProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_fusion_feature_profile()
    rows = []
    for spec in NEWS_METADATA_CONTRACTS:
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
    summary = summarize_news_metadata_fusion_contracts(df)
    summary["active_profile"] = active_profile.name
    summary["status"] = "READY"
    return df, summary


def summarize_news_metadata_fusion_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_contracts": 0, "status": "EMPTY"}
    return {
        "total_contracts": len(df),
        "metadata_only_verified": bool(df["metadata_only_required"].all()),
        "non_signal_guaranteed": bool(df["non_signal"].all()),
        "status": "READY",
    }


def get_news_metadata_contracts() -> List[Dict[str, Any]]:
    """Return list of news metadata fusion contracts."""
    return [dict(c) for c in NEWS_METADATA_CONTRACTS]
