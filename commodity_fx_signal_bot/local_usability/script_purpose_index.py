import pandas as pd
from pathlib import Path
from .usability_config import LocalUsabilityProfile

def infer_script_purpose(script_name: str, profile: LocalUsabilityProfile) -> dict:
    return {"script": script_name, "purpose": "usability review", "warnings": ["best-effort"]}

def build_script_purpose_index(project_root: Path, profile: LocalUsabilityProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([infer_script_purpose("run_usability_domain_registry", profile)])
    return df, {"total_scripts": len(df)}

def summarize_script_purpose_index(index_df: pd.DataFrame) -> dict:
    return {"total": len(index_df)}
