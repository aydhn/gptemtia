"""Final local meta-index module."""
import os
from pathlib import Path
import pandas as pd
from .atlas_config import LocalProjectAtlasProfile
from .atlas_models import MetaIndexItem, build_meta_index_item_id, meta_index_item_to_dict

def classify_meta_index_item(path: Path, project_root: Path, profile: LocalProjectAtlasProfile) -> dict:
    try:
        rel_path = str(path.relative_to(project_root)).replace("\\", "/")
    except ValueError:
        rel_path = str(path).replace("\\", "/")
        
    item_family = "unknown"
    lookup_family = "lookup_unknown"
    
    if "docs/" in rel_path:
        item_family = "docs"
        lookup_family = "lookup_docs"
    elif "scripts/" in rel_path:
        item_family = "scripts"
        lookup_family = "lookup_scripts"
    elif "reports/" in rel_path:
        item_family = "reports"
        lookup_family = "lookup_reports"
    elif "data/lake/" in rel_path:
        item_family = "datalake"
        lookup_family = "lookup_datalake"
    elif "tests/" in rel_path:
        item_family = "tests"
        lookup_family = "lookup_tests"

    return {
        "title": path.name,
        "item_path": rel_path,
        "item_family": item_family,
        "phase_ref": "various",
        "lookup_family": lookup_family,
        "summary": f"Offline file: {path.name}",
        "exists": path.exists(),
        "size_bytes": path.stat().st_size if path.exists() else 0,
        "manual_review_required": False,
        "warnings": ["Not official knowledge index."]
    }

def discover_meta_index_items(project_root: Path, profile: LocalProjectAtlasProfile) -> pd.DataFrame:
    items = []
    
    for root, dirs, files in os.walk(project_root):
        if ".git" in root or "__pycache__" in root or "venv" in root:
            continue
            
        for file in files:
            p = Path(root) / file
            if not p.is_file():
                continue
            
            info = classify_meta_index_item(p, project_root, profile)
            
            if info["item_family"] == "unknown":
                continue

            item = MetaIndexItem(
                index_id=build_meta_index_item_id(info["item_path"], info["item_family"], info["phase_ref"]),
                title=info["title"],
                item_path=info["item_path"],
                item_family=info["item_family"],
                phase_ref=info["phase_ref"],
                lookup_family=info["lookup_family"],
                summary=info["summary"],
                warnings=info["warnings"]
            )
            
            d = meta_index_item_to_dict(item)
            d["exists"] = info["exists"]
            d["size_bytes"] = info["size_bytes"]
            d["manual_review_required"] = info["manual_review_required"]
            items.append(d)
            
            if len(items) >= profile.max_items:
                break
        if len(items) >= profile.max_items:
            break
            
    return pd.DataFrame(items)

def build_final_local_meta_index(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    df = discover_meta_index_items(project_root, profile)
    summary = summarize_meta_index(df)
    return df, summary

def summarize_meta_index(df: pd.DataFrame) -> dict:
    return {
        "total_items": len(df),
        "total_size_bytes": int(df["size_bytes"].sum()) if not df.empty else 0,
        "families": df["item_family"].unique().tolist() if not df.empty else []
    }

def save_meta_index(df: pd.DataFrame, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    return output_path
