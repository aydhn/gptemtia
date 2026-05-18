"""
Data models for orchestration layer.
"""

import hashlib
import json
from dataclasses import dataclass, asdict
from typing import Optional, List

@dataclass
class PipelineJob:
    job_id: str
    job_name: str
    job_type: str
    description: str
    script_module: Optional[str]
    callable_path: Optional[str]
    required_inputs: List[str]
    expected_outputs: List[str]
    dependencies: List[str]
    optional_dependencies: List[str]
    enabled: bool = True
    dry_run_supported: bool = True
    notes: str = ""

@dataclass
class JobExecutionResult:
    job_id: str
    job_name: str
    symbol: Optional[str]
    timeframe: str
    status: str
    started_at_utc: Optional[str]
    finished_at_utc: Optional[str]
    duration_seconds: Optional[float]
    attempts: int
    produced_outputs: List[str]
    missing_dependencies: List[str]
    warnings: List[str]
    error_message: Optional[str] = None

@dataclass
class WorkflowRunManifest:
    run_id: str
    workflow_name: str
    profile_name: str
    timeframe: str
    symbols: List[str]
    started_at_utc: str
    finished_at_utc: Optional[str]
    workflow_status: str
    job_count: int
    success_count: int
    failed_count: int
    skipped_count: int
    dry_run: bool
    results: List[dict]
    warnings: List[str]

def build_orchestration_run_id(workflow_name: str, profile_name: str, timeframe: str, symbols: List[str]) -> str:
    parts = [workflow_name, profile_name, timeframe]
    if symbols:
        symbols_str = "_".join(sorted(symbols))
        symbols_hash = hashlib.md5(symbols_str.encode()).hexdigest()[:8]
        parts.append(symbols_hash)
    base_str = "_".join(parts)
    # deterministic hash for uniqueness
    full_hash = hashlib.md5(base_str.encode()).hexdigest()[:12]
    return f"run_{full_hash}"

def build_job_id(job_name: str, job_type: str) -> str:
    return f"{job_name}_{job_type}"

def pipeline_job_to_dict(job: PipelineJob) -> dict:
    return asdict(job)

def job_execution_result_to_dict(result: JobExecutionResult) -> dict:
    return asdict(result)

def workflow_run_manifest_to_dict(manifest: WorkflowRunManifest) -> dict:
    return asdict(manifest)
