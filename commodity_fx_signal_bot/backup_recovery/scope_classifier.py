"""
Scope classifier for backup recovery.
"""

from pathlib import Path
from .backup_config import BackupRecoveryProfile
from .backup_labels import validate_backup_scope, validate_artifact_criticality

SENSITIVE_PATTERNS = [
    ".env",
    "secret",
    "credential",
    "token",
    "private_key",
    "api_key",
    "broker_key",
    "exchange_key",
    "password",
    "key.pem",
    "id_rsa"
]

def detect_secret_or_sensitive_path(path: Path) -> bool:
    name_lower = path.name.lower()
    for pattern in SENSITIVE_PATTERNS:
        if pattern in name_lower:
            return True
    return False

def detect_large_or_cache_artifact(path: Path, profile: BackupRecoveryProfile) -> bool:
    if "__pycache__" in str(path) or ".pytest_cache" in str(path) or path.suffix in [".pyc", ".pyo"]:
        return True
    if path.is_file():
        try:
            size_mb = path.stat().st_size / (1024 * 1024)
            if size_mb > profile.max_hash_file_mb:
                return True
        except Exception:
            pass
    return False


def classify_backup_scope(path: Path, project_root: Path, profile: BackupRecoveryProfile) -> str:
    if detect_secret_or_sensitive_path(path):
        return "excluded_secret_scope"
    if detect_large_or_cache_artifact(path, profile):
        if "__pycache__" in str(path) or ".pyc" in path.suffix:
            return "excluded_cache_scope"
        return "excluded_large_artifact_scope"

    rel_path = str(path.relative_to(project_root)).replace("\\", "/")

    if rel_path.startswith("config/"):
        return "config_template_scope"
    if rel_path.startswith("docs/"):
        return "docs_scope"
    if rel_path.startswith("tests/"):
        return "tests_scope"
    if rel_path.endswith(".py") and not rel_path.startswith("reports/") and not rel_path.startswith("data/"):
        return "critical_source_scope"

    if "manifest" in rel_path and rel_path.endswith(".json"):
        return "generated_manifest_scope"

    if rel_path.startswith("reports/output/"):
        return "reports_manifest_only_scope"
    if rel_path.startswith("data/lake/"):
        return "data_manifest_only_scope"

    return "unknown_scope"


def classify_artifact_criticality(path: Path, backup_scope: str) -> str:
    if backup_scope == "excluded_secret_scope":
        return "excluded_artifact"
    if backup_scope in ["critical_source_scope", "config_template_scope"]:
        return "critical_artifact"
    if backup_scope in ["docs_scope", "tests_scope"]:
        return "important_artifact"
    if backup_scope in ["generated_manifest_scope", "reports_manifest_only_scope", "data_manifest_only_scope"]:
        return "generated_artifact"
    return "unknown_criticality"


def decide_backup_include_policy(path: Path, backup_scope: str, criticality: str, profile: BackupRecoveryProfile) -> dict:
    if backup_scope == "excluded_secret_scope":
        return {"include": False, "manifest_only": False, "policy": "exclude"}
    if backup_scope in ["reports_manifest_only_scope", "data_manifest_only_scope"]:
        return {"include": True, "manifest_only": True, "policy": "manifest_only"}

    include = True
    manifest_only = False

    if backup_scope in ["excluded_cache_scope", "excluded_large_artifact_scope"]:
        include = False

    return {"include": include, "manifest_only": manifest_only, "policy": "include" if include else "exclude"}
