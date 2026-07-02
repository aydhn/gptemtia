import pandas as pd
from typing import Tuple, Dict
import datetime
from .archive_config import LocalArchiveProfile
from .archive_models import SnapshotCatalogItem, build_snapshot_id, snapshot_catalog_item_to_dict

def build_snapshot_catalog_item(snapshot_name: str, item_df: pd.DataFrame, profile: LocalArchiveProfile) -> SnapshotCatalogItem:
    count = 0
    if not item_df.empty and 'domain_label' in item_df.columns:
        if snapshot_name == "full_project_manifest_snapshot":
            count = len(item_df)
        elif snapshot_name == "docs_reports_snapshot":
            count = len(item_df[item_df['domain_label'].isin(["documentation_archive", "report_archive"])])
        elif snapshot_name == "cross_layer_outputs_snapshot":
            count = len(item_df[item_df['domain_label'] == "cross_layer_archive"])
        elif snapshot_name == "security_boundary_snapshot":
            count = len(item_df[item_df['domain_label'] == "security_archive"])

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    return SnapshotCatalogItem(
        snapshot_id=build_snapshot_id(snapshot_name, now),
        snapshot_name=snapshot_name,
        created_at_utc=now,
        snapshot_scope=snapshot_name,
        item_count=count,
        local_only=True,
        manifest_path=None,
        warnings=["This is a local manifest snapshot, not a cloud backup"]
    )

def build_project_snapshot_catalog(item_df: pd.DataFrame, profile: LocalArchiveProfile) -> Tuple[pd.DataFrame, Dict]:
    scopes = [
        "full_project_manifest_snapshot",
        "docs_reports_snapshot",
        "cross_layer_outputs_snapshot",
        "security_boundary_snapshot",
        "operator_handoff_snapshot",
        "maintenance_preservation_snapshot"
    ]
    snapshots = [build_snapshot_catalog_item(s, item_df, profile) for s in scopes]
    df = pd.DataFrame([snapshot_catalog_item_to_dict(s) for s in snapshots])
    summary = summarize_project_snapshot_catalog(df)
    return df, summary

def summarize_project_snapshot_catalog(snapshot_df: pd.DataFrame) -> Dict:
    if snapshot_df.empty: return {"total_snapshots": 0}
    return {
        "total_snapshots": len(snapshot_df),
        "total_items_in_snapshots": int(snapshot_df['item_count'].sum()),
        "notice": "Snapshots are logical manifests only. No files were copied or uploaded."
    }
