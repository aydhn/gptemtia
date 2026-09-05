from typing import List


BENCHMARK_DOMAIN_LABELS: List[str] = [
    "provider_benchmark_profile_domain",
    "provider_benchmark_domain",
    "benchmark_metric_domain",
    "benchmark_weight_domain",
    "coverage_benchmark_domain",
    "capability_benchmark_domain",
    "quality_benchmark_domain",
    "normalization_benchmark_domain",
    "traceability_benchmark_domain",
    "license_provenance_benchmark_domain",
    "no_scraping_compliance_domain",
    "metadata_only_compliance_domain",
    "manual_review_benchmark_domain",
    "fx_provider_benchmark_domain",
    "commodity_provider_benchmark_domain",
    "macro_provider_benchmark_domain",
    "calendar_provider_benchmark_domain",
    "news_metadata_provider_benchmark_domain",
    "cross_domain_provider_benchmark_domain",
    "benchmark_scoring_domain",
    "provider_ranking_research_domain",
    "benchmark_finding_domain",
    "benchmark_manual_review_domain",
    "benchmark_health_domain",
    "benchmark_validation_domain",
    "benchmark_safety_domain",
    "phase_116_handoff_domain",
    "unknown_benchmark_domain",
]

BENCHMARK_METRIC_LABELS: List[str] = [
    "metric_coverage",
    "metric_capability",
    "metric_quality",
    "metric_normalization",
    "metric_traceability",
    "metric_license_provenance",
    "metric_no_scraping_compliance",
    "metric_metadata_only_compliance",
    "metric_manual_review_load",
    "metric_cross_domain_consistency",
    "metric_unknown",
]

BENCHMARK_STATUS_LABELS: List[str] = [
    "benchmark_pass",
    "benchmark_pass_with_warnings",
    "benchmark_partial",
    "benchmark_fail",
    "benchmark_manual_review_required",
    "benchmark_placeholder_only",
    "benchmark_unknown",
]

PROVIDER_DOMAIN_LABELS: List[str] = [
    "provider_domain_fx",
    "provider_domain_commodity",
    "provider_domain_macro",
    "provider_domain_calendar",
    "provider_domain_news_metadata",
    "provider_domain_cross_domain",
    "provider_domain_unknown",
]


def list_benchmark_domain_labels() -> List[str]:
    return list(BENCHMARK_DOMAIN_LABELS)


def list_benchmark_metric_labels() -> List[str]:
    return list(BENCHMARK_METRIC_LABELS)


def list_benchmark_status_labels() -> List[str]:
    return list(BENCHMARK_STATUS_LABELS)


def list_provider_domain_labels() -> List[str]:
    return list(PROVIDER_DOMAIN_LABELS)


def validate_benchmark_domain_label(label: str) -> bool:
    if label not in BENCHMARK_DOMAIN_LABELS:
        raise ValueError(f"Invalid benchmark domain label: '{label}'. Must be one of {BENCHMARK_DOMAIN_LABELS}")
    return True


def validate_benchmark_metric_label(label: str) -> bool:
    if label not in BENCHMARK_METRIC_LABELS:
        raise ValueError(f"Invalid benchmark metric label: '{label}'. Must be one of {BENCHMARK_METRIC_LABELS}")
    return True


def validate_benchmark_status_label(label: str) -> bool:
    if label not in BENCHMARK_STATUS_LABELS:
        raise ValueError(f"Invalid benchmark status label: '{label}'. Must be one of {BENCHMARK_STATUS_LABELS}")
    return True


def validate_provider_domain_label(label: str) -> bool:
    if label not in PROVIDER_DOMAIN_LABELS:
        raise ValueError(f"Invalid provider domain label: '{label}'. Must be one of {PROVIDER_DOMAIN_LABELS}")
    return True
