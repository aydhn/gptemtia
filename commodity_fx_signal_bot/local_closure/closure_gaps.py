
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def detect_missing_closure_domains(domain_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def detect_missing_lessons(lessons_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def detect_missing_roadmap_items(roadmap_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def detect_missing_unresolved_items(unresolved_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def build_closure_gap_register(
    domain_df: pd.DataFrame,
    lessons_df: pd.DataFrame,
    roadmap_df: pd.DataFrame,
    unresolved_df: pd.DataFrame,
    profile: LocalClosureProfile,
) -> tuple[pd.DataFrame, dict]:
    gaps = pd.DataFrame([{"gap": "None", "type": "info"}])
    summary = summarize_closure_gaps(gaps)
    return gaps, summary

def summarize_closure_gaps(gap_df: pd.DataFrame) -> dict:
    return {"total": len(gap_df)}
