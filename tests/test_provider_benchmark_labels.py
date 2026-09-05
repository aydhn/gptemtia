import pytest
from advanced_provider_benchmark.provider_benchmark_labels import (
    list_benchmark_domain_labels,
    list_benchmark_metric_labels,
    list_benchmark_status_labels,
    list_provider_domain_labels,
    validate_benchmark_domain_label,
    validate_benchmark_metric_label,
    validate_benchmark_status_label,
    validate_provider_domain_label,
)


def test_provider_benchmark_labels():
    domains = list_benchmark_domain_labels()
    assert len(domains) >= 27
    assert "provider_benchmark_profile_domain" in domains
    assert "coverage_benchmark_domain" in domains
    assert "phase_116_handoff_domain" in domains

    metrics = list_benchmark_metric_labels()
    assert len(metrics) >= 10
    assert "metric_coverage" in metrics
    assert "metric_capability" in metrics
    assert "metric_quality" in metrics
    assert "metric_normalization" in metrics
    assert "metric_traceability" in metrics
    assert "metric_license_provenance" in metrics
    assert "metric_no_scraping_compliance" in metrics
    assert "metric_metadata_only_compliance" in metrics

    statuses = list_benchmark_status_labels()
    assert "benchmark_pass" in statuses
    assert "benchmark_fail" in statuses

    prov_domains = list_provider_domain_labels()
    assert "provider_domain_fx" in prov_domains
    assert "provider_domain_commodity" in prov_domains
    assert "provider_domain_macro" in prov_domains
    assert "provider_domain_calendar" in prov_domains
    assert "provider_domain_news_metadata" in prov_domains

    assert validate_benchmark_domain_label("coverage_benchmark_domain") is True
    assert validate_benchmark_metric_label("metric_quality") is True
    assert validate_benchmark_status_label("benchmark_pass") is True
    assert validate_provider_domain_label("provider_domain_fx") is True

    with pytest.raises(ValueError):
        validate_benchmark_domain_label("invalid_domain")

    with pytest.raises(ValueError):
        validate_benchmark_metric_label("invalid_metric")

    with pytest.raises(ValueError):
        validate_benchmark_status_label("invalid_status")

    with pytest.raises(ValueError):
        validate_provider_domain_label("invalid_provider_domain")
