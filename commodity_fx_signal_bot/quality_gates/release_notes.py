import pandas as pd
from pathlib import Path

def collect_phase_summaries(project_root: Path) -> pd.DataFrame:
    return pd.DataFrame()

def build_release_notes_draft(manifest: dict, checklist_df: pd.DataFrame, phase_summary_df: pd.DataFrame | None = None) -> str:
    return "Draft"

def build_known_limitations_section(quality_summary: dict) -> str:
    return "Limitations"

def build_safety_boundaries_section() -> str:
    return "Safety"

def save_release_notes_draft(text: str, output_path: Path) -> Path:
    return output_path
