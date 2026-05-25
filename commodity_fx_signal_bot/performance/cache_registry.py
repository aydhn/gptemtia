import json
import hashlib
from pathlib import Path
import pandas as pd
from typing import Optional, Dict, List
from datetime import datetime, timezone

from .performance_models import CacheRecord, cache_record_to_dict

class CacheRegistry:
    def __init__(self, cache_dir: Path):
        self.cache_dir = cache_dir
        self.registry_file = self.cache_dir / "cache_registry.jsonl"
        self._ensure_dir()

    def _ensure_dir(self):
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        if not self.registry_file.exists():
            self.registry_file.touch()

    def add_cache_record(self, record: CacheRecord) -> Path:
        with open(self.registry_file, 'a') as f:
            f.write(json.dumps(cache_record_to_dict(record)) + '\n')
        return self.registry_file

    def load_cache_records(self) -> pd.DataFrame:
        if not self.registry_file.exists():
            return pd.DataFrame()
        records = []
        with open(self.registry_file, 'r') as f:
            for line in f:
                if line.strip():
                    try:
                        records.append(json.loads(line))
                    except json.JSONDecodeError:
                        pass
        return pd.DataFrame(records)

    def get_cache_record(self, cache_key: str) -> Optional[dict]:
        df = self.load_cache_records()
        if df.empty or "cache_key" not in df.columns:
            return None
        matches = df[df["cache_key"] == cache_key]
        if matches.empty:
            return None
        # Return the most recent one
        return matches.iloc[-1].to_dict()

    def mark_cache_status(self, cache_key: str, status: str) -> dict:
        record = self.get_cache_record(cache_key)
        if record:
            record["status"] = status
            # For simplicity, we just append a new record with updated status
            # In a real system we'd rewrite or update
            with open(self.registry_file, 'a') as f:
                f.write(json.dumps(record) + '\n')
            return record
        return {}

    def summarize(self) -> dict:
        df = self.load_cache_records()
        if df.empty:
            return {"total_records": 0, "total_size_mb": 0.0}

        # Deduplicate by cache_id to get latest
        if "cache_id" in df.columns:
            df = df.drop_duplicates(subset=["cache_id"], keep="last")

        total_size = df["size_bytes"].sum() if "size_bytes" in df.columns else 0
        return {
            "total_records": len(df),
            "total_size_mb": total_size / (1024 * 1024) if total_size else 0.0
        }

def build_cache_key(module_name: str, operation_name: str, parameters: Optional[dict] = None) -> str:
    parts = [module_name, operation_name]
    if parameters:
        # Sort to ensure consistent key
        sorted_params = sorted(parameters.items())
        parts.append(str(sorted_params))
    raw = "_".join(parts)
    return hashlib.md5(raw.encode('utf-8')).hexdigest()[:16]

def build_source_signature(paths: Optional[List[Path]] = None, params: Optional[dict] = None) -> str:
    raw = ""
    if paths:
        for p in sorted(paths):
            if p.exists() and p.is_file():
                raw += f"{p.name}:{p.stat().st_mtime}|"
            else:
                raw += f"{p.name}:missing|"
    if params:
        raw += str(sorted(params.items()))
    return hashlib.md5(raw.encode('utf-8')).hexdigest()[:16]

def infer_cache_type_from_path(path: Path) -> str:
    ext = path.suffix.lower()
    if ext == '.parquet':
        return 'parquet'
    elif ext == '.csv':
        return 'csv'
    elif ext == '.json':
        return 'json'
    else:
        return 'unknown'

def cache_records_to_dataframe(records: List[CacheRecord]) -> pd.DataFrame:
    return pd.DataFrame([cache_record_to_dict(r) for r in records])
