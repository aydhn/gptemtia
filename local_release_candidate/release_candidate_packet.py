import pandas as pd
from pathlib import Path
from local_release_candidate.release_candidate_config import LocalReleaseCandidateProfile
from local_release_candidate.release_candidate_models import *

def build_final_local_release_candidate_rehearsal_packet(project_root: Path, profile: LocalReleaseCandidateProfile) -> tuple[str, dict]:
    return 'mock', {}

def build_release_candidate_rehearsal_sections(project_root: Path, profile: LocalReleaseCandidateProfile) -> list[dict]:
    return []

def summarize_release_candidate_rehearsal_packet(text: str) -> dict:
    return {}

def save_release_candidate_rehearsal_packet(text: str, output_path: Path) -> Path:
    return Path('mock')

