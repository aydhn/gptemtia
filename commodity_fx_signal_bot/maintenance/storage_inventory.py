"""Storage Inventory Builder for offline maintenance."""
from pathlib import Path
from datetime import datetime, timezone
import pandas as pd
from typing import Tuple, Dict

from maintenance.maintenance_config import MaintenanceProfile
from maintenance.maintenance_models import StorageArtifactRecord, build_storage_artifact_id


class StorageInventoryBuilder:
    def __init__(self, project_root: Path):
        self.project_root = project_root

    def scan_storage(
        self,
        profile: MaintenanceProfile,
    ) -> Tuple[pd.DataFrame, Dict]:
        records = []
        scan_dirs = []

        # Hardcoding the scan dirs relative to project_root to avoid heavy imports here
        data_lake = self.project_root / "data" / "lake"
        reports_output = self.project_root / "reports" / "output"
        logs_dir = self.project_root / "logs"
        archives_manifests = self.project_root / "archives" / "manifests"

        if profile.scan_data_lake:
            scan_dirs.extend([
                data_lake / "raw",
                data_lake / "processed",
                data_lake / "performance" / "cache",
                data_lake / "performance" / "checkpoints",
                data_lake / "knowledge_base" / "indexes",
                data_lake / "quality_gates",
                data_lake / "governance",
                data_lake / "experiments"
            ])

        if profile.scan_reports_output:
            scan_dirs.append(reports_output)

        if profile.scan_logs:
            scan_dirs.append(logs_dir)

        scan_dirs.append(archives_manifests)

        for d in scan_dirs:
            if not d.exists() or not d.is_dir():
                continue
            for path in d.rglob("*"):
                if path.is_file():
                    records.append(self.build_storage_record(path, profile))
                    if len(records) >= profile.max_inventory_files:
                        break
            if len(records) >= profile.max_inventory_files:
                break

        df = pd.DataFrame([r.__dict__ for r in records]) if records else pd.DataFrame(columns=[
            "artifact_id", "path", "relative_path", "artifact_type", "retention_category",
            "size_bytes", "modified_at_utc", "age_days", "extension", "protected",
            "lifecycle_label", "warnings"
        ])

        summary = self.summarize_storage_inventory(df)
        return df, summary

    def classify_artifact_type(self, path: Path) -> str:
        parts = path.parts
        if "raw" in parts:
            return "raw_data"
        if "cache" in parts:
            return "cache"
        if "checkpoints" in parts:
            return "checkpoint"
        if "reports" in parts and "output" in parts:
            return "report"
        if "logs" in parts:
            return "log"
        if "experiments" in parts:
            return "experiment"
        if "quality_gates" in parts:
            return "quality_gate"
        if "governance" in parts:
            return "governance"
        if "knowledge_base" in parts:
            return "knowledge_base"
        return "unknown"

    def classify_retention_category(self, path: Path) -> str:
        art_type = self.classify_artifact_type(path)
        mapping = {
            "raw_data": "raw_data_retention",
            "cache": "cache_retention",
            "checkpoint": "checkpoint_retention",
            "report": "report_retention",
            "log": "log_retention",
            "experiment": "experiment_retention",
            "quality_gate": "quality_report_retention",
            "governance": "governance_retention",
            "knowledge_base": "knowledge_base_retention"
        }
        return mapping.get(art_type, "unknown_retention")

    def is_protected_artifact(self, path: Path) -> bool:
        name = path.name
        if name in ["README.md", "ARCHITECTURE.md", "PHASE_LOG.md", ".env.example"]:
            return True
        if path.suffix == ".py" or path.suffix == ".yaml" or path.suffix == ".toml":
            return True
        if "tests" in path.parts:
            return True
        return False

    def build_storage_record(self, path: Path, profile: MaintenanceProfile) -> StorageArtifactRecord:
        try:
            stat = path.stat()
            size = stat.st_size
            mod_time = stat.st_mtime
            mod_dt = datetime.fromtimestamp(mod_time, tz=timezone.utc)
            mod_str = mod_dt.isoformat()
            age = (datetime.now(timezone.utc) - mod_dt).total_seconds() / 86400.0
        except Exception:
            size, mod_str, age = None, None, None

        rel_path = str(path.relative_to(self.project_root)) if self.project_root in path.parents else str(path)
        art_id = build_storage_artifact_id(rel_path, size, mod_str)

        protected = self.is_protected_artifact(path)

        return StorageArtifactRecord(
            artifact_id=art_id,
            path=str(path),
            relative_path=rel_path,
            artifact_type=self.classify_artifact_type(path),
            retention_category=self.classify_retention_category(path),
            size_bytes=size,
            modified_at_utc=mod_str,
            age_days=age,
            extension=path.suffix,
            protected=protected,
            lifecycle_label="protected_artifact" if protected else "unknown_lifecycle",
            warnings=[]
        )

    def summarize_storage_inventory(self, inventory_df: pd.DataFrame) -> dict:
        if inventory_df.empty:
            return {"total_files": 0, "total_size_bytes": 0}

        return {
            "total_files": len(inventory_df),
            "total_size_bytes": inventory_df["size_bytes"].sum() if "size_bytes" in inventory_df else 0,
            "protected_files": int(inventory_df["protected"].sum()) if "protected" in inventory_df else 0,
        }
