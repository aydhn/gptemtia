import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from governance.governance_models import AuditTrailRecord, build_audit_id


class AuditTrail:
    def __init__(self, audit_dir: Path):
        self.audit_dir = audit_dir
        self.audit_dir.mkdir(parents=True, exist_ok=True)
        self.audit_file = self.audit_dir / "audit_trail.jsonl"

    def add_event(self, record: AuditTrailRecord) -> Path:
        with open(self.audit_file, 'a') as f:
            f.write(json.dumps(record.__dict__) + '\n')
        return self.audit_file

    def load_events(self) -> pd.DataFrame:
        if not self.audit_file.exists():
            return pd.DataFrame()

        records = []
        with open(self.audit_file, 'r') as f:
            for line in f:
                if line.strip():
                    records.append(json.loads(line))
        return pd.DataFrame(records)

    def filter_by_artifact(self, artifact_id: str) -> pd.DataFrame:
        df = self.load_events()
        if df.empty:
            return df
        return df[df["artifact_id"] == artifact_id]

    def filter_by_event_label(self, event_label: str) -> pd.DataFrame:
        df = self.load_events()
        if df.empty:
            return df
        return df[df["event_label"] == event_label]

    def summarize(self) -> dict:
        df = self.load_events()
        if df.empty:
            return {"total_events": 0}

        return {
            "total_events": len(df),
            "event_types": df["event_label"].value_counts().to_dict(),
            "actors": df["actor"].value_counts().to_dict()
        }

def build_audit_events_from_inventory(inventory_df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    events = []
    warnings = []

    if inventory_df.empty:
        return pd.DataFrame(), {"warnings": ["Empty inventory"]}

    for _, row in inventory_df.iterrows():
        art_id = row["artifact_id"]
        ts = datetime.now(timezone.utc).isoformat()

        event = AuditTrailRecord(
            audit_id=build_audit_id("artifact_scanned", art_id, ts),
            event_label="artifact_scanned",
            artifact_id=art_id,
            actor="local_research_system",
            event_timestamp_utc=ts,
            description=f"Scanned artifact {row.get('file_name', 'unknown')}",
            metadata={"path": row.get("path")},
            warnings=[]
        )
        events.append(event.__dict__)

    return pd.DataFrame(events), {"warnings": warnings}

def build_audit_events_from_lineage(node_df: pd.DataFrame, edge_df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    events = []
    ts = datetime.now(timezone.utc).isoformat()

    if node_df is not None and not node_df.empty:
        event = AuditTrailRecord(
            audit_id=build_audit_id("lineage_recorded", None, ts),
            event_label="lineage_recorded",
            artifact_id=None,
            actor="local_research_system",
            event_timestamp_utc=ts,
            description=f"Generated lineage graph with {len(node_df)} nodes.",
            metadata={"node_count": len(node_df)},
            warnings=[]
        )
        events.append(event.__dict__)

    return pd.DataFrame(events), {"warnings": []}

def build_audit_trail_report(audit_df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    summary = {
        "total": len(audit_df) if audit_df is not None else 0,
        "note": "This is a local research audit trail. It is NOT a broker or compliance audit."
    }
    return audit_df, summary
