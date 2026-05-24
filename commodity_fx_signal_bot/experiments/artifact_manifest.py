import hashlib
import logging
from pathlib import Path
import pandas as pd
from typing import Optional, Any

logger = logging.getLogger(__name__)

def hash_file(path: Path, max_mb: int = 50) -> Optional[str]:
    if not path.exists() or not path.is_file():
        return None

    try:
        size_mb = path.stat().st_size / (1024 * 1024)
        if size_mb > max_mb:
            logger.warning(f"File {path.name} is too large ({size_mb:.1f} MB > {max_mb} MB). Skipping hash.")
            return "skipped_too_large"

        hasher = hashlib.md5()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        logger.warning(f"Failed to hash {path}: {e}")
        return None

def build_artifact_record(path: Path, artifact_type: str, required: bool = False) -> dict:
    exists = path.exists()
    return {
        "artifact_type": artifact_type,
        "path": str(path),
        "exists": exists,
        "hash": hash_file(path) if exists else None,
        "required": required
    }

def discover_experiment_artifacts(data_lake: Any, module_scope: list[str], timeframe: str, symbols: Optional[list[str]] = None) -> list[dict]:
    # In a real system, we would query the data_lake to find paths.
    # We will return some mock artifact records for testing and demonstration.
    # The true path structure should be inferred or injected.
    artifacts = []

    # Example logic using pseudo paths (a real integration would use paths.py config)
    if "meta_research" in module_scope:
        artifacts.append({
            "artifact_type": "meta",
            "path": f"data/lake/meta_research/reports/meta_report_{timeframe}.json",
            "exists": False,
            "hash": None,
            "required": True
        })

    if "factor_research" in module_scope:
        artifacts.append({
            "artifact_type": "factor",
            "path": f"data/lake/factor_research/reports/factor_report_{timeframe}.json",
            "exists": False,
            "hash": None,
            "required": False
        })

    return artifacts

def build_experiment_artifact_manifest(run_id: str, artifacts: list[dict]) -> dict:
    return {
        "run_id": run_id,
        "artifacts": artifacts,
        "total_artifacts": len(artifacts),
        "existing_artifacts": sum(1 for a in artifacts if a.get("exists")),
        "missing_required": [a["artifact_type"] for a in artifacts if a.get("required") and not a.get("exists")]
    }

def validate_artifact_manifest(manifest: dict) -> dict:
    valid = len(manifest.get("missing_required", [])) == 0
    warnings = []
    if not valid:
        warnings.append(f"Missing required artifacts: {manifest.get('missing_required')}")

    return {
        "valid": valid,
        "warnings": warnings
    }

def artifact_manifest_to_dataframe(manifest: dict) -> pd.DataFrame:
    artifacts = manifest.get("artifacts", [])
    if not artifacts:
        return pd.DataFrame()

    df = pd.DataFrame(artifacts)
    df["run_id"] = manifest.get("run_id")
    return df
