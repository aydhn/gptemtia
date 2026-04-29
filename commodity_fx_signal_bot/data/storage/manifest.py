import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, List, Optional

import pandas as pd

from config.symbols import SymbolSpec
from core.logger import get_logger
from data.storage.data_lake import DataLake

logger = get_logger(__name__)


@dataclass
class DataLakeManifestEntry:
    symbol: str
    name: str
    asset_class: str
    sub_class: str
    data_source: str
    timeframe: str
    path: str
    exists: bool
    rows: int
    start: Optional[str]
    end: Optional[str]
    last_updated_utc: Optional[str]
    quality_grade: str
    notes: str = ""


def build_manifest(
    data_lake: DataLake,
    symbols: List[SymbolSpec],
    timeframes_by_symbol: Dict[str, tuple[str, ...]],
) -> List[DataLakeManifestEntry]:
    """Build a manifest of all available data in the Data Lake."""
    entries = []

    for spec in symbols:
        allowed_tfs = timeframes_by_symbol.get(spec.symbol, tuple())
        metadata = data_lake.load_metadata(spec)

        row_counts = metadata.get("row_counts_by_timeframe", {})
        starts = metadata.get("first_timestamp_by_timeframe", {})
        ends = metadata.get("last_timestamp_by_timeframe", {})
        last_updated = metadata.get("last_updated_utc")
        grades = metadata.get("quality_grades", {})

        for tf in allowed_tfs:
            exists = data_lake.has_ohlcv(spec, tf)
            path = str(data_lake.get_ohlcv_path(spec, tf))

            rows = row_counts.get(tf, 0) if exists else 0
            start = starts.get(tf) if exists else None
            end = ends.get(tf) if exists else None
            grade = grades.get(tf, "N/A") if exists else "N/A"

            entry = DataLakeManifestEntry(
                symbol=spec.symbol,
                name=spec.name,
                asset_class=spec.asset_class,
                sub_class=spec.sub_class,
                data_source=spec.data_source,
                timeframe=tf,
                path=path,
                exists=exists,
                rows=rows,
                start=start,
                end=end,
                last_updated_utc=last_updated if exists else None,
                quality_grade=grade,
            )
            entries.append(entry)

    return entries


def manifest_to_dataframe(entries: List[DataLakeManifestEntry]) -> pd.DataFrame:
    """Convert manifest entries to a DataFrame."""
    return pd.DataFrame([asdict(e) for e in entries])


def save_manifest_csv(entries: List[DataLakeManifestEntry], path: Path) -> None:
    """Save manifest to a CSV file."""
    df = manifest_to_dataframe(entries)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    logger.debug(f"Manifest saved to CSV: {path}")


def save_manifest_json(entries: List[DataLakeManifestEntry], path: Path) -> None:
    """Save manifest to a JSON file."""
    data = [asdict(e) for e in entries]
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    logger.debug(f"Manifest saved to JSON: {path}")


def summarize_manifest(entries: List[DataLakeManifestEntry]) -> dict:
    """Summarize the manifest."""
    total_expected = len(entries)
    existing = [e for e in entries if e.exists]
    total_existing = len(existing)

    missing = total_expected - total_existing
    completion_rate = total_existing / total_expected if total_expected > 0 else 0.0

    grades = {}
    for e in existing:
        grades[e.quality_grade] = grades.get(e.quality_grade, 0) + 1

    by_timeframe = {}
    for e in entries:
        if e.timeframe not in by_timeframe:
            by_timeframe[e.timeframe] = {"expected": 0, "existing": 0}
        by_timeframe[e.timeframe]["expected"] += 1
        if e.exists:
            by_timeframe[e.timeframe]["existing"] += 1

    return {
        "total_expected": total_expected,
        "total_existing": total_existing,
        "missing": missing,
        "completion_rate": completion_rate,
        "grades": grades,
        "by_timeframe": by_timeframe,
    }
