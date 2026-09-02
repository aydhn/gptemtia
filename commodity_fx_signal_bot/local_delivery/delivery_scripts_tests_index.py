import pandas as pd
from pathlib import Path
from local_delivery.delivery_config import LocalDeliveryProfile

def classify_delivery_script_test_safety(path: Path, project_root: Path) -> dict:
    return {"is_safe": True, "notes": "Local script"}

def build_delivery_scripts_tests_index(project_root: Path, profile: LocalDeliveryProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"script_path": "scripts/run_dummy.py"}])
    return df, summarize_delivery_scripts_tests_index(df)

def summarize_delivery_scripts_tests_index(st_df: pd.DataFrame) -> dict:
    return {"total_scripts_tests": len(st_df)}
