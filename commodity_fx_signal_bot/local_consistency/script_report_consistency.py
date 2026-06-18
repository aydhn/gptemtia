from pathlib import Path

import pandas as pd

from local_consistency.consistency_config import LocalConsistencyProfile


def discover_scripts(project_root: Path) -> pd.DataFrame:
    return pd.DataFrame()

def infer_expected_reports_from_scripts(script_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def compare_scripts_to_report_outputs(script_df: pd.DataFrame, expected_df: pd.DataFrame, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"warnings": []}

def detect_script_without_documented_outputs(script_df: pd.DataFrame, expected_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def build_script_report_consistency_report(project_root: Path, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    script_df = discover_scripts(project_root)
    expected_df = infer_expected_reports_from_scripts(script_df)
    return compare_scripts_to_report_outputs(script_df, expected_df, profile)
