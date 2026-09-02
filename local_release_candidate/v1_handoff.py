import pandas as pd
from pathlib import Path
from local_release_candidate.release_candidate_config import LocalReleaseCandidateProfile
from local_release_candidate.release_candidate_models import *

def build_v1_handoff_checklist(profile: LocalReleaseCandidateProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {}

def build_default_v1_handoff_items(profile: LocalReleaseCandidateProfile) -> pd.DataFrame:
    return pd.DataFrame()

def summarize_v1_handoff(df: pd.DataFrame) -> dict:
    return {}

