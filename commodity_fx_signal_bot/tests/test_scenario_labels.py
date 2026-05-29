import pytest
from scenarios.scenario_labels import (
    list_scenario_type_labels, list_scenario_status_labels,
    list_scenario_safety_labels, list_case_study_labels,
    validate_scenario_type, validate_scenario_safety, ScenarioLabelError
)

def test_scenario_labels_lists_not_empty():
    assert len(list_scenario_type_labels()) > 0
    assert len(list_scenario_status_labels()) > 0
    assert len(list_scenario_safety_labels()) > 0
    assert len(list_case_study_labels()) > 0

def test_validate_scenario_type():
    validate_scenario_type("symbol_research_scenario")
    with pytest.raises(ScenarioLabelError):
        validate_scenario_type("invalid_type")

def test_validate_scenario_safety():
    validate_scenario_safety("synthetic_offline_only")
    with pytest.raises(ScenarioLabelError):
        validate_scenario_safety("invalid_safety")

def test_scenario_validated_not_live():
    # Just a conceptual check, scenario_validated shouldn't be named live
    assert "scenario_validated" in list_scenario_status_labels()
    assert "live_approved" not in list_scenario_status_labels()
