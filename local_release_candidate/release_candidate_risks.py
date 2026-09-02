import pandas as pd
from pathlib import Path
from local_release_candidate.release_candidate_config import LocalReleaseCandidateProfile
from local_release_candidate.release_candidate_models import *

def build_release_candidate_risk_summary(exception_df: pd.DataFrame, gap_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalReleaseCandidateProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {}

def classify_release_candidate_risk(row: pd.Series, profile: LocalReleaseCandidateProfile) -> str:
    return 'mock'

def build_release_candidate_risk_digest(risk_df: pd.DataFrame, profile: LocalReleaseCandidateProfile) -> tuple[str, dict]:
    return 'mock', {}

def summarize_release_candidate_risks(risk_df: pd.DataFrame) -> dict:
    return {}

