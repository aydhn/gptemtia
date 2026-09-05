
def list_commodity_domain_labels() -> list[str]:
    return [
        "commodity_provider_profile_domain", "commodity_provider_domain", "commodity_universe_domain",
        "commodity_category_domain", "commodity_metadata_domain", "commodity_symbol_normalization_domain",
        "commodity_spot_schema_domain", "commodity_ohlcv_schema_domain", "commodity_futures_contract_domain",
        "commodity_continuous_contract_domain", "commodity_roll_adjustment_domain", "commodity_provider_capability_domain",
        "commodity_provider_metadata_domain", "commodity_provider_request_domain", "commodity_provider_response_domain",
        "commodity_provider_error_domain", "commodity_provider_interface_domain", "commodity_adapter_contract_domain",
        "commodity_provider_registry_domain", "commodity_provider_resolver_domain", "commodity_provider_preference_domain",
        "commodity_provider_matcher_domain", "commodity_fixture_domain", "commodity_placeholder_domain",
        "commodity_output_validation_domain", "commodity_safety_domain", "commodity_health_domain",
        "commodity_quality_domain", "unknown_commodity_domain"
    ]

def list_commodity_category_labels() -> list[str]:
    return [
        "commodity_precious_metals", "commodity_energy", "commodity_industrial_metals",
        "commodity_agriculture", "commodity_livestock_placeholder", "commodity_softs", "commodity_unknown_category"
    ]

def list_commodity_data_type_labels() -> list[str]:
    return [
        "commodity_data_spot", "commodity_data_ohlcv", "commodity_data_futures_contract_metadata",
        "commodity_data_continuous_contract_placeholder", "commodity_data_symbol_metadata",
        "commodity_data_provider_metadata", "commodity_data_unknown"
    ]

def list_commodity_provider_status_labels() -> list[str]:
    return [
        "commodity_provider_ready", "commodity_provider_ready_with_warnings", "commodity_provider_placeholder_only",
        "commodity_provider_missing", "commodity_provider_blocked_by_no_scraping_boundary",
        "commodity_provider_needs_manual_review", "commodity_provider_unknown"
    ]

def list_commodity_risk_labels() -> list[str]:
    return [
        "commodity_provider_critical_risk", "commodity_provider_high_risk", "commodity_provider_medium_risk",
        "commodity_provider_low_risk", "commodity_provider_info", "commodity_provider_unknown_risk"
    ]

def validate_commodity_domain_label(label: str) -> bool: return label in list_commodity_domain_labels()
def validate_commodity_category_label(label: str) -> bool: return label in list_commodity_category_labels()
def validate_commodity_data_type_label(label: str) -> bool: return label in list_commodity_data_type_labels()
def validate_commodity_provider_status(label: str) -> bool: return label in list_commodity_provider_status_labels()
def validate_commodity_risk_label(label: str) -> bool: return label in list_commodity_risk_labels()
