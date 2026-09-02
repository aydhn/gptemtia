import pandas as pd
from pathlib import Path
from local_release_candidate.release_candidate_config import LocalReleaseCandidateProfile
from local_release_candidate.release_candidate_models import *

def build_baseline_reproducibility_checklist(profile: LocalReleaseCandidateProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {}

def build_default_reproducibility_items(profile: LocalReleaseCandidateProfile) -> pd.DataFrame:
    return pd.DataFrame()

def summarize_baseline_reproducibility(df: pd.DataFrame) -> dict:
    return {}

