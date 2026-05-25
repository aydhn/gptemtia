from dataclasses import dataclass, asdict
from typing import Optional, List
import hashlib
import re

@dataclass
class RuntimeProfileRecord:
    profile_id: str
    command_name: str
    module_name: str
    command: str
    started_at_utc: str
    finished_at_utc: Optional[str]
    duration_seconds: Optional[float]
    exit_code: Optional[int]
    timed_out: bool
    stdout_tail: Optional[str]
    stderr_tail: Optional[str]
    warnings: List[str]

@dataclass
class MemoryProfileRecord:
    profile_id: str
    command_name: str
    module_name: str
    peak_memory_mb: Optional[float]
    start_memory_mb: Optional[float]
    end_memory_mb: Optional[float]
    memory_delta_mb: Optional[float]
    budget_status: str
    warnings: List[str]

@dataclass
class ResourceBudget:
    budget_id: str
    module_name: str
    max_runtime_seconds: int
    max_memory_mb: int
    max_batch_symbols: int
    max_parallel_workers: int
    cache_enabled: bool
    checkpointing_enabled: bool
    warnings: List[str]

@dataclass
class CacheRecord:
    cache_id: str
    cache_key: str
    cache_type: str
    path: str
    size_bytes: Optional[int]
    created_at_utc: Optional[str]
    expires_at_utc: Optional[str]
    status: str
    source_signature: Optional[str]
    warnings: List[str]

@dataclass
class BatchPlan:
    plan_id: str
    plan_name: str
    module_name: str
    total_items: int
    batch_size: int
    batch_count: int
    max_parallel_workers: int
    checkpoint_every_items: int
    estimated_runtime_seconds: Optional[float]
    warnings: List[str]

def build_runtime_profile_id(command_name: str, started_at_utc: str) -> str:
    raw = f"{command_name}_{started_at_utc}"
    return hashlib.md5(raw.encode('utf-8')).hexdigest()[:12]

def build_resource_budget_id(module_name: str, profile_name: str) -> str:
    raw = f"{module_name}_{profile_name}"
    return hashlib.md5(raw.encode('utf-8')).hexdigest()[:12]

def build_cache_id(cache_key: str, cache_type: str) -> str:
    raw = f"{cache_key}_{cache_type}"
    return hashlib.md5(raw.encode('utf-8')).hexdigest()[:12]

def build_batch_plan_id(plan_name: str, module_name: str) -> str:
    raw = f"{plan_name}_{module_name}"
    return hashlib.md5(raw.encode('utf-8')).hexdigest()[:12]

def runtime_profile_record_to_dict(record: RuntimeProfileRecord) -> dict:
    return asdict(record)

def memory_profile_record_to_dict(record: MemoryProfileRecord) -> dict:
    return asdict(record)

def resource_budget_to_dict(budget: ResourceBudget) -> dict:
    return asdict(budget)

def cache_record_to_dict(record: CacheRecord) -> dict:
    return asdict(record)

def batch_plan_to_dict(plan: BatchPlan) -> dict:
    return asdict(plan)

def sanitize_command_for_profile(command: str) -> str:
    # Basic sanitization, remove extra spaces
    sanitized = re.sub(r'\s+', ' ', command).strip()
    return sanitized
