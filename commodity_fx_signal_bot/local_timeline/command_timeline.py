"""
Command and script timeline module.
"""

from pathlib import Path
import pandas as pd

from local_timeline.timeline_config import LocalTimelineProfile

def classify_command_script(path: Path, project_root: Path) -> str:
    rel = path.relative_to(project_root).as_posix()
    if rel.startswith("scripts/run_"):
        return "run_script"
    if rel.startswith("scripts/update_"):
        return "update_script"
    return "other_script"

def map_scripts_to_report_outputs(project_root: Path, script_df: pd.DataFrame) -> pd.DataFrame:
    if script_df.empty:
        return pd.DataFrame()
    mapped = script_df.copy()
    mapped['inferred_report_output'] = mapped['relative_path'].apply(
        lambda x: x.replace("scripts/run_", "reports/output/").replace(".py", "") if isinstance(x, str) else None
    )
    return mapped

def build_command_script_evolution_timeline(project_root: Path, profile: LocalTimelineProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"status": "extracted in pipeline"}

def summarize_command_script_timeline(script_df: pd.DataFrame) -> dict:
    if script_df.empty:
        return {"total_script_events": 0}
    return {
        "total_script_events": len(script_df),
        "unique_scripts": script_df['relative_path'].nunique() if 'relative_path' in script_df else 0
    }
