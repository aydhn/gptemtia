import pandas as pd
from pathlib import Path
from local_release_candidate.release_candidate_config import LocalReleaseCandidateProfile
from local_release_candidate.release_candidate_models import *

def build_release_candidate_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame | None = None) -> str:
    return 'mock'

def build_release_candidate_packet_markdown_report(summary: dict, packet_text: str | None = None) -> str:
    return 'mock'

def build_frozen_baseline_snapshot_markdown_report(summary: dict, baseline_df: pd.DataFrame | None = None) -> str:
    return 'mock'

def build_final_acceptance_rehearsal_markdown_report(summary: dict, acceptance_text: str | None = None) -> str:
    return 'mock'

def build_operator_signoff_markdown_report(summary: dict, signoff_text: str | None = None) -> str:
    return 'mock'

def build_v1_release_dossier_markdown_report(summary: dict, dossier_text: str | None = None) -> str:
    return 'mock'

def build_release_candidate_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    return 'mock'

def build_release_candidate_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    return 'mock'

def build_release_candidate_disclaimer() -> str:
    return 'mock'

