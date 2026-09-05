import pandas as pd
from typing import Tuple, Dict, List
from advanced_news_metadata.news_provider_config import NewsProviderProfile
from advanced_news_metadata.news_provider_models import NewsItemReferenceField, build_news_item_reference_field_id

def build_default_news_item_reference_fields(profile: NewsProviderProfile) -> List[NewsItemReferenceField]:
    fields = [
        NewsItemReferenceField(
            field_id=build_news_item_reference_field_id("item_id"),
            field_name="item_id",
            field_type="string",
            description="Unique identifier for item reference.",
            required=True,
            no_full_text_policy="strictly_enforced_no_raw_text",
            manual_review_required=False
        ),
        NewsItemReferenceField(
            field_id=build_news_item_reference_field_id("source_name"),
            field_name="source_name",
            field_type="string",
            description="Originating publisher or agency name.",
            required=True,
            no_full_text_policy="strictly_enforced_no_raw_text",
            manual_review_required=False
        ),
        NewsItemReferenceField(
            field_id=build_news_item_reference_field_id("timestamp"),
            field_name="timestamp",
            field_type="datetime_iso8601",
            description="Publication timestamp.",
            required=True,
            no_full_text_policy="strictly_enforced_no_raw_text",
            manual_review_required=False
        ),
        NewsItemReferenceField(
            field_id=build_news_item_reference_field_id("title_or_summary_ref"),
            field_name="title_or_summary_ref",
            field_type="string",
            description="Short headline reference or pointer; never full article text.",
            required=True,
            no_full_text_policy="strictly_enforced_no_raw_text",
            manual_review_required=True
        ),
        NewsItemReferenceField(
            field_id=build_news_item_reference_field_id("canonical_reference"),
            field_name="canonical_reference",
            field_type="string",
            description="Canonical external URI or catalog citation; not raw article body.",
            required=False,
            no_full_text_policy="strictly_enforced_no_raw_text",
            manual_review_required=False
        ),
        NewsItemReferenceField(
            field_id=build_news_item_reference_field_id("content_hash_placeholder"),
            field_name="content_hash_placeholder",
            field_type="string",
            description="Cryptographic hash placeholder for deduplication verification in Phase 112.",
            required=False,
            no_full_text_policy="strictly_enforced_no_raw_text",
            manual_review_required=False
        ),
        NewsItemReferenceField(
            field_id=build_news_item_reference_field_id("provider_item_id_placeholder"),
            field_name="provider_item_id_placeholder",
            field_type="string",
            description="External provider unique reference ID placeholder.",
            required=False,
            no_full_text_policy="strictly_enforced_no_raw_text",
            manual_review_required=False
        ),
        NewsItemReferenceField(
            field_id=build_news_item_reference_field_id("license_note"),
            field_name="license_note",
            field_type="string",
            description="Legal licensing and attribution requirement note.",
            required=True,
            no_full_text_policy="strictly_enforced_no_raw_text",
            manual_review_required=True
        ),
        NewsItemReferenceField(
            field_id=build_news_item_reference_field_id("no_full_text_policy"),
            field_name="no_full_text_policy",
            field_type="string",
            description="Formal policy declaring that full text ingestion is disabled.",
            required=True,
            no_full_text_policy="strictly_enforced_no_raw_text",
            manual_review_required=False
        ),
        NewsItemReferenceField(
            field_id=build_news_item_reference_field_id("manual_review_required"),
            field_name="manual_review_required",
            field_type="boolean",
            description="Indicates whether this reference entry requires compliance verification.",
            required=True,
            no_full_text_policy="strictly_enforced_no_raw_text",
            manual_review_required=False
        )
    ]
    return fields

def build_news_item_reference_schema_contract(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_news_item_reference_fields(profile)
    df = pd.DataFrame([vars(i) for i in items])
    summary = summarize_news_item_reference_schema(df)
    return df, summary

def summarize_news_item_reference_schema(df: pd.DataFrame) -> Dict:
    return {
        "total_fields": len(df),
        "fields": df["field_name"].tolist() if not df.empty else []
    }
