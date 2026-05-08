import json
import pandas as pd
from pathlib import Path
from dataclasses import dataclass, asdict
from datetime import datetime, timezone

@dataclass
class ModelRegistryEntry:
    model_id: str
    symbol: str
    timeframe: str
    training_profile: str
    dataset_profile: str
    model_family: str
    task_type: str
    target_column: str
    artifact_paths: dict
    metrics: dict
    cv_summary: dict
    leakage_audit_passed: bool
    dataset_quality_passed: bool
    model_quality_passed: bool
    registry_status: str
    created_at_utc: str
    warnings: list[str]

def model_registry_entry_to_dict(entry: ModelRegistryEntry) -> dict:
    return asdict(entry)

def build_registry_status(metrics: dict, quality_report: dict, leakage_audit: dict | None = None) -> str:
    if leakage_audit and not leakage_audit.get("passed", True):
        return "rejected_candidate"

    if not quality_report.get("passed", True):
        return "quality_failed"

    if quality_report.get("warnings"):
        return "registered_warning_candidate"

    return "registered_candidate"

class ModelRegistry:
    def __init__(self, registry_dir: Path):
        self.registry_dir = registry_dir
        self.registry_dir.mkdir(parents=True, exist_ok=True)

    def register(self, entry: ModelRegistryEntry) -> Path:
        safe_id = "".join([c if c.isalnum() or c in "-_" else "_" for c in entry.model_id])
        path = self.registry_dir / f"{safe_id}_registry.json"
        with open(path, "w") as f:
            json.dump(model_registry_entry_to_dict(entry), f, indent=4)
        return path

    def list_entries(self) -> pd.DataFrame:
        data = []
        for file_path in self.registry_dir.glob("*_registry.json"):
            with open(file_path, "r") as f:
                try:
                    entry = json.load(f)
                    data.append(entry)
                except Exception:
                    pass

        if not data:
            return pd.DataFrame()
        return pd.DataFrame(data)

    def load_entry(self, model_id: str) -> dict:
        safe_id = "".join([c if c.isalnum() or c in "-_" else "_" for c in model_id])
        path = self.registry_dir / f"{safe_id}_registry.json"
        if not path.exists():
            return {}
        with open(path, "r") as f:
            return json.load(f)

    def find_by_symbol(self, symbol: str) -> pd.DataFrame:
        df = self.list_entries()
        if df.empty:
            return df
        return df[df['symbol'] == symbol]

    def find_by_target(self, target_column: str) -> pd.DataFrame:
        df = self.list_entries()
        if df.empty:
            return df
        return df[df['target_column'] == target_column]
