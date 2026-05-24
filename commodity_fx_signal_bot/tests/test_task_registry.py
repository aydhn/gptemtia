from pathlib import Path
from research_planning.task_registry import ResearchTaskRegistry, deduplicate_tasks
from research_planning.planning_models import ResearchTask

def test_registry_add_load():
    registry = ResearchTaskRegistry(Path("/tmp/mock_registry"))
    task = ResearchTask("id", "type", "title", "desc", "planned", 0.0, "low", "none", [], [], [], "low", "low", [], "time", [])
    registry.add_task(task)

    df = registry.load_tasks()
    assert not df.empty
    assert len(df) == 1

    t = registry.get_task("id")
    assert t["title"] == "title"

    registry.update_task_status("id", "task_completed")
    t2 = registry.get_task("id")
    assert t2["status"] == "task_completed"

def test_deduplicate_tasks():
    task1 = ResearchTask("id1", "type", "title", "desc", "planned", 0.0, "low", "none", [], [], [], "low", "low", [], "time", [])
    task2 = ResearchTask("id1", "type", "title", "desc", "planned", 0.0, "low", "none", [], [], [], "low", "low", [], "time", [])

    deduped = deduplicate_tasks([task1, task2])
    assert len(deduped) == 1
    assert "Duplicate merged" in deduped[0].warnings
