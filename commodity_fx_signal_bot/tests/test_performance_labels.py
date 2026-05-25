import pytest
from performance.performance_labels import (
    list_performance_check_labels,
    list_resource_status_labels,
    list_cache_status_labels,
    list_optimization_labels,
    list_stability_labels,
    validate_performance_check_label,
    validate_resource_status_label,
    validate_cache_status_label,
    validate_optimization_label,
    validate_stability_label
)

def test_label_lists_not_empty():
    assert len(list_performance_check_labels()) > 0
    assert len(list_resource_status_labels()) > 0
    assert len(list_cache_status_labels()) > 0
    assert len(list_optimization_labels()) > 0
    assert len(list_stability_labels()) > 0

def test_validate_performance_check_label():
    validate_performance_check_label("runtime_profile_check")
    with pytest.raises(ValueError):
        validate_performance_check_label("invalid_label")

def test_validate_resource_status_label():
    validate_resource_status_label("within_budget")
    with pytest.raises(ValueError):
        validate_resource_status_label("invalid_label")

def test_stability_label_meaning():
    # stable_large_run is in the list but shouldn't be interpreted as production readiness
    # This is a conceptual test verified by code review and documentation later
    assert "stable_large_run" in list_stability_labels()
