import os
import json
import joblib
from pathlib import Path
from dataclasses import dataclass, asdict
from datetime import datetime, timezone

@dataclass
class ModelArtifactBundle:
    model_id: str
    model_family: str
    task_type: str
    target_column: str
    model_path: str
    preprocessor_path: str
    metadata_path: str
    feature_schema_path: str
    target_schema_path: str
    created_at_utc: str
    warnings: list[str]

def save_model_artifact(model, model_id: str, base_dir: Path) -> Path:
    safe_id = "".join([c if c.isalnum() or c in "-_" else "_" for c in model_id])
    path = base_dir / f"{safe_id}_model.joblib"
    joblib.dump(model, path)
    return path

def load_model_artifact(path: Path):
    return joblib.load(path)

def save_preprocessor_artifact(preprocessor, model_id: str, base_dir: Path) -> Path:
    safe_id = "".join([c if c.isalnum() or c in "-_" else "_" for c in model_id])
    path = base_dir / f"{safe_id}_preprocessor.joblib"
    joblib.dump(preprocessor, path)
    return path

def load_preprocessor_artifact(path: Path):
    return joblib.load(path)

def save_model_metadata(metadata: dict, model_id: str, base_dir: Path) -> Path:
    safe_id = "".join([c if c.isalnum() or c in "-_" else "_" for c in model_id])
    path = base_dir / f"{safe_id}_metadata.json"
    with open(path, "w") as f:
        json.dump(metadata, f, indent=4)
    return path

def save_schema_snapshot(schema: dict, model_id: str, base_dir: Path, schema_name: str) -> Path:
    safe_id = "".join([c if c.isalnum() or c in "-_" else "_" for c in model_id])
    safe_name = "".join([c if c.isalnum() or c in "-_" else "_" for c in schema_name])
    path = base_dir / f"{safe_id}_{safe_name}.json"
    with open(path, "w") as f:
        json.dump(schema, f, indent=4)
    return path

def build_model_artifact_bundle(
    model_id: str,
    model_family: str,
    task_type: str,
    target_column: str,
    model_path: str,
    preprocessor_path: str,
    metadata_path: str,
    feature_schema_path: str,
    target_schema_path: str,
    warnings: list[str] = None
) -> ModelArtifactBundle:
    return ModelArtifactBundle(
        model_id=model_id,
        model_family=model_family,
        task_type=task_type,
        target_column=target_column,
        model_path=str(model_path),
        preprocessor_path=str(preprocessor_path),
        metadata_path=str(metadata_path),
        feature_schema_path=str(feature_schema_path),
        target_schema_path=str(target_schema_path),
        created_at_utc=datetime.now(timezone.utc).isoformat(),
        warnings=warnings or []
    )

def model_artifact_bundle_to_dict(bundle: ModelArtifactBundle) -> dict:
    return asdict(bundle)
