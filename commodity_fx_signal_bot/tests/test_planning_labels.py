import pytest
from research_planning.planning_labels import (
    list_research_task_type_labels,
    list_research_priority_labels,
    list_task_status_labels,
    list_planning_recommendation_labels,
    validate_research_task_type,
    validate_research_priority,
    validate_task_status,
    validate_planning_recommendation
)

def test_label_lists_not_empty():
    assert len(list_research_task_type_labels()) > 0
    assert len(list_research_priority_labels()) > 0
    assert len(list_task_status_labels()) > 0
    assert len(list_planning_recommendation_labels()) > 0

def test_validate_research_task_type():
    validate_research_task_type("data_quality_task") # Should not raise
    with pytest.raises(ValueError):
        validate_research_task_type("invalid_task_type")

def test_validate_research_priority():
    validate_research_priority("high_research_priority") # Should not raise
    with pytest.raises(ValueError):
        validate_research_priority("live_priority")
