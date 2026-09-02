class ConfigError(Exception): pass

DOMAIN_LABELS = [
    "performance_budget_domain", "runtime_profile_domain", "resource_footprint_domain",
    "cpu_estimate_domain", "memory_estimate_domain", "disk_estimate_domain",
    "growth_estimate_domain", "runtime_estimate_domain", "maintenance_cost_domain",
    "machine_suitability_domain", "efficiency_planning_domain", "retention_planning_domain",
    "quality_validation_domain", "unknown_performance_domain"
]

ESTIMATE_LABELS = [
    "cpu_estimate_low", "cpu_estimate_medium", "cpu_estimate_high",
    "memory_estimate_low", "memory_estimate_medium", "memory_estimate_high",
    "disk_estimate_low", "disk_estimate_medium", "disk_estimate_high",
    "runtime_estimate_low", "runtime_estimate_medium", "runtime_estimate_high",
    "estimate_unknown"
]

STATUS_LABELS = [
    "performance_ready_for_rehearsal", "performance_ready_with_warnings",
    "performance_missing", "performance_blocked_by_safety",
    "performance_needs_manual_review", "performance_unknown"
]

EFFICIENCY_CANDIDATE_LABELS = [
    "lightweight_mode_candidate", "output_reduction_candidate", "retention_policy_candidate",
    "report_rotation_candidate", "datalake_retention_candidate", "script_runtime_candidate",
    "test_runtime_candidate", "blocked_by_safety_candidate", "unknown_efficiency_candidate"
]

RISK_LABELS = [
    "performance_critical_risk", "performance_high_risk", "performance_medium_risk",
    "performance_low_risk", "performance_info", "performance_unknown_risk"
]

def list_performance_domain_labels() -> list[str]: return DOMAIN_LABELS
def list_performance_estimate_labels() -> list[str]: return ESTIMATE_LABELS
def list_performance_status_labels() -> list[str]: return STATUS_LABELS
def list_efficiency_candidate_labels() -> list[str]: return EFFICIENCY_CANDIDATE_LABELS
def list_performance_risk_labels() -> list[str]: return RISK_LABELS

def validate_performance_domain_label(label: str) -> None:
    if label not in DOMAIN_LABELS: raise ConfigError("Invalid domain label")
def validate_performance_estimate_label(label: str) -> None:
    if label not in ESTIMATE_LABELS: raise ConfigError("Invalid estimate label")
def validate_performance_status(label: str) -> None:
    if label not in STATUS_LABELS: raise ConfigError("Invalid status label")
def validate_efficiency_candidate_label(label: str) -> None:
    if label not in EFFICIENCY_CANDIDATE_LABELS: raise ConfigError("Invalid candidate label")
def validate_performance_risk(label: str) -> None:
    if label not in RISK_LABELS: raise ConfigError("Invalid risk label")
