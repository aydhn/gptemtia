from dataclasses import dataclass, asdict
from typing import List, Optional, Dict, Any
import hashlib
import json

@dataclass
class MaintenanceDomain:
    domain_id: str
    domain_name: str
    domain_label: str
    description: str
    owner_role: str
    default_cadence: str
    required_artifacts: List[str]
    warnings: List[str]

@dataclass
class MaintenanceTask:
    task_id: str
    domain_label: str
    task_name: str
    description: str
    cadence: str
    status: str
    last_seen_utc: Optional[str]
    next_review_hint: Optional[str]
    safe_command: Optional[str]
    warnings: List[str]

@dataclass
class DependencyWatchItem:
    dependency_id: str
    dependency_name: str
    source_file: str
    version_spec: Optional[str]
    status: str
    review_reason: str
    recommendation: str
    warnings: List[str]

@dataclass
class MaintenanceFinding:
    finding_id: str
    domain_label: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: List[str]

@dataclass
class MaintenanceBinder:
    binder_id: str
    profile_name: str
    created_at_utc: str
    local_only: bool
    sustainability_score: float
    included_sections: List[str]
    warnings: List[str]

def build_maintenance_domain_id(domain_name: str) -> str:
    hash_input = domain_name.strip()
    return f"domain_{hashlib.sha256(hash_input.encode()).hexdigest()[:12]}"

def build_maintenance_task_id(domain_label: str, task_name: str) -> str:
    hash_input = f"{domain_label}:{task_name}"
    return f"task_{hashlib.sha256(hash_input.encode()).hexdigest()[:12]}"

def build_dependency_watch_id(dependency_name: str, source_file: str) -> str:
    hash_input = f"{dependency_name}:{source_file}"
    return f"dep_{hashlib.sha256(hash_input.encode()).hexdigest()[:12]}"

def build_maintenance_finding_id(domain_label: str, title: str) -> str:
    hash_input = f"{domain_label}:{title}"
    return f"finding_{hashlib.sha256(hash_input.encode()).hexdigest()[:12]}"

def build_maintenance_binder_id(profile_name: str, created_at_utc: str) -> str:
    hash_input = f"{profile_name}:{created_at_utc}"
    return f"binder_{hashlib.sha256(hash_input.encode()).hexdigest()[:12]}"

def maintenance_domain_to_dict(item: MaintenanceDomain) -> Dict[str, Any]:
    return asdict(item)

def maintenance_task_to_dict(item: MaintenanceTask) -> Dict[str, Any]:
    return asdict(item)

def dependency_watch_item_to_dict(item: DependencyWatchItem) -> Dict[str, Any]:
    return asdict(item)

def maintenance_finding_to_dict(item: MaintenanceFinding) -> Dict[str, Any]:
    return asdict(item)

def maintenance_binder_to_dict(item: MaintenanceBinder) -> Dict[str, Any]:
    return asdict(item)
