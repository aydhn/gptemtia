"""
Artifact inventory module.
"""

import os
from pathlib import Path
import hashlib
import pandas as pd
from datetime import datetime, timezone
import logging

from .metadata_config import ArtifactMetadataProfile
from .metadata_models import ResearchArtifact, build_research_artifact_id, research_artifact_to_dict

logger = logging.getLogger(__name__)

def classify_research_artifact_type(path: Path, project_root: Path) -> str:
    rel_path = str(path.relative_to(project_root)).replace("\\", "/")

    if "ml/models" in rel_path or "data/lake/ml/models" in rel_path or "data/lake/factor_research/models" in rel_path:
        return "model_artifact"
    elif "data/lake" in rel_path and ("raw" in rel_path or "processed" in rel_path or "features" in rel_path):
        if "features" in rel_path:
             return "feature_set_artifact"
        if "synthetic" in rel_path:
             return "synthetic_data_artifact"
        return "dataset_artifact"
    elif "experiments" in rel_path:
        return "experiment_artifact"
    elif "backtest" in rel_path:
        return "backtest_artifact"
    elif "validation" in rel_path:
        return "validation_artifact"
    elif "scenarios" in rel_path:
        return "scenario_artifact"
    elif "scenario_regression" in rel_path or "regression" in rel_path:
        return "regression_artifact"
    elif "synthetic_indices" in rel_path:
        return "synthetic_data_artifact"
    elif "research_reports" in rel_path or "reports/output" in rel_path:
        if path.suffix in [".md", ".txt", ".json", ".csv"]:
             return "research_report_artifact"
    elif "evidence_governance" in rel_path:
        return "evidence_artifact"
    elif "docs/generated" in rel_path:
        return "documentation_artifact"

    return "unknown_artifact"

def infer_research_artifact_module(path: Path, project_root: Path) -> str:
    rel_path = str(path.relative_to(project_root)).replace("\\", "/")
    parts = rel_path.split("/")
    if len(parts) > 1:
        return parts[1] if parts[0] == "data" else parts[0]
    return "unknown"

def calculate_research_artifact_hash(path: Path, profile: ArtifactMetadataProfile) -> tuple[str | None, dict]:
    try:
        size_bytes = path.stat().st_size
        if size_bytes > profile.max_artifact_mb * 1024 * 1024:
            return None, {"warning": f"File exceeds max artifact size ({profile.max_artifact_mb}MB), hash skipped."}

        hasher = hashlib.sha256()
        with open(path, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest(), {}
    except Exception as e:
        return None, {"warning": str(e)}

def build_research_artifact(path: Path, project_root: Path, profile: ArtifactMetadataProfile) -> ResearchArtifact:
    rel_path = str(path.relative_to(project_root)).replace("\\", "/")
    art_type = classify_research_artifact_type(path, project_root)
    module = infer_research_artifact_module(path, project_root)

    try:
        stat = path.stat()
        mtime = datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat()
        size = stat.st_size
    except:
        mtime = None
        size = None

    content_hash, hash_info = calculate_research_artifact_hash(path, profile)
    warnings = []
    if "warning" in hash_info:
        warnings.append(hash_info["warning"])

    if art_type == "unknown_artifact":
        warnings.append("Artifact type could not be classified.")

    return ResearchArtifact(
        artifact_id=build_research_artifact_id(rel_path),
        relative_path=rel_path,
        artifact_type=art_type,
        module_name=module,
        title=path.name,
        description=f"{art_type} for {path.name}",
        created_or_modified_at_utc=mtime,
        content_hash=content_hash,
        size_bytes=size,
        use_label="offline_research_use_only",
        metadata_status="metadata_partial",
        warnings=warnings
    )

def discover_research_artifacts(project_root: Path, profile: ArtifactMetadataProfile) -> tuple[pd.DataFrame, dict]:
    artifacts = []
    summary = {
        "total_discovered": 0,
        "warnings": 0,
        "types_found": set()
    }

    # Define search directories relative to project_root
    search_dirs = [
        "data/lake/ml",
        "data/lake/backtest",
        "data/lake/validation",
        "data/lake/experiments",
        "data/lake/scenarios",
        "data/lake/scenario_regression",
        "data/lake/synthetic_indices",
        "data/lake/factor_research",
        "data/lake/meta_research",
        "data/lake/research_reports",
        "reports/output",
        "docs/generated"
    ]

    # Also include models if available
    for d in search_dirs:
        dir_path = project_root / d
        if not dir_path.exists() or not dir_path.is_dir():
            continue

        for root, _, files in os.walk(dir_path):
            if "credentials" in root or "secrets" in root or "__pycache__" in root:
                continue

            for file in files:
                if file.startswith('.') or file.endswith('.pyc') or file == ".env":
                    continue

                file_path = Path(root) / file

                # Check for simple known secret patterns
                if "secret" in file.lower() or "credential" in file.lower() or "key" in file.lower():
                     continue

                try:
                    artifact = build_research_artifact(file_path, project_root, profile)
                    artifacts.append(artifact_to_dict(artifact))
                    summary["total_discovered"] += 1
                    summary["types_found"].add(artifact.artifact_type)
                    if artifact.warnings:
                        summary["warnings"] += len(artifact.warnings)

                    if len(artifacts) >= profile.max_artifacts:
                        logger.warning(f"Max artifacts limit ({profile.max_artifacts}) reached.")
                        summary["warnings"] += 1
                        break
                except Exception as e:
                    logger.warning(f"Error processing {file_path}: {e}")
                    summary["warnings"] += 1

            if len(artifacts) >= profile.max_artifacts:
                break

    summary["types_found"] = list(summary["types_found"])

    if artifacts:
        df = pd.DataFrame(artifacts)
    else:
        df = pd.DataFrame(columns=[
            "artifact_id", "relative_path", "artifact_type", "module_name",
            "title", "description", "created_or_modified_at_utc", "content_hash",
            "size_bytes", "use_label", "metadata_status", "warnings"
        ])

    return df, summary

def artifact_to_dict(artifact: ResearchArtifact) -> dict:
     return research_artifact_to_dict(artifact)

def summarize_research_artifacts(artifact_df: pd.DataFrame) -> dict:
    if artifact_df.empty:
        return {"total_artifacts": 0}

    return {
        "total_artifacts": len(artifact_df),
        "types": artifact_df["artifact_type"].value_counts().to_dict(),
        "modules": artifact_df["module_name"].value_counts().to_dict()
    }
