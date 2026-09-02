import pandas as pd
from pathlib import Path
from local_release_candidate.release_candidate_config import LocalReleaseCandidateProfile
from local_release_candidate.release_candidate_models import *

def build_baseline_drift_warning_registry(inventory_df: pd.DataFrame, hash_df: pd.DataFrame, profile: LocalReleaseCandidateProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {}

def detect_baseline_drift_warnings(inventory_df: pd.DataFrame, hash_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def summarize_baseline_drift_warnings(df: pd.DataFrame) -> dict:
    return {}

