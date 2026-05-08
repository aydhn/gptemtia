import hashlib
from dataclasses import dataclass
import dataclasses
from datetime import datetime, timezone
import pandas as pd

@dataclass
class MLDatasetMetadata:
    dataset_id: str
    symbol: str
    timeframe: str
    profile: str
    row_count: int
    feature_count: int
    target_count: int
    start_date: str
    end_date: str
    feature_sets: list[str]
    target_columns: list[str]
    leakage_audit_passed: bool
    quality_passed: bool
    created_at_utc: str
    warnings: list[str]

def build_dataset_id(symbol: str, timeframe: str, profile: str, target_columns: list[str]) -> str:
    # Create a deterministic ID
    base = f"{symbol}_{timeframe}_{profile}_{','.join(sorted(target_columns))}"
    hash_obj = hashlib.md5(base.encode())
    return f"{symbol}_{timeframe}_{hash_obj.hexdigest()[:8]}"

def build_dataset_metadata(
    symbol: str,
    timeframe: str,
    profile: str,
    dataset: pd.DataFrame,
    feature_columns: list[str],
    target_columns: list[str],
    feature_sets: list[str],
    leakage_audit: dict,
    quality_report: dict
) -> MLDatasetMetadata:

    warnings = leakage_audit.get("warnings", []) + quality_report.get("warnings", [])

    return MLDatasetMetadata(
        dataset_id=build_dataset_id(symbol, timeframe, profile, target_columns),
        symbol=symbol,
        timeframe=timeframe,
        profile=profile,
        row_count=len(dataset),
        feature_count=len(feature_columns),
        target_count=len(target_columns),
        start_date=str(dataset.index.min()) if not dataset.empty else "",
        end_date=str(dataset.index.max()) if not dataset.empty else "",
        feature_sets=feature_sets,
        target_columns=target_columns,
        leakage_audit_passed=leakage_audit.get("passed", False),
        quality_passed=quality_report.get("passed", False),
        created_at_utc=datetime.now(timezone.utc).isoformat(),
        warnings=warnings
    )

def dataset_metadata_to_dict(metadata: MLDatasetMetadata) -> dict:
    return dataclasses.asdict(metadata)
