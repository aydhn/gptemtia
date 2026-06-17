"""
Scenario regression event timeline module.
"""

from pathlib import Path
import pandas as pd

from local_timeline.timeline_config import LocalTimelineProfile

def classify_scenario_regression_event(path: Path, project_root: Path) -> str:
    return "regression_update"

def link_scenario_events_to_regression_outputs(project_root: Path, scenario_df: pd.DataFrame) -> pd.DataFrame:
    if scenario_df.empty:
        return pd.DataFrame()
    mapped = scenario_df.copy()
    mapped['linked_output'] = "inferred_output"
    return mapped

def build_scenario_regression_event_timeline(project_root: Path, profile: LocalTimelineProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"status": "extracted in pipeline"}

def summarize_scenario_regression_timeline(scenario_df: pd.DataFrame) -> dict:
    if scenario_df.empty:
        return {"total_scenario_events": 0}
    return {
        "total_scenario_events": len(scenario_df),
        "unique_scenario_files": scenario_df['relative_path'].nunique() if 'relative_path' in scenario_df else 0
    }
