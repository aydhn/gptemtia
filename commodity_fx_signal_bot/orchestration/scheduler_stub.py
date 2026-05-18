"""
Stub for future background scheduler implementation.
"""

from dataclasses import dataclass, asdict
from typing import List

@dataclass
class ScheduleDefinition:
    schedule_id: str
    workflow_name: str
    profile_name: str
    timeframe: str
    cron_like: str
    enabled: bool
    dry_run: bool
    notes: str = ""

_DEFAULT_SCHEDULES = [
    ScheduleDefinition(
        schedule_id="daily_research_morning",
        workflow_name="daily_research_workflow",
        profile_name="balanced_research_orchestration",
        timeframe="1d",
        cron_like="09:00",
        enabled=False,
        dry_run=True,
        notes="Daily research run in the morning (inactive)"
    ),
    ScheduleDefinition(
        schedule_id="paper_reporting_evening",
        workflow_name="paper_reporting_workflow",
        profile_name="paper_reporting_orchestration",
        timeframe="1d",
        cron_like="18:00",
        enabled=False,
        dry_run=True,
        notes="Evening paper trading report (inactive)"
    ),
    ScheduleDefinition(
        schedule_id="healthcheck_morning",
        workflow_name="healthcheck_workflow",
        profile_name="minimal_healthcheck_orchestration",
        timeframe="1d",
        cron_like="08:00",
        enabled=False,
        dry_run=True,
        notes="Morning system health check (inactive)"
    )
]

def build_default_schedule_definitions() -> List[ScheduleDefinition]:
    return list(_DEFAULT_SCHEDULES)

def validate_schedule_definition(schedule: ScheduleDefinition) -> dict:
    valid = True
    errors = []

    if not schedule.schedule_id:
         valid = False
         errors.append("Missing schedule_id")
    if not schedule.workflow_name:
         valid = False
         errors.append("Missing workflow_name")
    if not schedule.cron_like:
         valid = False
         errors.append("Missing cron_like string")

    return {
         "valid": valid,
         "errors": errors
    }

def schedule_definition_to_dict(schedule: ScheduleDefinition) -> dict:
    return asdict(schedule)

def list_schedule_definitions(enabled_only: bool = True) -> List[ScheduleDefinition]:
    if enabled_only:
        return [s for s in _DEFAULT_SCHEDULES if s.enabled]
    return list(_DEFAULT_SCHEDULES)
