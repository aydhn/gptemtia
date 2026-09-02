import pandas as pd
from pathlib import Path
from local_release_candidate.release_candidate_config import LocalReleaseCandidateProfile
from local_release_candidate.release_candidate_models import *

def build_release_candidate_gap_register(domain_df: pd.DataFrame, baseline_df: pd.DataFrame, acceptance_df: pd.DataFrame, signoff_df: pd.DataFrame, profile: LocalReleaseCandidateProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {}

def detect_missing_release_candidate_domains(domain_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def detect_missing_baseline_items(baseline_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def detect_missing_acceptance_criteria(acceptance_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def detect_missing_signoff_items(signoff_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def summarize_release_candidate_gaps(gap_df: pd.DataFrame) -> dict:
    return {}

