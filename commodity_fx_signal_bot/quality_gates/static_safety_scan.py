import pandas as pd
from pathlib import Path

def scan_file_for_forbidden_terms(path: Path) -> dict:
    return {"forbidden": []}

def scan_project_for_forbidden_terms(project_root: Path) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {}

def scan_for_network_call_patterns(project_root: Path) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {}

def scan_for_background_loop_patterns(project_root: Path) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {}

def scan_for_broker_execution_patterns(project_root: Path) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {}

def build_static_safety_report(project_root: Path) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {}
