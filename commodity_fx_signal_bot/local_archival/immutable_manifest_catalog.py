"""
Immutable Manifest Rehearsal Catalog.
"""
import pandas as pd
from local_archival.archival_config import LocalArchivalProfile

def build_immutable_manifest_entries(manifest: dict, hash_df: pd.DataFrame, profile: LocalArchivalProfile) -> pd.DataFrame:
    df = hash_df.copy()
    if not df.empty:
        df["immutable_manifest_note"] = "dry-run rehearsal"
    return df

def build_immutable_manifest_rehearsal_catalog(manifest: dict, hash_df: pd.DataFrame, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    df = build_immutable_manifest_entries(manifest, hash_df, profile)
    return df, summarize_immutable_manifest_catalog(df)

def summarize_immutable_manifest_catalog(catalog_df: pd.DataFrame) -> dict:
    return {"catalog_entries": len(catalog_df) if catalog_df is not None else 0}
