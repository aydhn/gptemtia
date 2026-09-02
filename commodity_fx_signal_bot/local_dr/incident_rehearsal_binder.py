
import pandas as pd
from pathlib import Path
from local_dr.dr_config import LocalDRProfile

def build_incident_rehearsal_sections(scenario_df: pd.DataFrame, drill_df: pd.DataFrame, failure_df: pd.DataFrame) -> list[dict]:
    return [{"section": "dummy"}]

def build_incident_rehearsal_binder(scenario_df: pd.DataFrame, drill_df: pd.DataFrame, failure_df: pd.DataFrame, profile: LocalDRProfile) -> tuple[str, dict]:
    return "Incident Rehearsal Binder", {"total": 1}

def save_incident_rehearsal_binder(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text, encoding="utf-8")
    return output_path

def summarize_incident_rehearsal_binder(binder_text: str) -> dict:
    return {"len": len(binder_text)}
