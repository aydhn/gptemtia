import pandas as pd
from pathlib import Path
from local_release_candidate.release_candidate_config import LocalReleaseCandidateProfile
from local_release_candidate.release_candidate_models import *

def build_release_candidate_exception_register(baseline_df: pd.DataFrame, acceptance_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalReleaseCandidateProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {}

def detect_release_candidate_exceptions(baseline_df: pd.DataFrame, acceptance_df: pd.DataFrame, no_go_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def summarize_release_candidate_exceptions(exception_df: pd.DataFrame) -> dict:
    return {}

