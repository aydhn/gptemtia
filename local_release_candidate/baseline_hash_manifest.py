import pandas as pd
from pathlib import Path
from local_release_candidate.release_candidate_config import LocalReleaseCandidateProfile
from local_release_candidate.release_candidate_models import *

def build_baseline_hash_manifest_rehearsal(project_root: Path, profile: LocalReleaseCandidateProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {}

def compute_rehearsal_hash_for_file(path: Path, project_root: Path, profile: LocalReleaseCandidateProfile) -> dict:
    return {}

def summarize_baseline_hash_manifest(df: pd.DataFrame) -> dict:
    return {}

