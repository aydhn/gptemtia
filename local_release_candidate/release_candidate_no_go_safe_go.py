import pandas as pd
from pathlib import Path
from local_release_candidate.release_candidate_config import LocalReleaseCandidateProfile
from local_release_candidate.release_candidate_models import *

def build_release_candidate_no_go_safe_go_summary(profile: LocalReleaseCandidateProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {}

def build_release_candidate_no_go_conditions(profile: LocalReleaseCandidateProfile) -> pd.DataFrame:
    return pd.DataFrame()

def build_release_candidate_safe_go_conditions(profile: LocalReleaseCandidateProfile) -> pd.DataFrame:
    return pd.DataFrame()

def summarize_release_candidate_no_go_safe_go(summary_df: pd.DataFrame) -> dict:
    return {}

