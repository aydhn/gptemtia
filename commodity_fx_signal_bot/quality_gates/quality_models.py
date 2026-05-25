from dataclasses import dataclass, asdict
from typing import Dict, List, Optional
import hashlib
import json

@dataclass
class QualityCheckResult:
    check_id: str
    check_type: str
    status: str
    name: str
    passed: bool
    score: Optional[float]
    started_at_utc: str
    finished_at_utc: Optional[str]
    duration_seconds: Optional[float]
    details: dict
    warnings: List[str]
    error_message: Optional[str] = None

@dataclass
class TestHealthRecord:
    test_file: str
    test_count: int
    passed_count: int
    failed_count: int
    skipped_count: int
    pass_rate: Optional[float]
    duration_seconds: Optional[float]
    warnings: List[str]

@dataclass
class ImportGraphRecord:
    module_name: str
    file_path: str
    imports: List[str]
    internal_imports: List[str]
    external_imports: List[str]
    importable: bool
    circular_import_risk: bool
    warnings: List[str]

@dataclass
class ReleaseCandidateManifest:
    rc_id: str
    profile_name: str
    created_at_utc: str
    status_label: str
    quality_score: float
    included_modules: List[str]
    included_reports: List[str]
    included_manifests: List[str]
    checklist_summary: dict
    warnings: List[str]

def build_quality_check_id(check_type: str, name: str) -> str:
    raw = f"{check_type}_{name}"
    return hashlib.md5(raw.encode("utf-8")).hexdigest()

def build_release_candidate_id(profile_name: str, created_at_utc: str) -> str:
    raw = f"{profile_name}_{created_at_utc}"
    return "rc_" + hashlib.md5(raw.encode("utf-8")).hexdigest()

def quality_check_result_to_dict(result: QualityCheckResult) -> dict:
    return asdict(result)

def test_health_record_to_dict(record: TestHealthRecord) -> dict:
    return asdict(record)

def import_graph_record_to_dict(record: ImportGraphRecord) -> dict:
    return asdict(record)

def release_candidate_manifest_to_dict(manifest: ReleaseCandidateManifest) -> dict:
    return asdict(manifest)

def clamp_quality_score(value: Optional[float]) -> Optional[float]:
    if value is None:
        return None
    return max(0.0, min(1.0, float(value)))
