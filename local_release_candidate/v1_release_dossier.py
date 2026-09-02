import pandas as pd
from pathlib import Path
from local_release_candidate.release_candidate_config import LocalReleaseCandidateProfile
from local_release_candidate.release_candidate_models import *

def build_v1_offline_release_dossier(project_root: Path, profile: LocalReleaseCandidateProfile) -> tuple[str, dict]:
    return 'mock', {}

def build_v1_release_dossier_sections(project_root: Path, profile: LocalReleaseCandidateProfile) -> list[dict]:
    return []

def summarize_v1_release_dossier(text: str) -> dict:
    return {}

def save_v1_release_dossier(text: str, output_path: Path) -> Path:
    return Path('mock')

