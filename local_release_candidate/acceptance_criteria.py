import pandas as pd
from pathlib import Path
from local_release_candidate.release_candidate_config import LocalReleaseCandidateProfile
from local_release_candidate.release_candidate_models import *

def build_final_acceptance_criteria_matrix(profile: LocalReleaseCandidateProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {}

def build_default_acceptance_criteria(profile: LocalReleaseCandidateProfile) -> list[AcceptanceCriterion]:
    return []

def summarize_acceptance_criteria(df: pd.DataFrame) -> dict:
    return {}

