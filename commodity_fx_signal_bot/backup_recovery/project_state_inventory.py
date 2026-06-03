"""
Project state inventory scanner.
"""

from pathlib import Path
import hashlib
from datetime import datetime, timezone
import pandas as pd

from .backup_config import BackupRecoveryProfile
from .backup_models import ProjectStateArtifact, build_project_state_artifact_id, project_state_artifact_to_dict
from .scope_classifier import classify_backup_scope, classify_artifact_criticality, decide_backup_include_policy


def classify_project_artifact_type(path: Path, project_root: Path) -> str:
    if path.is_dir():
        return "directory"
    return "file"


def calculate_project_artifact_hash(path: Path, profile: BackupRecoveryProfile) -> tuple[str | None, dict]:
    if not path.is_file():
        return None, {}

    try:
        size_mb = path.stat().st_size / (1024 * 1024)
        if size_mb > profile.max_hash_file_mb:
            return None, {"warning": f"File too large for hash: {size_mb:.2f} MB"}

        hasher = hashlib.sha256()
        with open(path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest(), {}
    except Exception as e:
        return None, {"error": str(e)}


def build_project_state_artifact(path: Path, project_root: Path, profile: BackupRecoveryProfile) -> ProjectStateArtifact:
    rel_path = str(path.relative_to(project_root)).replace("\\", "/")
    art_type = classify_project_artifact_type(path, project_root)

    scope = classify_backup_scope(path, project_root, profile)
    criticality = classify_artifact_criticality(path, scope)
    policy_dict = decide_backup_include_policy(path, scope, criticality, profile)

    size_bytes = path.stat().st_size if path.is_file() else None
    modified_at = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).isoformat() if path.exists() else None

    hash_val = None
    warnings = []

    # Do not read secret file content
    if scope != "excluded_secret_scope" and path.is_file() and policy_dict.get("include"):
        hash_val, h_res = calculate_project_artifact_hash(path, profile)
        if "warning" in h_res:
            warnings.append(h_res["warning"])
        if "error" in h_res:
            warnings.append(h_res["error"])

    # basic priority: critical > docs > generated
    pri = 99
    if criticality == "critical_artifact":
        pri = 1
    elif criticality == "important_artifact":
        pri = 2
    elif criticality == "generated_artifact":
        pri = 3

    return ProjectStateArtifact(
        artifact_id=build_project_state_artifact_id(rel_path),
        relative_path=rel_path,
        artifact_type=art_type,
        backup_scope=scope,
        criticality=criticality,
        include_policy=policy_dict["policy"],
        size_bytes=size_bytes,
        content_hash=hash_val,
        modified_at_utc=modified_at,
        restore_priority=pri,
        warnings=warnings
    )


def scan_project_state(project_root: Path, profile: BackupRecoveryProfile) -> tuple[pd.DataFrame, dict]:
    artifacts = []

    roots_to_scan = [
        "commodity_fx_signal_bot",
        "scripts",
        "tests",
        "config",
        "docs",
        "data/lake",
        "reports/output",
        "portable_bundle",
        "backup_recovery_bundle",
    ]

    files_scanned = 0
    for r_dir in roots_to_scan:
        scan_dir = project_root / r_dir
        if not scan_dir.exists():
            continue

        for path in scan_dir.rglob("*"):
            if files_scanned >= profile.max_inventory_files:
                break

            if ".git" in path.parts:
                continue

            art = build_project_state_artifact(path, project_root, profile)
            artifacts.append(project_state_artifact_to_dict(art))
            files_scanned += 1

    df = pd.DataFrame(artifacts)

    summary = summarize_project_state_inventory(df)
    return df, summary


def summarize_project_state_inventory(inventory_df: pd.DataFrame) -> dict:
    if inventory_df is None or inventory_df.empty:
        return {"status": "empty"}

    return {
        "total_artifacts": len(inventory_df),
        "critical_count": len(inventory_df[inventory_df["criticality"] == "critical_artifact"]),
        "excluded_secrets": len(inventory_df[inventory_df["backup_scope"] == "excluded_secret_scope"]),
        "total_size_mb": inventory_df["size_bytes"].sum() / (1024 * 1024) if "size_bytes" in inventory_df else 0
    }
