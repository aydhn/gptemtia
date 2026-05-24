import pandas as pd
from typing import Any
import logging

from experiments.experiment_models import ExperimentDefinition, ExperimentRunManifest

logger = logging.getLogger(__name__)

def build_reproducibility_manifest(
    experiment: ExperimentDefinition,
    run_manifest: ExperimentRunManifest,
    version_record: dict,
    artifact_manifest: dict
) -> dict:
    return {
        "run_id": run_manifest.run_id,
        "experiment_id": experiment.experiment_id,
        "version_id": version_record.get("version_id"),
        "has_config_snapshot": "config_snapshot" in version_record,
        "has_environment_snapshot": "environment_snapshot" in version_record,
        "has_git_snapshot": version_record.get("git_snapshot", {}).get("git_commit", "unknown") != "unknown",
        "has_artifact_manifest": artifact_manifest is not None and len(artifact_manifest.get("artifacts", [])) > 0,
        "missing_required_artifacts": artifact_manifest.get("missing_required", []) if artifact_manifest else [],
        "module_scope": experiment.module_scope,
        "symbols": experiment.symbols,
        "timeframe": experiment.timeframe
    }

def validate_reproducibility_manifest(manifest: dict) -> dict:
    warnings = []

    if not manifest.get("has_config_snapshot"):
        warnings.append("Missing config snapshot")
    if not manifest.get("has_environment_snapshot"):
        warnings.append("Missing environment snapshot")
    if not manifest.get("has_git_snapshot"):
        warnings.append("Missing git commit hash or tree is dirty")
    if manifest.get("missing_required_artifacts"):
        warnings.append(f"Missing required artifacts: {manifest['missing_required_artifacts']}")

    valid = len(warnings) == 0
    return {
        "valid": valid,
        "warnings": warnings
    }

def calculate_reproducibility_score(manifest: dict) -> float:
    score = 0.0
    total_weights = 0.0

    weights = {
        "has_config_snapshot": 0.25,
        "has_environment_snapshot": 0.25,
        "has_git_snapshot": 0.25,
        "has_artifact_manifest": 0.15,
        "no_missing_artifacts": 0.10
    }

    if manifest.get("has_config_snapshot"):
        score += weights["has_config_snapshot"]
    total_weights += weights["has_config_snapshot"]

    if manifest.get("has_environment_snapshot"):
        score += weights["has_environment_snapshot"]
    total_weights += weights["has_environment_snapshot"]

    if manifest.get("has_git_snapshot"):
        score += weights["has_git_snapshot"]
    total_weights += weights["has_git_snapshot"]

    if manifest.get("has_artifact_manifest"):
        score += weights["has_artifact_manifest"]
    total_weights += weights["has_artifact_manifest"]

    if not manifest.get("missing_required_artifacts"):
        score += weights["no_missing_artifacts"]
    total_weights += weights["no_missing_artifacts"]

    return score / total_weights if total_weights > 0 else 0.0

def build_rerun_candidate_command(manifest: dict) -> str:
    # Explicitly avoid any live/broker commands.
    scopes = " ".join(manifest.get("module_scope", []))
    timeframe = manifest.get("timeframe", "1d")

    cmd = f"python -m scripts.run_experiment_tracking_report --timeframe {timeframe}"
    if scopes:
        cmd += f" --module-scope {scopes}"

    return cmd

def reproducibility_manifest_to_dataframe(manifest: dict) -> pd.DataFrame:
    flat = {
        "run_id": manifest.get("run_id"),
        "experiment_id": manifest.get("experiment_id"),
        "version_id": manifest.get("version_id"),
        "has_config": manifest.get("has_config_snapshot", False),
        "has_env": manifest.get("has_environment_snapshot", False),
        "has_git": manifest.get("has_git_snapshot", False),
        "missing_artifacts": len(manifest.get("missing_required_artifacts", [])),
        "reproducibility_score": calculate_reproducibility_score(manifest)
    }
    return pd.DataFrame([flat])
