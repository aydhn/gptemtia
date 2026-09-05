def list_calendar_domain_labels():
    return [
        "calendar_provider_profile_domain",
        "calendar_provider_domain",
        "economic_event_universe_domain",
        "economic_event_category_domain",
        "economic_event_importance_domain",
        "event_indicator_mapping_domain",
        "calendar_event_schema_domain",
        "release_event_schema_domain",
        "event_surprise_requirement_domain",
        "event_time_normalization_domain",
        "event_revision_handling_domain",
        "calendar_provider_capability_domain",
        "calendar_provider_metadata_domain",
        "calendar_provider_request_domain",
        "calendar_provider_response_domain",
        "calendar_provider_error_domain",
        "calendar_provider_interface_domain",
        "calendar_adapter_contract_domain",
        "calendar_provider_registry_domain",
        "calendar_provider_resolver_domain",
        "calendar_provider_preference_domain",
        "calendar_provider_matcher_domain",
        "calendar_fixture_domain",
        "calendar_placeholder_domain",
        "calendar_output_validation_domain",
        "calendar_safety_domain",
        "calendar_health_domain",
        "calendar_quality_domain",
        "unknown_calendar_domain"
    ]

def list_event_category_labels():
    return [
        "event_central_bank_policy",
        "event_inflation",
        "event_labor",
        "event_growth",
        "event_pmi_sentiment",
        "event_trade_balance",
        "event_energy_inventory",
        "event_bond_auction_placeholder",
        "event_speech_placeholder",
        "event_unknown_category"
    ]

def list_event_importance_labels():
    return [
        "event_importance_high",
        "event_importance_medium",
        "event_importance_low",
        "event_importance_info",
        "event_importance_unknown"
    ]

def list_calendar_data_type_labels():
    return [
        "calendar_data_event_schedule",
        "calendar_data_release_event",
        "calendar_data_event_metadata",
        "calendar_data_revision_metadata",
        "calendar_data_provider_metadata",
        "calendar_data_unknown"
    ]

def list_calendar_provider_status_labels():
    return [
        "calendar_provider_ready",
        "calendar_provider_ready_with_warnings",
        "calendar_provider_placeholder_only",
        "calendar_provider_missing",
        "calendar_provider_blocked_by_no_scraping_boundary",
        "calendar_provider_needs_manual_review",
        "calendar_provider_unknown"
    ]

def list_calendar_risk_labels():
    return [
        "calendar_provider_critical_risk",
        "calendar_provider_high_risk",
        "calendar_provider_medium_risk",
        "calendar_provider_low_risk",
        "calendar_provider_info",
        "calendar_provider_unknown_risk"
    ]

def validate_calendar_domain_label(label: str):
    if label not in list_calendar_domain_labels():
        raise ValueError(f"Invalid domain label: {label}")

def validate_event_category_label(label: str):
    if label not in list_event_category_labels():
        raise ValueError(f"Invalid event category label: {label}")

def validate_event_importance_label(label: str):
    if label not in list_event_importance_labels():
        raise ValueError(f"Invalid event importance label: {label}")

def validate_calendar_data_type_label(label: str):
    if label not in list_calendar_data_type_labels():
        raise ValueError(f"Invalid calendar data type label: {label}")

def validate_calendar_provider_status(label: str):
    if label not in list_calendar_provider_status_labels():
        raise ValueError(f"Invalid calendar provider status: {label}")

def validate_calendar_risk_label(label: str):
    if label not in list_calendar_risk_labels():
        raise ValueError(f"Invalid calendar risk label: {label}")
