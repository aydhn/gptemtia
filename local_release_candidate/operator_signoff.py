import pandas as pd
from pathlib import Path
from local_release_candidate.release_candidate_config import LocalReleaseCandidateProfile
from local_release_candidate.release_candidate_models import *

def build_operator_signoff_packet(profile: LocalReleaseCandidateProfile) -> tuple[str, dict]:
    return 'mock', {}

def build_operator_signoff_sections(profile: LocalReleaseCandidateProfile) -> list[dict]:
    return []

def build_operator_signoff_checklist_registry(profile: LocalReleaseCandidateProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {}

def build_default_operator_signoff_items(profile: LocalReleaseCandidateProfile) -> list[OperatorSignoffItem]:
    return []

def summarize_operator_signoff_packet(text: str) -> dict:
    return {}

def summarize_operator_signoff_checklist(df: pd.DataFrame) -> dict:
    return {}

