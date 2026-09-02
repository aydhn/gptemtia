
import pandas as pd
from pathlib import Path
from .hardening_config import LocalHardeningProfile

def detect_forbidden_dependency_mentions(project_root: Path, profile: LocalHardeningProfile) -> pd.DataFrame: return pd.DataFrame()
def detect_external_service_dependency_mentions(project_root: Path, profile: LocalHardeningProfile) -> pd.DataFrame: return pd.DataFrame()
def summarize_dependency_boundary(dep_df: pd.DataFrame) -> dict: return {"total": len(dep_df)}
def build_final_dependency_boundary_report(project_root: Path, profile: LocalHardeningProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame()
    return df, summarize_dependency_boundary(df)
