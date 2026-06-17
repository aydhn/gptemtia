"""
Data models for Local Timeline Engine.
"""

from dataclasses import dataclass, asdict
import hashlib

@dataclass
class ProjectEvent:
    event_id: str
    event_type: str
    event_time_utc: str | None
    source_label: str
    module_name: str | None
    relative_path: str | None
    title: str
    summary: str
    phase_number: int | None
    change_impact: str
    metadata: dict
    warnings: list[str]

@dataclass
class PhaseChronologyItem:
    phase_number: int
    phase_title: str
    first_seen_utc: str | None
    last_seen_utc: str | None
    related_modules: list[str]
    related_artifacts: list[str]
    event_count: int
    status: str
    warnings: list[str]

@dataclass
class ArtifactEvolutionRecord:
    artifact_id: str
    relative_path: str
    module_name: str | None
    first_seen_utc: str | None
    last_modified_utc: str | None
    event_count: int
    event_types: list[str]
    temporal_status: str
    change_impact: str
    warnings: list[str]

@dataclass
class TimelineQuery:
    query_id: str
    query_text: str
    query_intent: str
    filters: dict
    warnings: list[str]

@dataclass
class TimelineQueryResult:
    result_id: str
    query_id: str
    event_id: str | None
    artifact_id: str | None
    rank: int
    score: float
    explanation: str
    warnings: list[str]


def build_project_event_id(event_type: str, relative_path: str | None, event_time_utc: str | None, title: str) -> str:
    raw = f"{event_type}_{relative_path}_{event_time_utc}_{title}"
    return f"evt_{hashlib.sha256(raw.encode('utf-8')).hexdigest()[:16]}"

def build_artifact_evolution_id(relative_path: str) -> str:
    raw = f"art_{relative_path}"
    return f"art_{hashlib.sha256(raw.encode('utf-8')).hexdigest()[:16]}"

def build_timeline_query_id(query_text: str) -> str:
    raw = f"qry_{query_text}"
    return f"qry_{hashlib.sha256(raw.encode('utf-8')).hexdigest()[:16]}"

def build_timeline_query_result_id(query_id: str, rank: int) -> str:
    return f"{query_id}_res_{rank}"

def project_event_to_dict(item: ProjectEvent) -> dict:
    return asdict(item)

def phase_chronology_item_to_dict(item: PhaseChronologyItem) -> dict:
    return asdict(item)

def artifact_evolution_record_to_dict(item: ArtifactEvolutionRecord) -> dict:
    return asdict(item)

def timeline_query_to_dict(item: TimelineQuery) -> dict:
    return asdict(item)

def timeline_query_result_to_dict(item: TimelineQueryResult) -> dict:
    return asdict(item)
