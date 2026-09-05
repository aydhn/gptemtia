"""Atlas labels module."""

_ATLAS_DOMAIN_LABELS = [
    "meta_index_domain", "universal_navigation_domain", "cross_phase_lookup_domain",
    "semantic_toc_domain", "terminal_project_atlas_domain", "family_map_domain",
    "phase_map_domain", "route_map_domain", "glossary_domain", "crosswalk_domain",
    "quality_validation_domain", "unknown_atlas_domain"
]

_ATLAS_STATUS_LABELS = [
    "atlas_rehearsal_ready", "atlas_rehearsal_ready_with_warnings", "atlas_rehearsal_missing",
    "atlas_rehearsal_blocked_by_safety", "atlas_rehearsal_needs_manual_review", "atlas_rehearsal_unknown"
]

_LOOKUP_FAMILY_LABELS = [
    "lookup_docs", "lookup_scripts", "lookup_reports", "lookup_datalake",
    "lookup_generated_docs", "lookup_tests", "lookup_safety_boundary", "lookup_unknown"
]

_ATLAS_ROUTE_LABELS = [
    "route_operator", "route_analyst", "route_maintainer", "route_codex_agent",
    "route_future_reader", "route_unknown"
]

_ATLAS_RISK_LABELS = [
    "atlas_critical_risk", "atlas_high_risk", "atlas_medium_risk", "atlas_low_risk",
    "atlas_info", "atlas_unknown_risk"
]

def list_atlas_domain_labels() -> list[str]:
    return _ATLAS_DOMAIN_LABELS

def list_atlas_status_labels() -> list[str]:
    return _ATLAS_STATUS_LABELS

def list_lookup_family_labels() -> list[str]:
    return _LOOKUP_FAMILY_LABELS

def list_atlas_route_labels() -> list[str]:
    return _ATLAS_ROUTE_LABELS

def list_atlas_risk_labels() -> list[str]:
    return _ATLAS_RISK_LABELS

def validate_atlas_domain_label(label: str) -> None:
    if label not in _ATLAS_DOMAIN_LABELS:
        raise ValueError(f"Invalid atlas domain label: {label}")

def validate_atlas_status(label: str) -> None:
    if label not in _ATLAS_STATUS_LABELS:
        raise ValueError(f"Invalid atlas status label: {label}")

def validate_lookup_family(label: str) -> None:
    if label not in _LOOKUP_FAMILY_LABELS:
        raise ValueError(f"Invalid lookup family label: {label}")

def validate_atlas_route(label: str) -> None:
    if label not in _ATLAS_ROUTE_LABELS:
        raise ValueError(f"Invalid atlas route label: {label}")

def validate_atlas_risk(label: str) -> None:
    if label not in _ATLAS_RISK_LABELS:
        raise ValueError(f"Invalid atlas risk label: {label}")
