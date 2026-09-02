
import pandas as pd
from pathlib import Path
from local_dr.dr_config import LocalDRProfile

def simulate_config_env_restore_requirements(project_root: Path, profile: LocalDRProfile) -> pd.DataFrame:
    return pd.DataFrame([{"req": "dummy"}])

def detect_config_env_restore_gaps(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"gap": "dummy"}])

def build_config_env_restore_simulation_report(project_root: Path, profile: LocalDRProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame([{"report": "dummy"}]), {"total": 1}

def summarize_config_env_restore_simulation(df: pd.DataFrame) -> dict:
    return {"total": len(df)}
