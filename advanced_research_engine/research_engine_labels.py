def list_research_engine_domain_labels():
    return [
        "research_engine_profile_domain", "research_engine_context_domain",
        "research_request_domain", "research_result_domain", "research_interface_domain",
        "data_access_interface_domain", "feature_interface_domain", "regime_interface_domain",
        "ml_interface_domain", "backtest_interface_domain", "portfolio_interface_domain",
        "report_interface_domain", "signal_research_interface_domain", "research_gateway_domain",
        "research_safety_domain", "research_quality_domain", "unknown_research_engine_domain"
    ]

def list_research_engine_status_labels():
    return [
        "research_engine_ready", "research_engine_ready_with_warnings", "research_engine_missing",
        "research_engine_blocked_by_safety", "research_engine_needs_manual_review", "research_engine_unknown"
    ]

def list_research_request_type_labels():
    return [
        "request_data_access", "request_feature_build", "request_regime_analysis",
        "request_ml_research", "request_backtest_research", "request_portfolio_research",
        "request_report_build", "request_signal_research", "request_full_research_dry_run"
    ]

def list_research_result_type_labels():
    return [
        "result_registry", "result_context", "result_dataframe", "result_report",
        "result_score", "result_validation", "result_quality", "result_error", "result_manual_review"
    ]

def list_research_engine_risk_labels():
    return [
        "research_engine_critical_risk", "research_engine_high_risk", "research_engine_medium_risk",
        "research_engine_low_risk", "research_engine_info", "research_engine_unknown_risk"
    ]

def validate_research_engine_domain_label(label: str): return label in list_research_engine_domain_labels()
def validate_research_engine_status(label: str): return label in list_research_engine_status_labels()
def validate_research_request_type(label: str): return label in list_research_request_type_labels()
def validate_research_result_type(label: str): return label in list_research_result_type_labels()
def validate_research_engine_risk_label(label: str): return label in list_research_engine_risk_labels()
