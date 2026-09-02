import pandas as pd
from pathlib import Path
from local_release_candidate.release_candidate_config import LocalReleaseCandidateProfile
from local_release_candidate.release_candidate_models import *

def build_final_acceptance_evidence_index(project_root: Path, profile: LocalReleaseCandidateProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {}

def map_final_acceptance_evidence_sources(project_root: Path, profile: LocalReleaseCandidateProfile) -> pd.DataFrame:
    return pd.DataFrame()

def summarize_acceptance_evidence(df: pd.DataFrame) -> dict:
    return {}

