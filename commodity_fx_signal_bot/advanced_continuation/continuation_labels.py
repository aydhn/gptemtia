_DOMAIN_LABELS = [
    "advanced_roadmap_domain", "phase_master_plan_domain", "post_mvp_reopen_domain",
    "phase_output_audit_domain", "mvp_gap_register_domain", "functional_continuation_domain",
    "dependency_map_domain", "milestone_map_domain", "development_risk_domain",
    "continuation_quality_domain", "unknown_continuation_domain"
]

_STATUS_LABELS = [
    "continuation_ready", "continuation_ready_with_warnings", "continuation_missing",
    "continuation_blocked_by_safety", "continuation_needs_manual_review", "continuation_unknown"
]

_TRACK_LABELS = [
    "track_data_providers", "track_feature_engine", "track_regime_engine",
    "track_ml_gpu", "track_backtest_benchmark", "track_portfolio_risk",
    "track_final_integration", "track_governance_safety"
]

_RISK_LABELS = [
    "continuation_critical_risk", "continuation_high_risk", "continuation_medium_risk",
    "continuation_low_risk", "continuation_info", "continuation_unknown_risk"
]

def list_continuation_domain_labels() -> list[str]:
    return _DOMAIN_LABELS.copy()

def list_continuation_status_labels() -> list[str]:
    return _STATUS_LABELS.copy()

def list_advanced_track_labels() -> list[str]:
    return _TRACK_LABELS.copy()

def list_continuation_risk_labels() -> list[str]:
    return _RISK_LABELS.copy()

def validate_continuation_domain_label(label: str) -> bool:
    return label in _DOMAIN_LABELS

def validate_continuation_status(label: str) -> bool:
    return label in _STATUS_LABELS

def validate_advanced_track_label(label: str) -> bool:
    return label in _TRACK_LABELS

def validate_continuation_risk_label(label: str) -> bool:
    return label in _RISK_LABELS
