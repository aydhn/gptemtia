import pytest
from local_timeline.timeline_labels import (
    list_event_type_labels, list_timeline_source_labels, list_temporal_status_labels,
    list_change_impact_labels, list_timeline_query_intent_labels, validate_event_type,
    validate_timeline_source, validate_temporal_status, validate_change_impact, validate_timeline_query_intent
)

def test_lists_not_empty():
    assert len(list_event_type_labels()) > 0
    assert len(list_timeline_source_labels()) > 0
    assert len(list_temporal_status_labels()) > 0
    assert len(list_change_impact_labels()) > 0
    assert len(list_timeline_query_intent_labels()) > 0

def test_validate_event_type():
    validate_event_type("phase_event")
    with pytest.raises(ValueError):
        validate_event_type("invalid_event")

def test_validate_timeline_source():
    validate_timeline_source("data_lake_source")
    with pytest.raises(ValueError):
        validate_timeline_source("invalid_source")

def test_high_change_attention_not_live_alarm():
    labels = list_change_impact_labels()
    assert "high_change_attention" in labels
    assert "live_alarm" not in labels
