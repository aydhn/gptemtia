import pandas as pd
from pathlib import Path
from .completion_config import LocalProjectCompletionProfile

def discover_final_inventory_items(project_root: Path, base_path: Path, item_kind: str, profile: LocalProjectCompletionProfile) -> pd.DataFrame:
    return pd.DataFrame([{"item_name": "mock", "item_path": "mock", "item_kind": item_kind}])

def summarize_final_inventory(df: pd.DataFrame) -> dict:
    if len(df) > 250000:
        return {"items": len(df), "warning": "Max inventory sınırı aşıldı."}
    return {"items": len(df), "note": "Read-only inventory."}

def build_final_module_inventory(project_root: Path, profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    df = discover_final_inventory_items(project_root, project_root, "module", profile)
    return df, summarize_final_inventory(df)

def build_final_script_inventory(project_root: Path, profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    df = discover_final_inventory_items(project_root, project_root / "scripts", "script", profile)
    return df, summarize_final_inventory(df)

def build_final_docs_inventory(project_root: Path, profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    df = discover_final_inventory_items(project_root, project_root / "docs", "doc", profile)
    return df, summarize_final_inventory(df)

def build_final_reports_inventory(project_root: Path, profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    df = discover_final_inventory_items(project_root, project_root / "reports", "report", profile)
    return df, summarize_final_inventory(df)

def build_final_datalake_inventory(project_root: Path, profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    df = discover_final_inventory_items(project_root, project_root / "data" / "lake", "datalake", profile)
    return df, summarize_final_inventory(df)

def build_final_generated_docs_inventory(project_root: Path, profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    df = discover_final_inventory_items(project_root, project_root / "docs" / "generated", "generated_doc", profile)
    return df, summarize_final_inventory(df)

def build_final_test_inventory(project_root: Path, profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    df = discover_final_inventory_items(project_root, project_root / "tests", "test", profile)
    return df, summarize_final_inventory(df)
