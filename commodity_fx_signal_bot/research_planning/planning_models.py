import hashlib
from dataclasses import dataclass, asdict

@dataclass
class ResearchSignal:
    signal_id: str
    source_module: str
    source_type: str
    symbol: str | None
    timeframe: str | None
    severity_score: float
    opportunity_score: float
    uncertainty_score: float
    quality_score: float | None
    title: str
    description: str
    evidence: dict
    warnings: list[str]

@dataclass
class ResearchTask:
    task_id: str
    task_type: str
    title: str
    description: str
    status: str
    priority_score: float
    priority_label: str
    recommendation_label: str
    source_signal_ids: list[str]
    related_symbols: list[str]
    related_modules: list[str]
    expected_impact: str
    estimated_effort: str
    dependencies: list[str]
    created_at_utc: str
    warnings: list[str]

@dataclass
class NextBestExperiment:
    recommendation_id: str
    task_id: str
    experiment_name: str
    hypothesis: str
    module_scope: list[str]
    symbols: list[str]
    timeframe: str
    expected_learning: str
    priority_score: float
    confidence_score: float
    blocking_factors: list[str]
    warnings: list[str]

@dataclass
class RoadmapHealthSnapshot:
    snapshot_id: str
    created_at_utc: str
    backlog_count: int
    high_priority_count: int
    blocked_count: int
    research_debt_score: float
    opportunity_score: float
    roadmap_health_score: float
    roadmap_status: str
    warnings: list[str]

def build_research_signal_id(source_module: str, title: str, symbol: str | None = None) -> str:
    seed = f"{source_module}_{title}_{symbol}"
    return hashlib.sha256(seed.encode()).hexdigest()[:12]

def build_research_task_id(task_type: str, title: str, related_symbols: list[str] | None = None) -> str:
    symbols_str = "_".join(related_symbols) if related_symbols else "all"
    seed = f"{task_type}_{title}_{symbols_str}"
    return hashlib.sha256(seed.encode()).hexdigest()[:12]

def build_next_best_experiment_id(task_id: str, experiment_name: str) -> str:
    seed = f"{task_id}_{experiment_name}"
    return hashlib.sha256(seed.encode()).hexdigest()[:12]

def build_roadmap_snapshot_id(created_at_utc: str) -> str:
    seed = f"roadmap_{created_at_utc}"
    return hashlib.sha256(seed.encode()).hexdigest()[:12]

def research_signal_to_dict(signal: ResearchSignal) -> dict:
    return asdict(signal)

def research_task_to_dict(task: ResearchTask) -> dict:
    return asdict(task)

def next_best_experiment_to_dict(experiment: NextBestExperiment) -> dict:
    return asdict(experiment)

def roadmap_health_snapshot_to_dict(snapshot: RoadmapHealthSnapshot) -> dict:
    return asdict(snapshot)

def clamp_planning_score(value: float | None) -> float:
    if value is None:
        return 0.0
    return max(0.0, min(1.0, value))
