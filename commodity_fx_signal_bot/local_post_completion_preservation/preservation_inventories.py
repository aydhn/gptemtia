import pandas as pd
from pathlib import Path
from local_post_completion_preservation.preservation_config import LocalPostCompletionPreservationProfile

def discover_preservation_inventory_items(project_root: Path, base_path: Path, item_kind: str, profile: LocalPostCompletionPreservationProfile) -> pd.DataFrame:
    return pd.DataFrame([{"path": str(base_path), "kind": item_kind}])

def build_preservation_inventory_registry(project_root: Path, profile: LocalPostCompletionPreservationProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"item": "registry"}])
    return df, summarize_preservation_inventory(df)

def build_preservation_final_docs_inventory(project_root: Path, profile: LocalPostCompletionPreservationProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"item": "docs"}])
    return df, summarize_preservation_inventory(df)

def build_preservation_final_reports_inventory(project_root: Path, profile: LocalPostCompletionPreservationProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"item": "reports"}])
    return df, summarize_preservation_inventory(df)

def build_preservation_final_datalake_inventory(project_root: Path, profile: LocalPostCompletionPreservationProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"item": "datalake"}])
    return df, summarize_preservation_inventory(df)

def build_preservation_final_scripts_inventory(project_root: Path, profile: LocalPostCompletionPreservationProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"item": "scripts"}])
    return df, summarize_preservation_inventory(df)

def build_preservation_final_tests_inventory(project_root: Path, profile: LocalPostCompletionPreservationProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"item": "tests"}])
    return df, summarize_preservation_inventory(df)

def build_preservation_generated_docs_inventory(project_root: Path, profile: LocalPostCompletionPreservationProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"item": "generated_docs"}])
    return df, summarize_preservation_inventory(df)

def summarize_preservation_inventory(df: pd.DataFrame) -> dict:
    return {"count": len(df)}
