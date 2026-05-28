from dataclasses import dataclass, asdict
from typing import Dict, List, Optional
import uuid

@dataclass
class AuditResult:
    audit_id: str
    audit_type: str
    status: str
    title: str
    score: Optional[float]
    passed: bool
    checked_items: int
    warning_count: int
    failure_count: int
    summary: dict
    warnings: List[str]
    failures: List[str]

@dataclass
class FinalRisk:
    risk_id: str
    severity: str
    category: str
    title: str
    description: str
    affected_modules: List[str]
    recommended_action: str
    blocking: bool
    warnings: List[str]

@dataclass
class FinalGap:
    gap_id: str
    category: str
    title: str
    description: str
    affected_modules: List[str]
    priority_score: float
    recommended_follow_up: str
    warnings: List[str]

@dataclass
class FinalAcceptanceSnapshot:
    snapshot_id: str
    created_at_utc: str
    profile_name: str
    acceptance_score: float
    safety_score: float
    readiness_label: str
    audit_count: int
    passed_audit_count: int
    warning_count: int
    failure_count: int
    blocking_risk_count: int
    gap_count: int
    warnings: List[str]

def build_audit_id(audit_type: str, title: str) -> str:
    clean_title = "".join(c if c.isalnum() else "_" for c in title).lower().strip("_")
    return f"{audit_type}_{clean_title}_{uuid.uuid4().hex[:8]}"

def build_final_risk_id(category: str, title: str) -> str:
    clean_title = "".join(c if c.isalnum() else "_" for c in title).lower().strip("_")
    return f"risk_{category}_{clean_title}_{uuid.uuid4().hex[:8]}"

def build_final_gap_id(category: str, title: str) -> str:
    clean_title = "".join(c if c.isalnum() else "_" for c in title).lower().strip("_")
    return f"gap_{category}_{clean_title}_{uuid.uuid4().hex[:8]}"

def build_acceptance_snapshot_id(profile_name: str, created_at_utc: str) -> str:
    clean_time = created_at_utc.replace(":", "").replace("-", "").replace(" ", "_")
    return f"snapshot_{profile_name}_{clean_time}_{uuid.uuid4().hex[:8]}"

def audit_result_to_dict(result: AuditResult) -> dict:
    return asdict(result)

def final_risk_to_dict(risk: FinalRisk) -> dict:
    return asdict(risk)

def final_gap_to_dict(gap: FinalGap) -> dict:
    return asdict(gap)

def final_acceptance_snapshot_to_dict(snapshot: FinalAcceptanceSnapshot) -> dict:
    return asdict(snapshot)

def clamp_review_score(value: Optional[float]) -> Optional[float]:
    if value is None:
        return None
    return max(0.0, min(1.0, value))
