"""
Metadata Export module.
"""

import pandas as pd
from pathlib import Path
import json
from .metadata_models import MetadataExportRecord, build_metadata_export_id, metadata_export_record_to_dict
from .metadata_config import ArtifactMetadataProfile

def build_metadata_export_index(artifact_df: pd.DataFrame, card_tables: dict[str, pd.DataFrame], profile: ArtifactMetadataProfile) -> pd.DataFrame:
    if artifact_df.empty:
        return pd.DataFrame()

    records = []
    for _, row in artifact_df.iterrows():
        rec = MetadataExportRecord(
            export_id=build_metadata_export_id(row["artifact_id"], "metadata_bundle"),
            artifact_id=row["artifact_id"],
            card_id=None,
            export_type="metadata_bundle",
            export_path=f"exports/{row['artifact_id']}_metadata.json",
            local_only=True,
            safe_to_share=True,
            warnings=["Not for cloud registry upload."]
        )
        records.append(metadata_export_record_to_dict(rec))

    return pd.DataFrame(records)

def validate_metadata_export_safety(export_manifest: dict, export_index_df: pd.DataFrame, profile: ArtifactMetadataProfile) -> dict:
    warnings = []
    if not export_index_df.empty:
        if not export_index_df["local_only"].all():
             warnings.append("Some exports are not marked local_only.")

    return {
        "safe": len(warnings) == 0,
        "warnings": warnings
    }

def build_research_artifact_metadata_export(artifact_df: pd.DataFrame, card_tables: dict[str, pd.DataFrame], profile: ArtifactMetadataProfile) -> dict:
    manifest = {
        "export_version": "1.0",
        "profile": profile.name,
        "total_artifacts": len(artifact_df) if not artifact_df.empty else 0,
        "total_card_tables": len(card_tables),
        "local_only": True,
        "no_cloud_upload": True,
        "no_raw_secrets": True
    }
    return manifest

def save_metadata_export_manifest(manifest: dict, output_path: Path) -> Path:
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=4)
    return output_path

def summarize_metadata_export(manifest: dict, export_index_df: pd.DataFrame) -> dict:
    return {
        "total_exports": len(export_index_df) if not export_index_df.empty else 0,
        "local_only_confirmed": manifest.get("local_only", False)
    }
