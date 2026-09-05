import pandas as pd
from typing import Tuple, Dict, List
from advanced_news_metadata.news_provider_config import NewsProviderProfile
from advanced_news_metadata.news_provider_models import NewsMetadataSchemaField, build_news_schema_field_id

def build_default_news_metadata_schema_fields(profile: NewsProviderProfile) -> List[NewsMetadataSchemaField]:
    fields = [
        NewsMetadataSchemaField(
            field_id=build_news_schema_field_id("item_id"),
            field_name="item_id",
            field_type="string",
            description="Unique identifier for the news metadata item.",
            required=True,
            privacy_copyright_note="Synthetic or provider-supplied identifier; no personal or copyrighted payload.",
            manual_review_required=False
        ),
        NewsMetadataSchemaField(
            field_id=build_news_schema_field_id("timestamp"),
            field_name="timestamp",
            field_type="datetime_iso8601",
            description="UTC timestamp of news publication or release.",
            required=True,
            privacy_copyright_note="Temporal metadata only.",
            manual_review_required=False
        ),
        NewsMetadataSchemaField(
            field_id=build_news_schema_field_id("source_name"),
            field_name="source_name",
            field_type="string",
            description="Originating agency, central bank, or publisher name.",
            required=True,
            privacy_copyright_note="Entity name attribution only.",
            manual_review_required=False
        ),
        NewsMetadataSchemaField(
            field_id=build_news_schema_field_id("source_category"),
            field_name="source_category",
            field_type="string",
            description="Category label of the news source from news_source_categories.",
            required=True,
            privacy_copyright_note="Categorical taxonomy label.",
            manual_review_required=False
        ),
        NewsMetadataSchemaField(
            field_id=build_news_schema_field_id("title_or_summary_ref"),
            field_name="title_or_summary_ref",
            field_type="string",
            description="Short headline reference or abstract pointer; strictly NOT full article text.",
            required=True,
            privacy_copyright_note="Restricted to short public title reference or pointer; copyrighted full text forbidden.",
            manual_review_required=True
        ),
        NewsMetadataSchemaField(
            field_id=build_news_schema_field_id("url_or_source_ref"),
            field_name="url_or_source_ref",
            field_type="string",
            description="Canonical external reference URI or archive identifier.",
            required=False,
            privacy_copyright_note="Pointer reference only; automated fetching/scraping prohibited.",
            manual_review_required=False
        ),
        NewsMetadataSchemaField(
            field_id=build_news_schema_field_id("region_tags"),
            field_name="region_tags",
            field_type="list[string]",
            description="Geographic/jurisdiction tags (e.g., US, EU, TR, GLOBAL).",
            required=False,
            privacy_copyright_note="Standard region taxonomy tags.",
            manual_review_required=False
        ),
        NewsMetadataSchemaField(
            field_id=build_news_schema_field_id("currency_tags"),
            field_name="currency_tags",
            field_type="list[string]",
            description="Affected currency codes (e.g., USD, EUR, TRY).",
            required=False,
            privacy_copyright_note="ISO currency codes.",
            manual_review_required=False
        ),
        NewsMetadataSchemaField(
            field_id=build_news_schema_field_id("asset_tags"),
            field_name="asset_tags",
            field_type="list[string]",
            description="Asset class tags (FX, COMMODITIES, MACRO, RISK_SENTIMENT).",
            required=False,
            privacy_copyright_note="Taxonomy classification tags.",
            manual_review_required=False
        ),
        NewsMetadataSchemaField(
            field_id=build_news_schema_field_id("macro_tags"),
            field_name="macro_tags",
            field_type="list[string]",
            description="Macroeconomic factor tags (CENTRAL_BANK, INFLATION, LABOR).",
            required=False,
            privacy_copyright_note="Macro domain taxonomy tags.",
            manual_review_required=False
        ),
        NewsMetadataSchemaField(
            field_id=build_news_schema_field_id("commodity_tags"),
            field_name="commodity_tags",
            field_type="list[string]",
            description="Commodity tags (GOLD, CRUDE_OIL, NATURAL_GAS, COPPER).",
            required=False,
            privacy_copyright_note="Commodity taxonomy tags.",
            manual_review_required=False
        ),
        NewsMetadataSchemaField(
            field_id=build_news_schema_field_id("fx_tags"),
            field_name="fx_tags",
            field_type="list[string]",
            description="Foreign exchange tags (USD, EUR, TRY, DXY).",
            required=False,
            privacy_copyright_note="FX taxonomy tags.",
            manual_review_required=False
        ),
        NewsMetadataSchemaField(
            field_id=build_news_schema_field_id("topic_tags"),
            field_name="topic_tags",
            field_type="list[string]",
            description="Detailed topic labels from news_topic_taxonomy.",
            required=False,
            privacy_copyright_note="Topic categorization labels.",
            manual_review_required=False
        ),
        NewsMetadataSchemaField(
            field_id=build_news_schema_field_id("linked_calendar_event"),
            field_name="linked_calendar_event",
            field_type="string",
            description="Associated Phase 110 economic calendar event ID or canonical name.",
            required=False,
            privacy_copyright_note="Linkage reference only; not a price signal.",
            manual_review_required=True
        ),
        NewsMetadataSchemaField(
            field_id=build_news_schema_field_id("linked_macro_indicator"),
            field_name="linked_macro_indicator",
            field_type="string",
            description="Associated Phase 109 macro provider indicator series ID.",
            required=False,
            privacy_copyright_note="Cross-layer linkage reference.",
            manual_review_required=True
        ),
        NewsMetadataSchemaField(
            field_id=build_news_schema_field_id("provider_name"),
            field_name="provider_name",
            field_type="string",
            description="Name of the metadata provider adapter supplying this record.",
            required=True,
            privacy_copyright_note="Provider identification metadata.",
            manual_review_required=False
        ),
        NewsMetadataSchemaField(
            field_id=build_news_schema_field_id("retrieval_mode"),
            field_name="retrieval_mode",
            field_type="string",
            description="Access mode (dry_run, manual_file, local_cache, placeholder).",
            required=True,
            privacy_copyright_note="System operational mode.",
            manual_review_required=False
        ),
        NewsMetadataSchemaField(
            field_id=build_news_schema_field_id("metadata_only"),
            field_name="metadata_only",
            field_type="boolean",
            description="Affirms that the item contains only metadata and no raw text payload.",
            required=True,
            privacy_copyright_note="Strict invariant: must be True.",
            manual_review_required=False
        ),
        NewsMetadataSchemaField(
            field_id=build_news_schema_field_id("copyright_status"),
            field_name="copyright_status",
            field_type="string",
            description="Copyright compliance classification (public_domain, safe_metadata_ref, licensed_placeholder).",
            required=True,
            privacy_copyright_note="Compliance metadata tracking.",
            manual_review_required=True
        ),
        NewsMetadataSchemaField(
            field_id=build_news_schema_field_id("data_quality_status"),
            field_name="data_quality_status",
            field_type="string",
            description="Preliminary data quality status for handoff to Phase 112.",
            required=True,
            privacy_copyright_note="Quality tracking label.",
            manual_review_required=False
        ),
        NewsMetadataSchemaField(
            field_id=build_news_schema_field_id("manual_review_required"),
            field_name="manual_review_required",
            field_type="boolean",
            description="Flag indicating whether human analyst review is required.",
            required=True,
            privacy_copyright_note="Governance requirement.",
            manual_review_required=False
        )
    ]
    return fields

def build_news_metadata_schema_contract(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_news_metadata_schema_fields(profile)
    df = pd.DataFrame([vars(i) for i in items])
    summary = summarize_news_metadata_schema(df)
    return df, summary

def summarize_news_metadata_schema(df: pd.DataFrame) -> Dict:
    return {
        "total_fields": len(df),
        "fields": df["field_name"].tolist() if not df.empty else [],
        "required_fields": df[df["required"]]["field_name"].tolist() if not df.empty else []
    }
