from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from governance.fingerprinting import build_artifact_fingerprint
from governance.governance_config import GovernanceProfile
from governance.governance_models import ArtifactRecord, build_artifact_id


class ArtifactInventoryBuilder:
    def __init__(self, project_root: Path, data_lake_root: Path, reports_root: Path):
        self.project_root = project_root
        self.data_lake_root = data_lake_root
        self.reports_root = reports_root

    def scan_artifacts(self, profile: GovernanceProfile) -> tuple[pd.DataFrame, dict]:
        records = []
        warnings = []

        directories_to_scan = []
        if profile.scan_data_lake:
            directories_to_scan.append(self.data_lake_root)
        if profile.scan_reports_output:
            directories_to_scan.append(self.reports_root)

        for root_dir in directories_to_scan:
            if not root_dir.exists():
                warnings.append(f"Directory not found: {root_dir}")
                continue

            for path in root_dir.rglob("*"):
                if path.is_file():
                    # skip .gitignore, .env etc if somehow present in lake
                    if path.name.startswith("."):
                        continue

                    # Skip governance output itself to avoid infinite loops
                    if "governance" in path.parts:
                        continue

                    record = self.build_artifact_record(path, profile)
                    records.append(record)

        df = pd.DataFrame([r.__dict__ for r in records])
        summary = self.summarize_inventory(df)
        summary["warnings"] = warnings
        return df, summary

    def classify_artifact_type(self, path: Path) -> str:
        parts = path.parts

        if "features" in parts: return "feature_artifact"
        if "backtests" in parts: return "backtest_artifact"
        if "factor_research" in parts: return "factor_artifact"
        if "meta_research" in parts: return "meta_research_artifact"
        if "experiments" in parts: return "experiment_artifact"
        if "research_reports" in parts: return "research_report_artifact"
        if "report_exports" in parts: return "report_export_artifact"
        if "synthetic_indices" in parts: return "synthetic_index_artifact"
        if "portfolio_regime" in parts: return "regime_artifact"
        if "processed" in parts: return "processed_data_artifact"
        if "raw" in parts: return "raw_data_artifact"
        if "candidates" in parts: return "candidate_artifact"
        if "observability" in parts: return "observability_artifact"

        return "unknown_artifact"

    def build_artifact_record(self, path: Path, profile: GovernanceProfile) -> ArtifactRecord:
        try:
            rel_path = path.relative_to(self.project_root)
        except ValueError:
            rel_path = path

        stat = path.stat()
        size_bytes = stat.st_size if profile.capture_artifact_sizes else None

        modified_at_utc = None
        if profile.capture_modified_times:
            modified_at_utc = datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat()

        created_at_utc = datetime.fromtimestamp(stat.st_ctime, tz=timezone.utc).isoformat()

        artifact_id = build_artifact_id(str(rel_path), size_bytes, modified_at_utc)
        artifact_type = self.classify_artifact_type(path)

        fingerprint_data, fp_meta = build_artifact_fingerprint(path, profile)

        warnings = []
        if fp_meta.get("warnings"):
            warnings.extend(fp_meta["warnings"])

        if "secret" in str(path).lower() or "key" in str(path).lower() or ".env" in str(path).lower():
            warnings.append("Potential sensitive data file included in inventory.")

        return ArtifactRecord(
            artifact_id=artifact_id,
            artifact_type=artifact_type,
            path=str(path),
            relative_path=str(rel_path),
            file_name=path.name,
            extension=path.suffix,
            size_bytes=size_bytes,
            modified_at_utc=modified_at_utc,
            created_at_utc=created_at_utc,
            row_count=fingerprint_data.get("row_count"),
            column_count=fingerprint_data.get("column_count"),
            schema_fingerprint=fingerprint_data.get("schema_fingerprint"),
            content_fingerprint=fingerprint_data.get("content_fingerprint"),
            warnings=warnings
        )

    def summarize_inventory(self, inventory_df: pd.DataFrame) -> dict:
        if inventory_df.empty:
            return {
                "total_artifacts": 0,
                "artifacts_by_type": {},
                "total_size_mb": 0,
                "artifacts_with_warnings": 0
            }

        type_counts = inventory_df["artifact_type"].value_counts().to_dict()
        total_size = inventory_df["size_bytes"].sum() / (1024*1024) if "size_bytes" in inventory_df and inventory_df["size_bytes"].notna().any() else 0
        warning_count = len(inventory_df[inventory_df["warnings"].apply(lambda x: len(x) > 0)])

        return {
            "total_artifacts": len(inventory_df),
            "artifacts_by_type": type_counts,
            "total_size_mb": total_size,
            "artifacts_with_warnings": warning_count
        }
