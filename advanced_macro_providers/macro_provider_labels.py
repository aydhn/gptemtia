
def list_macro_domain_labels(): return ["macro_provider_profile_domain", "macro_provider_domain", "unknown_macro_domain"]
def list_macro_category_labels(): return ["macro_rates_and_yields", "macro_inflation", "macro_growth", "macro_labor", "macro_trade_balance", "macro_central_bank_policy", "macro_liquidity", "macro_risk_sentiment", "macro_yield_curve", "macro_currency_index", "macro_unknown_category"]
def list_macro_data_type_labels(): return ["macro_data_timeseries", "macro_data_release_metadata", "macro_data_revision_metadata", "macro_data_region_metadata", "macro_data_indicator_metadata", "macro_data_provider_metadata", "macro_data_unknown"]
def list_macro_provider_status_labels(): return ["macro_provider_ready", "macro_provider_ready_with_warnings", "macro_provider_placeholder_only", "macro_provider_missing", "macro_provider_blocked_by_no_scraping_boundary", "macro_provider_needs_manual_review", "macro_provider_unknown"]
def list_macro_risk_labels(): return ["macro_provider_critical_risk", "macro_provider_high_risk", "macro_provider_medium_risk", "macro_provider_low_risk", "macro_provider_info", "macro_provider_unknown_risk"]
def validate_macro_domain_label(label: str): pass
def validate_macro_category_label(label: str): pass
def validate_macro_data_type_label(label: str): pass
def validate_macro_provider_status(label: str): pass
def validate_macro_risk_label(label: str): pass
