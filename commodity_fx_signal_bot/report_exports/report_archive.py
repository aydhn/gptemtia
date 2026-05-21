import json
import logging
from pathlib import Path
from typing import Optional, Dict
import pandas as pd
from report_exports.export_models import ReportArchiveRecord, report_archive_record_to_dict

logger = logging.getLogger(__name__)

class ReportArchive:
    def __init__(self, archive_dir: Path):
        self.archive_dir = archive_dir
        self.archive_dir.mkdir(parents=True, exist_ok=True)
        self.manifest_path = self.archive_dir / "archive_manifest.jsonl"

    def add_record(self, record: ReportArchiveRecord) -> Path:
        record_dict = report_archive_record_to_dict(record)
        with open(self.manifest_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(record_dict) + "\n")
        return self.manifest_path

    def load_records(self) -> pd.DataFrame:
        if not self.manifest_path.exists():
            return pd.DataFrame()
        records = []
        with open(self.manifest_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    try:
                        records.append(json.loads(line))
                    except json.JSONDecodeError:
                        pass
        df = pd.DataFrame(records)
        if not df.empty and "created_at_utc" in df.columns:
            df["created_at_utc"] = pd.to_datetime(df["created_at_utc"])
            df = df.sort_values("created_at_utc", ascending=False).reset_index(drop=True)
        return df

    def find_previous_report(
        self,
        report_type: str,
        symbol: Optional[str],
        timeframe: str,
        profile_name: str,
        before_utc: Optional[str] = None,
    ) -> Optional[Dict]:
        df = self.load_records()
        if df.empty:
            return None
        mask = (df["report_type"] == report_type) & (df["timeframe"] == timeframe) & (df["profile_name"] == profile_name)
        if symbol:
            mask = mask & (df["symbol"] == symbol)
        if before_utc:
            mask = mask & (df["created_at_utc"].astype(str) < before_utc)
        filtered = df[mask]
        if filtered.empty:
            return None
        latest = filtered.iloc[0].to_dict()
        latest["created_at_utc"] = str(latest["created_at_utc"])
        return latest

    def list_by_symbol(self, symbol: str) -> pd.DataFrame:
        df = self.load_records()
        if df.empty:
            return df
        return df[df["symbol"] == symbol].reset_index(drop=True)

    def list_by_report_type(self, report_type: str) -> pd.DataFrame:
        df = self.load_records()
        if df.empty:
            return df
        return df[df["report_type"] == report_type].reset_index(drop=True)

    def summarize(self) -> Dict:
        df = self.load_records()
        return {
            "total_records": len(df),
            "report_types": df["report_type"].unique().tolist() if not df.empty else [],
            "symbols_covered": df["symbol"].dropna().unique().tolist() if not df.empty else [],
            "latest_record_utc": str(df["created_at_utc"].max()) if not df.empty else None
        }
