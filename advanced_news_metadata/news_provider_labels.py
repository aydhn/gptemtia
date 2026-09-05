def list_news_domain_labels():
    return [
        "news_provider_profile_domain",
        "news_metadata_domain",
        "news_source_domain",
        "news_source_category_domain",
        "news_metadata_schema_domain",
        "news_item_reference_domain",
        "news_asset_tag_domain",
        "news_macro_tag_domain",
        "news_commodity_tag_domain",
        "news_fx_tag_domain",
        "news_event_linkage_domain",
        "news_region_currency_mapping_domain",
        "news_topic_taxonomy_domain",
        "news_sentiment_requirement_domain",
        "news_impact_requirement_domain",
        "news_freshness_requirement_domain",
        "news_deduplication_requirement_domain",
        "news_provider_capability_domain",
        "news_provider_metadata_domain",
        "news_provider_request_domain",
        "news_provider_response_domain",
        "news_provider_error_domain",
        "news_provider_interface_domain",
        "news_adapter_contract_domain",
        "news_provider_registry_domain",
        "news_provider_resolver_domain",
        "news_provider_preference_domain",
        "news_provider_matcher_domain",
        "news_fixture_domain",
        "news_placeholder_domain",
        "news_output_validation_domain",
        "news_safety_domain",
        "news_health_domain",
        "news_quality_domain",
        "unknown_news_domain"
    ]

def list_news_source_category_labels():
    return [
        "news_source_official_statement",
        "news_source_central_bank",
        "news_source_government_agency",
        "news_source_exchange_notice",
        "news_source_energy_agency",
        "news_source_general_financial_news_placeholder",
        "news_source_licensed_newswire_placeholder",
        "news_source_public_dataset_placeholder",
        "news_source_manual_research_note",
        "news_source_unknown_category"
    ]

def list_news_topic_labels():
    return [
        "news_topic_central_bank",
        "news_topic_inflation",
        "news_topic_growth",
        "news_topic_labor",
        "news_topic_geopolitics",
        "news_topic_energy",
        "news_topic_metals",
        "news_topic_fx",
        "news_topic_risk_sentiment",
        "news_topic_liquidity",
        "news_topic_earnings_placeholder",
        "news_topic_unknown"
    ]

def list_news_data_type_labels():
    return [
        "news_data_metadata",
        "news_data_item_reference",
        "news_data_source_metadata",
        "news_data_topic_tags",
        "news_data_asset_tags",
        "news_data_event_linkage",
        "news_data_provider_metadata",
        "news_data_unknown"
    ]

def list_news_provider_status_labels():
    return [
        "news_provider_ready",
        "news_provider_ready_with_warnings",
        "news_provider_placeholder_only",
        "news_provider_missing",
        "news_provider_blocked_by_no_scraping_boundary",
        "news_provider_blocked_by_copyright_boundary",
        "news_provider_needs_manual_review",
        "news_provider_unknown"
    ]

def list_news_risk_labels():
    return [
        "news_provider_critical_risk",
        "news_provider_high_risk",
        "news_provider_medium_risk",
        "news_provider_low_risk",
        "news_provider_info",
        "news_provider_unknown_risk"
    ]

NEWS_DOMAINS = list_news_domain_labels()
NEWS_SOURCE_CATEGORIES = list_news_source_category_labels()
NEWS_TOPICS = list_news_topic_labels()
NEWS_DATA_TYPES = list_news_data_type_labels()
NEWS_PROVIDER_STATUS = list_news_provider_status_labels()
NEWS_RISK_LABELS = list_news_risk_labels()

def validate_news_domain_label(label: str) -> bool:
    return label in NEWS_DOMAINS

def validate_news_source_category_label(label: str) -> bool:
    return label in NEWS_SOURCE_CATEGORIES

def validate_news_topic_label(label: str) -> bool:
    return label in NEWS_TOPICS

def validate_news_data_type_label(label: str) -> bool:
    return label in NEWS_DATA_TYPES

def validate_news_provider_status_label(label: str) -> bool:
    return label in NEWS_PROVIDER_STATUS

def validate_news_provider_status(label: str) -> bool:
    return validate_news_provider_status_label(label)

def validate_news_risk_label(label: str) -> bool:
    return label in NEWS_RISK_LABELS
