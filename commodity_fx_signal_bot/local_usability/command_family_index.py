import pandas as pd
from pathlib import Path
from .usability_config import LocalUsabilityProfile

def classify_command_family(script_name: str) -> str:
    return "status"

def build_command_family_index(project_root: Path, profile: LocalUsabilityProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"script": "run_usability_domain_registry", "family": "usability"}])
    return df, {"total_commands": len(df)}

def summarize_command_family_index(index_df: pd.DataFrame) -> dict:
    return {"total": len(index_df)}
