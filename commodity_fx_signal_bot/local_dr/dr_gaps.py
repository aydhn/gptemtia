
import pandas as pd
from local_dr.dr_config import LocalDRProfile

def detect_missing_dr_domains(scenario_df: pd.DataFrame, drill_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()
def detect_missing_restore_prerequisites(drill_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()
def detect_missing_playbooks(scenario_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()
def detect_missing_traceability(trace_df: pd.DataFrame | None) -> pd.DataFrame:
    return pd.DataFrame()

def build_dr_gap_register(scenario_df: pd.DataFrame, drill_df: pd.DataFrame, trace_df: pd.DataFrame | None, restore_df: pd.DataFrame | None, profile: LocalDRProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame([{"gap": "missing"}]), {"total": 1}

def summarize_dr_gaps(gap_df: pd.DataFrame) -> dict:
    return {"total": len(gap_df)}
