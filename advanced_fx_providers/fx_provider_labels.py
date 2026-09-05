def list_fx_domain_labels() -> list[str]:
    return [
        "fx_provider_profile_domain", "fx_provider_domain", "fx_pair_universe_domain",
        "fx_currency_metadata_domain", "fx_symbol_normalization_domain", "fx_quote_schema_domain",
        "fx_ohlcv_schema_domain", "fx_cross_rate_domain", "fx_provider_capability_domain",
        "fx_provider_metadata_domain", "fx_provider_request_domain", "fx_provider_response_domain",
        "fx_provider_error_domain", "fx_provider_interface_domain", "fx_adapter_contract_domain",
        "fx_provider_registry_domain", "fx_provider_resolver_domain", "fx_provider_preference_domain",
        "fx_provider_matcher_domain", "fx_fixture_domain", "fx_placeholder_domain",
        "fx_output_validation_domain", "fx_safety_domain", "fx_health_domain",
        "fx_quality_domain", "unknown_fx_domain"
    ]

def list_fx_pair_group_labels() -> list[str]:
    return ["fx_major_pair", "fx_minor_pair", "fx_exotic_pair", "fx_cross_pair", "fx_custom_pair", "fx_unknown_pair_group"]

def list_fx_data_type_labels() -> list[str]:
    return ["fx_data_ohlcv", "fx_data_quote", "fx_data_spot_rate", "fx_data_forward_placeholder", "fx_data_symbol_metadata", "fx_data_provider_metadata", "fx_data_unknown"]

def list_fx_provider_status_labels() -> list[str]:
    return ["fx_provider_ready", "fx_provider_ready_with_warnings", "fx_provider_placeholder_only", "fx_provider_missing", "fx_provider_blocked_by_no_scraping_boundary", "fx_provider_needs_manual_review", "fx_provider_unknown"]

def list_fx_risk_labels() -> list[str]:
    return ["fx_provider_critical_risk", "fx_provider_high_risk", "fx_provider_medium_risk", "fx_provider_low_risk", "fx_provider_info", "fx_provider_unknown_risk"]

def validate_fx_domain_label(label: str) -> bool:
    return label in list_fx_domain_labels()

def validate_fx_pair_group_label(label: str) -> bool:
    return label in list_fx_pair_group_labels()

def validate_fx_data_type_label(label: str) -> bool:
    return label in list_fx_data_type_labels()

def validate_fx_provider_status(label: str) -> bool:
    return label in list_fx_provider_status_labels()

def validate_fx_risk_label(label: str) -> bool:
    return label in list_fx_risk_labels()
