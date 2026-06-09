import logging
from pathlib import Path
import pandas as pd
from datetime import datetime, timezone
import hashlib

from evidence_governance.evidence_config import EvidenceGovernanceProfile
from evidence_governance.evidence_models import EvidenceArtifact, build_evidence_artifact_id
from evidence_governance.evidence_labels import list_evidence_artifact_labels

logger = logging.getLogger(__name__)

def discover_evidence_artifacts(project_root: Path, profile: EvidenceGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    artifacts = []
    warnings = []

    # Define directories to scan based on instructions
    scan_patterns = [
        "reports/output/**/*",
        "data/lake/**/quality/**/*",
        "data/lake/**/safety/**/*",
        "data/lake/**/validation/**/*",
        "data/lake/**/manifests/**/*",
        "docs/*.md",
        "docs/generated/**/*.md",
        "backup_recovery_bundle/manifests/**/*",
        "portable_bundle/manifests/**/*"
    ]

    skip_patterns = [".env", "secrets", "credentials", ".key", ".pem", "__pycache__", ".git"]

    count = 0
    size_accum = 0

    for pattern in scan_patterns:
        for path in project_root.glob(pattern):
            if not path.is_file():
                continue

            # Skip logic
            if any(skip in path.name for skip in skip_patterns):
                continue

            size = path.stat().st_size
            if size > profile.max_artifact_mb * 1024 * 1024:
                warnings.append(f"File too large, manifest only: {path.relative_to(project_root)}")
                # we could add it without hash, but for now we'll just add it with a warning

            count += 1
            if count > profile.max_artifacts:
                warnings.append(f"Max artifacts reached ({profile.max_artifacts})")
                break

            art = build_evidence_artifact(path, project_root, profile)
            artifacts.append(art)

    from evidence_governance.evidence_models import evidence_artifact_to_dict
    df = pd.DataFrame([evidence_artifact_to_dict(a) for a in artifacts])

    summary = summarize_evidence_artifacts(df)
    summary["warnings"] = warnings
    return df, summary

def classify_evidence_artifact(path: Path, project_root: Path) -> str:
    rel_path = str(path.relative_to(project_root)).lower()

    if "quality" in rel_path:
        return "quality_evidence"
    if "safety" in rel_path:
        return "safety_evidence"
    if "secrets_hygiene" in rel_path:
        return "secrets_hygiene_evidence"
    if "backup_recovery" in rel_path:
        return "backup_recovery_evidence"
    if "portable_packaging" in rel_path:
        return "packaging_evidence"
    if "scenario_regression" in rel_path:
        return "scenario_regression_evidence"
    if "final_review" in rel_path:
        return "final_review_evidence"
    if "master_orchestration" in rel_path:
        return "master_orchestration_evidence"
    if "governance" in rel_path:
        return "governance_evidence"
    if rel_path.startswith("docs/"):
        return "documentation_evidence"
    if rel_path.startswith("reports/"):
        return "report_evidence"
    if rel_path.startswith("data/lake/"):
        return "datalake_evidence"

    return "unknown_evidence"

def infer_evidence_module(path: Path, project_root: Path) -> str:
    parts = path.relative_to(project_root).parts
    if len(parts) > 1:
        if parts[0] == "docs":
            if parts[1] == "generated" and len(parts) > 2:
                return parts[2]
            return "documentation"
        elif parts[0] in ["data", "reports"] and len(parts) > 2:
            return parts[2]
        return parts[1]
    return "unknown"

def calculate_evidence_hash(path: Path, profile: EvidenceGovernanceProfile) -> tuple[str | None, dict]:
    try:
        size = path.stat().st_size
        if size > profile.max_artifact_mb * 1024 * 1024:
            return None, {"warning": "File too large for hash"}

        hasher = hashlib.sha256()
        with open(path, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest(), {}
    except Exception as e:
        return None, {"error": str(e)}

def build_evidence_artifact(path: Path, project_root: Path, profile: EvidenceGovernanceProfile) -> EvidenceArtifact:
    rel_path = str(path.relative_to(project_root))
    art_id = build_evidence_artifact_id(rel_path)
    label = classify_evidence_artifact(path, project_root)
    module = infer_evidence_module(path, project_root)

    mtime = path.stat().st_mtime
    dt = datetime.fromtimestamp(mtime, tz=timezone.utc).isoformat()
    size = path.stat().st_size

    content_hash, hash_info = calculate_evidence_hash(path, profile)
    warnings = []
    if "warning" in hash_info:
        warnings.append(hash_info["warning"])
    if "error" in hash_info:
        warnings.append(hash_info["error"])

    # freshness classification logic is in scoring module, here we set a placeholder
    # to be updated later, or implement a basic check
    days_old = (datetime.now(timezone.utc) - datetime.fromtimestamp(mtime, tz=timezone.utc)).days
    if days_old <= profile.freshness_days_warning:
        freshness = "evidence_fresh"
    elif days_old <= profile.freshness_days_warning * 2:
        freshness = "evidence_warning_stale"
    else:
        freshness = "evidence_stale"

    return EvidenceArtifact(
        artifact_id=art_id,
        relative_path=rel_path,
        artifact_label=label,
        module_name=module,
        evidence_title=path.name,
        evidence_summary=f"Evidence artifact for {module}",
        created_or_modified_at_utc=dt,
        content_hash=content_hash,
        size_bytes=size,
        freshness_label=freshness,
        warnings=warnings
    )

def summarize_evidence_artifacts(artifact_df: pd.DataFrame) -> dict:
    if artifact_df is None or artifact_df.empty:
        return {"total_artifacts": 0}

    return {
        "total_artifacts": len(artifact_df),
        "total_size_bytes": int(artifact_df["size_bytes"].sum()) if "size_bytes" in artifact_df else 0,
        "labels": artifact_df["artifact_label"].value_counts().to_dict() if "artifact_label" in artifact_df else {},
        "freshness": artifact_df["freshness_label"].value_counts().to_dict() if "freshness_label" in artifact_df else {}
    }
