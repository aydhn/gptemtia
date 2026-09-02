"""
Archive Candidate Inventory.
"""
import pandas as pd
from pathlib import Path
from local_archival.archival_config import LocalArchivalProfile
from local_archival.sensitive_exclusions import is_sensitive_archival_path

def classify_archival_item_label(path: Path, project_root: Path) -> str:
    parts = path.parts
    if "docs" in parts: return "archival_doc_item"
    if "reports" in parts: return "archival_report_item"
    if "scripts" in parts: return "archival_script_item"
    if "tests" in parts: return "archival_test_item"
    return "archival_unknown_item"

def classify_archival_source_layer(path: Path, project_root: Path) -> str:
    parts = path.parts
    if "docs" in parts: return "docs"
    if "reports" in parts: return "reports"
    return "other"

def discover_archive_candidate_items(project_root: Path, profile: LocalArchivalProfile) -> pd.DataFrame:
    items = []
    if project_root.exists():
        for p in project_root.rglob("*"):
            if p.is_file():
                if ".git" in p.parts or "__pycache__" in p.parts: continue
                if is_sensitive_archival_path(p, project_root): continue
                if p.stat().st_size > profile.max_file_size_mb_for_hash * 1024 * 1024: continue
                try:
                    rel_path = p.relative_to(project_root).as_posix()
                except:
                    rel_path = p.name
                items.append({
                    "relative_path": rel_path,
                    "item_label": classify_archival_item_label(p, project_root),
                    "source_layer": classify_archival_source_layer(p, project_root),
                    "size_bytes": p.stat().st_size
                })
    return pd.DataFrame(items) if items else pd.DataFrame(columns=["relative_path", "item_label", "source_layer", "size_bytes"])

def build_archive_candidate_inventory(project_root: Path, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    df = discover_archive_candidate_items(project_root, profile)
    return df, summarize_archive_candidate_inventory(df)

def summarize_archive_candidate_inventory(inventory_df: pd.DataFrame) -> dict:
    return {"total_candidates": len(inventory_df) if inventory_df is not None else 0}
