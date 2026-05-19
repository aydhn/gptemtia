"""
Data models for security findings and audits.
"""

from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
import hashlib

@dataclass
class SecurityFinding:
    finding_id: str
    category: str
    severity: str
    status: str
    title: str
    description: str
    file_path: str | None = None
    line_number: int | None = None
    evidence: str | None = None
    recommended_action: str | None = None
    blocking: bool = False
    metadata: dict = field(default_factory=dict)

@dataclass
class SecurityAuditSummary:
    audit_id: str
    profile_name: str
    created_at_utc: str
    total_findings: int
    critical_count: int
    high_count: int
    medium_count: int
    low_count: int
    blocking_count: int
    security_status: str
    readiness_label: str
    readiness_score: float
    warnings: list[str] = field(default_factory=list)

def build_security_finding_id(category: str, title: str, file_path: str | None = None, line_number: int | None = None) -> str:
    raw = f"{category}_{title}_{file_path}_{line_number}"
    return hashlib.md5(raw.encode()).hexdigest()

def build_security_audit_id(profile_name: str) -> str:
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    return f"audit_{profile_name}_{ts}"

def security_finding_to_dict(finding: SecurityFinding) -> dict:
    return asdict(finding)

def security_audit_summary_to_dict(summary: SecurityAuditSummary) -> dict:
    return asdict(summary)

def sanitize_security_evidence(text: str | None) -> str | None:
    if not text:
        return text
    return text.replace("token", "***").replace("secret", "***")
