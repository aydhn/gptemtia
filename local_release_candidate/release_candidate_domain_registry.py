import pandas as pd
from pathlib import Path
from local_release_candidate.release_candidate_config import LocalReleaseCandidateProfile
from local_release_candidate.release_candidate_models import *

def build_release_candidate_domain_registry(profile: LocalReleaseCandidateProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {}

def build_default_release_candidate_domains(profile: LocalReleaseCandidateProfile) -> list[ReleaseCandidateDomain]:
    return []

def summarize_release_candidate_domains(domain_df: pd.DataFrame) -> dict:
    return {}

