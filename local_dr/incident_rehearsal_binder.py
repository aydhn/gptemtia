import pandas as pd
from pathlib import Path
from local_dr.profile import LocalDRProfile

def build_incident_rehearsal_binder(scenario_df: pd.DataFrame, drill_df: pd.DataFrame, failure_df: pd.DataFrame, profile: LocalDRProfile) -> tuple[str, dict]:
    return "Binder Content", {"status": "ok"}

def build_incident_rehearsal_sections(scenario_df: pd.DataFrame, drill_df: pd.DataFrame, failure_df: pd.DataFrame) -> list[dict]:
    return [{"section": "scenarios"}, {"section": "drills"}]

def save_incident_rehearsal_binder(text: str, output_path: Path) -> Path:
    output_path.write_text(text)
    return output_path

def summarize_incident_rehearsal_binder(binder_text: str) -> dict:
    return {"summary": "binder done"}
