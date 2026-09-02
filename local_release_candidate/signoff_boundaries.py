import pandas as pd
from pathlib import Path
from local_release_candidate.release_candidate_config import LocalReleaseCandidateProfile
from local_release_candidate.release_candidate_models import *

def build_operator_signoff_boundary_registry(profile: LocalReleaseCandidateProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {}

def build_non_signoff_boundary_registry(profile: LocalReleaseCandidateProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {}

def build_default_signoff_boundaries(profile: LocalReleaseCandidateProfile) -> pd.DataFrame:
    return pd.DataFrame()

def build_default_non_signoff_boundaries(profile: LocalReleaseCandidateProfile) -> pd.DataFrame:
    return pd.DataFrame()

def summarize_signoff_boundaries(signoff_df: pd.DataFrame, non_signoff_df: pd.DataFrame) -> dict:
    return {}

