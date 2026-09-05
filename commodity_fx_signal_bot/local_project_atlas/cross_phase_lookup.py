"""Cross-phase lookup engine module."""
import pandas as pd
from pathlib import Path
from .atlas_config import LocalProjectAtlasProfile
from .atlas_models import LookupItem, build_lookup_item_id, lookup_item_to_dict

def build_cross_phase_lookup_engine(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[str, dict]:
    doc = """# Cross-Phase Lookup Engine
This is an offline lookup engine. It is NOT an enterprise search, vector DB, or embedding system.
It maps keywords to script/report families purely based on string matching.
"""
    return doc, {"type": "offline_lookup_doc"}

def build_cross_phase_lookup_registry(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    items = []
    # Sample items
    keys = ["data", "report", "docs", "scripts", "tests", "models", "features"]
    for k in keys:
        item = LookupItem(
            lookup_id=build_lookup_item_id(k, "lookup_docs", f"docs/{k}.md"),
            lookup_key=k,
            lookup_family="lookup_docs",
            source_ref="keyword",
            target_ref=f"docs/{k}.md",
            relation_type="keyword_match",
            warnings=["Not semantic search"]
        )
        items.append(lookup_item_to_dict(item))
    
    df = pd.DataFrame(items)
    return df, summarize_cross_phase_lookup_registry(df)

def query_cross_phase_lookup(registry_df: pd.DataFrame, query_text: str, limit: int = 25) -> pd.DataFrame:
    if registry_df.empty:
        return registry_df
    mask = registry_df["lookup_key"].str.contains(query_text, case=False, na=False)
    return registry_df[mask].head(limit)

def summarize_cross_phase_lookup_registry(df: pd.DataFrame) -> dict:
    return {
        "total_lookups": len(df),
        "families": df["lookup_family"].unique().tolist() if not df.empty else []
    }
