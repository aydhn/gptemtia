import pytest
from local_timeline.timeline_models import (
    ProjectEvent, PhaseChronologyItem, ArtifactEvolutionRecord, TimelineQuery, TimelineQueryResult,
    build_project_event_id, build_artifact_evolution_id, build_timeline_query_id, project_event_to_dict
)

def test_build_project_event_id_deterministic():
    id1 = build_project_event_id("type", "path", "time", "title")
    id2 = build_project_event_id("type", "path", "time", "title")
    assert id1 == id2
    assert id1.startswith("evt_")

def test_build_artifact_evolution_id_deterministic():
    id1 = build_artifact_evolution_id("path")
    id2 = build_artifact_evolution_id("path")
    assert id1 == id2
    assert id1.startswith("art_")

def test_build_timeline_query_id_deterministic():
    id1 = build_timeline_query_id("query")
    id2 = build_timeline_query_id("query")
    assert id1 == id2
    assert id1.startswith("qry_")

def test_dataclass_to_dict():
    evt = ProjectEvent("id", "type", "time", "src", "mod", "path", "title", "sum", 1, "imp", {}, [])
    d = project_event_to_dict(evt)
    assert d["event_id"] == "id"
    assert "trade" not in str(type(evt)).lower()
