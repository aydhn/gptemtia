import json
import hashlib
from pathlib import Path
import pandas as pd
from typing import Tuple, Dict, List
from datetime import datetime, timezone

def build_checkpoint_key(module_name: str, run_name: str, batch_index: int) -> str:
    raw = f"{module_name}_{run_name}_{batch_index}"
    return hashlib.md5(raw.encode('utf-8')).hexdigest()[:16]

def create_checkpoint_manifest(
    run_name: str,
    module_name: str,
    total_items: int,
    completed_items: int,
    checkpoint_paths: List[str]
) -> dict:
    return {
        "run_name": run_name,
        "module_name": module_name,
        "total_items": total_items,
        "completed_items": completed_items,
        "status": "in_progress" if completed_items < total_items else "completed",
        "last_updated_utc": datetime.now(timezone.utc).isoformat(),
        "checkpoint_paths": checkpoint_paths
    }

def save_checkpoint_manifest(manifest: dict, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)

    run_name = manifest.get("run_name", "unknown_run")
    mod_name = manifest.get("module_name", "unknown_mod")

    filename = f"manifest_{mod_name}_{run_name}.json"
    filepath = output_dir / filename

    with open(filepath, 'w') as f:
        json.dump(manifest, f, indent=2)

    return filepath

def load_checkpoint_manifest(path: Path) -> dict:
    if not path.exists():
        return {}
    with open(path, 'r') as f:
        return json.load(f)

def calculate_checkpoint_progress(manifest: dict) -> float:
    total = manifest.get("total_items", 0)
    completed = manifest.get("completed_items", 0)

    if total <= 0:
        return 0.0

    return min(1.0, completed / total)

def build_resume_plan_from_checkpoint(manifest: dict) -> Tuple[pd.DataFrame, Dict]:
    if not manifest:
        return pd.DataFrame(), {"status": "no_manifest"}

    total = manifest.get("total_items", 0)
    completed = manifest.get("completed_items", 0)
    remaining = max(0, total - completed)

    plan = {
        "module_name": manifest.get("module_name"),
        "run_name": manifest.get("run_name"),
        "completed": completed,
        "remaining": remaining,
        "action": "resume" if remaining > 0 else "complete"
    }

    df = pd.DataFrame([plan])
    summary = {
        "can_resume": remaining > 0,
        "progress_pct": calculate_checkpoint_progress(manifest) * 100
    }

    return df, summary
