RUNTIME_DOMAIN_LABELS = [
    "runtime_profile_domain", "runtime_context_domain", "runtime_capability_domain",
    "runtime_module_domain", "runtime_dependency_domain", "runtime_execution_contract_domain",
    "runtime_command_contract_domain", "runtime_output_contract_domain",
    "runtime_datalake_contract_domain", "runtime_featurestore_contract_domain",
    "runtime_report_contract_domain", "runtime_safety_domain", "runtime_health_domain",
    "runtime_quality_domain", "unknown_runtime_domain"
]

RUNTIME_STATUS_LABELS = [
    "runtime_ready", "runtime_ready_with_warnings", "runtime_missing",
    "runtime_blocked_by_safety", "runtime_needs_manual_review", "runtime_unknown"
]

RUNTIME_CAPABILITY_LABELS = [
    "capability_settings", "capability_paths", "capability_datalake",
    "capability_featurestore", "capability_reporting", "capability_scripts",
    "capability_tests", "capability_docs", "capability_advanced_continuation",
    "capability_provider_future", "capability_feature_future", "capability_regime_future",
    "capability_ml_gpu_future", "capability_backtest_future", "capability_portfolio_future",
    "capability_final_integration_future"
]

RUNTIME_RISK_LABELS = [
    "runtime_critical_risk", "runtime_high_risk", "runtime_medium_risk",
    "runtime_low_risk", "runtime_info", "runtime_unknown_risk"
]

def list_runtime_domain_labels(): return RUNTIME_DOMAIN_LABELS
def list_runtime_status_labels(): return RUNTIME_STATUS_LABELS
def list_runtime_capability_labels(): return RUNTIME_CAPABILITY_LABELS
def list_runtime_risk_labels(): return RUNTIME_RISK_LABELS

def validate_runtime_domain_label(label: str): return label in RUNTIME_DOMAIN_LABELS
def validate_runtime_status(label: str): return label in RUNTIME_STATUS_LABELS
def validate_runtime_capability_label(label: str): return label in RUNTIME_CAPABILITY_LABELS
def validate_runtime_risk_label(label: str): return label in RUNTIME_RISK_LABELS
