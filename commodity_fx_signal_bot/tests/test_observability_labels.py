import pytest

from observability.observability_labels import (
    list_health_status_labels,
    list_component_labels,
    list_error_severity_labels,
    list_error_category_labels,
    validate_health_status,
    validate_component_label,
    validate_error_severity,
    validate_error_category,
    infer_health_status_from_score,
    is_critical_health_status
)

def test_lists_not_empty():
    assert len(list_health_status_labels()) > 0
    assert len(list_component_labels()) > 0
    assert len(list_error_severity_labels()) > 0
    assert len(list_error_category_labels()) > 0

def test_validate_health_status():
    validate_health_status("healthy")
    with pytest.raises(ValueError, match="Invalid health status"):
        validate_health_status("super_healthy")

def test_validate_component_label():
    validate_component_label("data_lake")
    with pytest.raises(ValueError, match="Invalid component"):
        validate_component_label("invalid_component_name")

def test_validate_error_severity():
    validate_error_severity("warning")
    with pytest.raises(ValueError, match="Invalid error severity"):
        validate_error_severity("mild")

def test_validate_error_category():
    validate_error_category("network_error")
    with pytest.raises(ValueError, match="Invalid error category"):
        validate_error_category("some_other_error")

def test_infer_health_status_from_score():
    assert infer_health_status_from_score(1.0) == "healthy"
    assert infer_health_status_from_score(0.95) == "healthy"
    assert infer_health_status_from_score(0.94) == "degraded"
    assert infer_health_status_from_score(0.70) == "degraded"
    assert infer_health_status_from_score(0.69) == "unhealthy"
    assert infer_health_status_from_score(0.40) == "unhealthy"
    assert infer_health_status_from_score(0.39) == "critical"
    assert infer_health_status_from_score(0.0) == "critical"

    with pytest.raises(ValueError):
        infer_health_status_from_score(-0.1)
    with pytest.raises(ValueError):
        infer_health_status_from_score(1.1)

def test_is_critical_health_status():
    assert is_critical_health_status("critical") == True
    assert is_critical_health_status("healthy") == False
    assert is_critical_health_status("degraded") == False
