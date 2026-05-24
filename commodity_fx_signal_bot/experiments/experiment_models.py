from dataclasses import dataclass, asdict
import re
import hashlib
from typing import Optional

@dataclass
class ResearchHypothesis:
    hypothesis_id: str
    title: str
    description: str
    hypothesis_status: str
    target_module: str
    target_symbols: list[str]
    timeframe: str
    expected_effect: str
    success_metrics: list[str]
    created_at_utc: str
    updated_at_utc: Optional[str]
    notes: str
    warnings: list[str]

@dataclass
class ExperimentDefinition:
    experiment_id: str
    experiment_name: str
    experiment_type: str
    hypothesis_id: Optional[str]
    profile_name: str
    timeframe: str
    symbols: list[str]
    module_scope: list[str]
    parameters: dict
    baseline_experiment_id: Optional[str]
    created_at_utc: str
    notes: str
    warnings: list[str]

@dataclass
class ExperimentRunManifest:
    run_id: str
    experiment_id: str
    experiment_name: str
    experiment_type: str
    status: str
    profile_name: str
    timeframe: str
    symbols: list[str]
    started_at_utc: str
    finished_at_utc: Optional[str]
    duration_seconds: Optional[float]
    produced_artifacts: list[str]
    metrics: dict
    warnings: list[str]
    error_message: Optional[str] = None

@dataclass
class ExperimentComparison:
    comparison_id: str
    baseline_run_id: Optional[str]
    candidate_run_id: str
    comparison_label: str
    metric_deltas: dict
    improved_metrics: list[str]
    deteriorated_metrics: list[str]
    neutral_metrics: list[str]
    summary: dict
    warnings: list[str]

def sanitize_experiment_name(value: str) -> str:
    value = re.sub(r'[^a-zA-Z0-9]', '_', value)
    value = value.lower()
    return value

def build_hypothesis_id(title: str, timeframe: str, target_module: str) -> str:
    raw = f"{title}_{timeframe}_{target_module}"
    h = hashlib.md5(raw.encode()).hexdigest()[:8]
    return f"hyp_{h}"

def build_experiment_id(experiment_name: str, experiment_type: str, timeframe: str) -> str:
    raw = f"{experiment_name}_{experiment_type}_{timeframe}"
    h = hashlib.md5(raw.encode()).hexdigest()[:8]
    sanitized = sanitize_experiment_name(experiment_name)[:20]
    return f"exp_{sanitized}_{h}"

def build_experiment_run_id(experiment_id: str, created_at_utc: str) -> str:
    raw = f"{experiment_id}_{created_at_utc}"
    h = hashlib.md5(raw.encode()).hexdigest()[:8]
    return f"run_{h}"

def build_experiment_comparison_id(baseline_run_id: Optional[str], candidate_run_id: str) -> str:
    b = baseline_run_id or "none"
    raw = f"{b}_{candidate_run_id}"
    h = hashlib.md5(raw.encode()).hexdigest()[:8]
    return f"cmp_{h}"

def research_hypothesis_to_dict(hypothesis: ResearchHypothesis) -> dict:
    return asdict(hypothesis)

def experiment_definition_to_dict(definition: ExperimentDefinition) -> dict:
    return asdict(definition)

def experiment_run_manifest_to_dict(manifest: ExperimentRunManifest) -> dict:
    return asdict(manifest)

def experiment_comparison_to_dict(comparison: ExperimentComparison) -> dict:
    return asdict(comparison)
