import pandas as pd
from pathlib import Path
from local_release_candidate.release_candidate_config import LocalReleaseCandidateProfile
from local_release_candidate.release_candidate_models import *

def build_v1_known_limitations_registry(profile: LocalReleaseCandidateProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {}

def build_v1_unresolved_items_registry(profile: LocalReleaseCandidateProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {}

def build_default_known_limitations(profile: LocalReleaseCandidateProfile) -> pd.DataFrame:
    return pd.DataFrame()

def build_default_unresolved_items(profile: LocalReleaseCandidateProfile) -> pd.DataFrame:
    return pd.DataFrame()

def summarize_v1_known_limitations(limit_df: pd.DataFrame, unresolved_df: pd.DataFrame) -> dict:
    return {}

