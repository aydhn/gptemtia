from pathlib import Path

import pandas as pd

from local_consistency.consistency_config import LocalConsistencyProfile


def discover_report_outputs(project_root: Path) -> pd.DataFrame:
    return pd.DataFrame()

def discover_datalake_outputs(project_root: Path) -> pd.DataFrame:
    return pd.DataFrame()

def compare_reports_to_datalake(report_df: pd.DataFrame, datalake_df: pd.DataFrame, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"warnings": []}

def detect_report_without_datalake_counterpart(report_df: pd.DataFrame, datalake_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def detect_datalake_without_report_counterpart(report_df: pd.DataFrame, datalake_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def build_report_datalake_consistency_report(project_root: Path, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    report_df = discover_report_outputs(project_root)
    datalake_df = discover_datalake_outputs(project_root)
    return compare_reports_to_datalake(report_df, datalake_df, profile)
