
from dataclasses import dataclass
import hashlib
from typing import Optional

@dataclass
class SensitiveFileRecord:
    file_id: str
    relative_path: str
    file_type: str
    size_bytes: Optional[int]
    scan_allowed: bool
    scan_reason: str
    sensitive_path_hint: bool
    warnings: list[str]

@dataclass
class SecretFinding:
    finding_id: str
    finding_type: str
    severity: str
    relative_path: str
    line_number: Optional[int]
    column_start: Optional[int]
    masked_value: Optional[str]
    pattern_name: str
    confidence: float
    redaction_status: str
    warnings: list[str]

@dataclass
class CredentialBoundaryResult:
    boundary_id: str
    boundary_name: str
    status: str
    checked_paths: list[str]
    finding_count: int
    critical_count: int
    summary: dict
    warnings: list[str]

@dataclass
class EnvTemplateAuditItem:
    item_id: str
    variable_name: str
    template_path: str
    status: str
    has_placeholder: bool
    has_realistic_secret_value: bool
    recommendation: str
    warnings: list[str]

@dataclass
class SecretRemediationRecommendation:
    recommendation_id: str
    finding_id: Optional[str]
    title: str
    description: str
    safe_action: str
    destructive: bool
    requires_manual_review: bool
    warnings: list[str]

def build_sensitive_file_id(relative_path: str) -> str:
    raw = f"{relative_path}".encode('utf-8')
    return f"sf_{hashlib.md5(raw).hexdigest()[:12]}"

def build_secret_finding_id(relative_path: str, line_number: Optional[int], pattern_name: str, masked_value: Optional[str]) -> str:
    raw = f"{relative_path}_{line_number}_{pattern_name}_{masked_value}".encode('utf-8')
    return f"sec_{hashlib.md5(raw).hexdigest()[:12]}"

def build_credential_boundary_id(boundary_name: str) -> str:
    raw = f"{boundary_name}".encode('utf-8')
    return f"cb_{hashlib.md5(raw).hexdigest()[:12]}"

def build_env_template_item_id(variable_name: str, template_path: str) -> str:
    raw = f"{variable_name}_{template_path}".encode('utf-8')
    return f"env_{hashlib.md5(raw).hexdigest()[:12]}"

def build_secret_recommendation_id(title: str, finding_id: Optional[str] = None) -> str:
    raw = f"{title}_{finding_id}".encode('utf-8')
    return f"rec_{hashlib.md5(raw).hexdigest()[:12]}"

def sensitive_file_record_to_dict(record: SensitiveFileRecord) -> dict:
    return record.__dict__

def secret_finding_to_dict(finding: SecretFinding) -> dict:
    return finding.__dict__

def credential_boundary_result_to_dict(result: CredentialBoundaryResult) -> dict:
    return result.__dict__

def env_template_audit_item_to_dict(item: EnvTemplateAuditItem) -> dict:
    return item.__dict__

def secret_remediation_recommendation_to_dict(item: SecretRemediationRecommendation) -> dict:
    return item.__dict__
