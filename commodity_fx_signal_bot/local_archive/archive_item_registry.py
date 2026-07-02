import os
from pathlib import Path
import pandas as pd
from typing import Tuple, Dict, List
import datetime
from .archive_config import LocalArchiveProfile
from .archive_models import ArchiveItem, build_archive_item_id, archive_item_to_dict

def classify_archive_domain_from_path(path: Path, project_root: Path) -> str:
    try:
        rel_path = path.relative_to(project_root)
        parts = rel_path.parts
    except ValueError:
        return "unknown_archive"

    if not parts:
        return "unknown_archive"

    top_level = parts[0]

    if top_level == "docs":
        return "documentation_archive"
    elif top_level == "reports":
        return "report_archive"
    elif top_level == "data" and len(parts) > 1 and parts[1] == "lake":
        return "datalake_archive"
    elif top_level == "config":
        return "config_archive"
    elif top_level == "scripts":
        return "script_archive"
    elif top_level == "tests":
        return "test_archive"
    elif top_level == "security":
        return "security_archive"

    if "consistency" in str(rel_path) or "evidence" in str(rel_path):
        return "cross_layer_archive"

    if rel_path.name == "README.md":
        return "documentation_archive"

    return "unknown_archive"

def classify_archive_item_status(path: Path, project_root: Path, profile: LocalArchiveProfile) -> str:
    name = path.name.lower()
    if name in [".env", "secrets.yaml", "credentials.json", ".gitignore"]:
        return "archive_excluded"
    if name.endswith((".key", ".pem", ".p12", ".pfx")):
        return "archive_excluded"
    if "secret" in name or "credential" in name or "token" in name or "private" in name:
        return "archive_excluded"

    try:
        rel_path = path.relative_to(project_root)
        parts = rel_path.parts
        if "__pycache__" in parts or ".git" in parts or "cache" in parts:
            return "archive_excluded"
    except ValueError:
        pass

    return "archive_candidate"

def build_archive_item_from_path(path: Path, project_root: Path, profile: LocalArchiveProfile) -> ArchiveItem:
    try:
        rel_path = str(path.relative_to(project_root))
    except ValueError:
        rel_path = str(path)

    domain_label = classify_archive_domain_from_path(path, project_root)
    status = classify_archive_item_status(path, project_root, profile)

    size = None
    modified = None

    if path.exists() and path.is_file():
        try:
            stat = path.stat()
            size = stat.st_size
            modified = datetime.datetime.fromtimestamp(stat.st_mtime, tz=datetime.timezone.utc).isoformat()
        except OSError:
            pass

    warnings = []
    if status == "archive_excluded":
        warnings.append("Item is excluded. Content should not be captured.")

    return ArchiveItem(
        item_id=build_archive_item_id(rel_path),
        relative_path=rel_path,
        domain_label=domain_label,
        item_status=status,
        retention_label="retention_unknown",
        size_bytes=size,
        modified_at_utc=modified,
        content_hash=None,
        integrity_status="integrity_unknown",
        warnings=warnings
    )

def build_archive_item_registry(project_root: Path, domain_df: pd.DataFrame, profile: LocalArchiveProfile) -> Tuple[pd.DataFrame, Dict]:
    items = []
    item_count = 0
    max_items = profile.max_items

    for root, dirs, files in os.walk(project_root):
        dirs[:] = [d for d in dirs if d not in [".git", "__pycache__", "venv", ".venv", "env", ".env_folder"]]
        for file in files:
            if item_count >= max_items:
                break
            path = Path(root) / file
            domain = classify_archive_domain_from_path(path, project_root)
            if domain == "documentation_archive" and not profile.scan_docs: continue
            if domain == "report_archive" and not profile.scan_reports: continue
            if domain == "datalake_archive" and not profile.scan_data_lake: continue
            if domain == "config_archive" and not profile.scan_configs: continue
            if domain == "script_archive" and not profile.scan_scripts: continue
            if domain == "test_archive" and not profile.scan_tests: continue
            if domain == "cross_layer_archive" and not profile.scan_cross_layer_outputs: continue
            if domain == "security_archive" and not profile.scan_security_layers: continue

            items.append(build_archive_item_from_path(path, project_root, profile))
            item_count += 1

        if item_count >= max_items:
            break

    df = pd.DataFrame([archive_item_to_dict(i) for i in items])
    summary = summarize_archive_items(df)
    return df, summary

def summarize_archive_items(item_df: pd.DataFrame) -> Dict:
    if item_df.empty:
        return {"total_items": 0, "total_size_mb": 0.0, "status": "empty"}
    candidates = int((item_df["item_status"] == "archive_candidate").sum())
    excluded = int((item_df["item_status"] == "archive_excluded").sum())
    size = item_df["size_bytes"].sum()
    size_mb = float(size) / (1024 * 1024) if pd.notna(size) else 0.0
    return {
        "total_items": len(item_df),
        "candidates": candidates,
        "excluded": excluded,
        "total_size_mb": round(size_mb, 2),
        "notice": "Item registry works as a local manifest, files are not copied."
    }
