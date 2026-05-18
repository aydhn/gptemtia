import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from orchestration.scheduler_stub import list_schedule_definitions, validate_schedule_definition

def test_scheduler_stub():
    schedules = list_schedule_definitions(enabled_only=False)
    assert len(schedules) > 0

    enabled = list_schedule_definitions(enabled_only=True)
    assert len(enabled) == 0

    val = validate_schedule_definition(schedules[0])
    assert val["valid"]
