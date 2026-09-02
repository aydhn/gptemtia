import pandas as pd
from pathlib import Path
from local_release_candidate.release_candidate_config import LocalReleaseCandidateProfile
from local_release_candidate.release_candidate_models import *

def build_frozen_baseline_snapshot_registry(project_root: Path, profile: LocalReleaseCandidateProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {}

def build_frozen_baseline_snapshot_summary(project_root: Path, profile: LocalReleaseCandidateProfile) -> dict:
    return {}

def summarize_frozen_baseline_snapshot(df: pd.DataFrame) -> dict:
    return {}

