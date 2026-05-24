import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from governance.governance_models import ProvenanceRecord, build_provenance_id


class ProvenanceRegistry:
    def __init__(self, registry_dir: Path):
        self.registry_dir = registry_dir
        self.registry_dir.mkdir(parents=True, exist_ok=True)
        self.registry_file = self.registry_dir / "provenance_records.jsonl"

    def add_record(self, record: ProvenanceRecord) -> Path:
        with open(self.registry_file, 'a') as f:
            f.write(json.dumps(record.__dict__) + '\n')
        return self.registry_file

    def load_records(self) -> pd.DataFrame:
        if not self.registry_file.exists():
            return pd.DataFrame()

        records = []
        with open(self.registry_file, 'r') as f:
            for line in f:
                if line.strip():
                    records.append(json.loads(line))
        return pd.DataFrame(records)

    def get_record(self, provenance_id: str) -> dict | None:
        df = self.load_records()
        if df.empty:
            return None
        res = df[df["provenance_id"] == provenance_id]
        if res.empty:
            return None
        return res.iloc[0].to_dict()

    def find_by_artifact_id(self, artifact_id: str) -> pd.DataFrame:
        df = self.load_records()
        if df.empty:
            return pd.DataFrame()
        return df[df["artifact_id"] == artifact_id]

    def find_by_producer_module(self, producer_module: str) -> pd.DataFrame:
        df = self.load_records()
        if df.empty:
            return pd.DataFrame()
        return df[df["producer_module"] == producer_module]

    def summarize(self) -> dict:
        df = self.load_records()
        if df.empty:
            return {"total_records": 0}

        return {
            "total_records": len(df),
            "unique_artifacts": df["artifact_id"].nunique(),
            "sources": df["source_system"].value_counts().to_dict(),
            "producers": df["producer_module"].value_counts().to_dict() if "producer_module" in df else {}
        }

def infer_producer_module_from_path(path: str) -> str | None:
    path_lower = path.lower()
    if "factor_research" in path_lower: return "factor_research"
    if "meta_research" in path_lower: return "meta_research"
    if "experiments" in path_lower: return "experiments"
    if "synthetic_indices" in path_lower: return "synthetic_indices"
    if "portfolio_regime" in path_lower: return "portfolio_regime"
    if "research_reports" in path_lower: return "research_reports"
    if "report_exports" in path_lower: return "report_exports"
    if "backtests" in path_lower: return "backtest_pipeline"
    if "features" in path_lower: return "feature_pipeline"
    return None

def infer_source_system_from_path(path: str) -> str:
    path_lower = path.lower()
    if "raw" in path_lower:
        if "yahoo" in path_lower or "yfinance" in path_lower:
            return "yahoo_finance_library"
        if "fred" in path_lower:
            return "fred_api"
        if "evds" in path_lower:
            return "evds_api"
        return "external_api"
    if "reports" in path_lower:
        return "report_generated"
    if "experiments" in path_lower:
        return "experiment_manifest"
    return "data_lake_derived"

def build_provenance_records_from_inventory(inventory_df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    records = []
    warnings_list = []

    if inventory_df.empty:
        return pd.DataFrame(), {"warnings": ["Inventory is empty"]}

    for _, row in inventory_df.iterrows():
        artifact_id = row["artifact_id"]
        path = row["relative_path"]

        producer = infer_producer_module_from_path(path)
        source = infer_source_system_from_path(path)

        prov_id = build_provenance_id(artifact_id, producer)

        warnings = []
        if producer is None:
            warnings.append(f"Could not reliably infer producer for {path}")

        record = ProvenanceRecord(
            provenance_id=prov_id,
            artifact_id=artifact_id,
            artifact_type=row["artifact_type"],
            source_system=source,
            producer_module=producer,
            producer_script=None,
            run_id=None,
            experiment_id=None,
            timeframe=None,
            symbols=[],
            parameters_hash=None,
            input_artifact_ids=[],
            created_at_utc=datetime.now(timezone.utc).isoformat(),
            warnings=warnings
        )
        records.append(record)
        if warnings:
            warnings_list.extend(warnings)

    df = pd.DataFrame([r.__dict__ for r in records])
    summary = {
        "total_provenance_records": len(df),
        "warnings": warnings_list
    }
    return df, summary
