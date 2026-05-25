import pandas as pd
from pathlib import Path

def discover_requirement_files(project_root: Path) -> pd.DataFrame:
    return pd.DataFrame()

def parse_requirements_file(path: Path) -> pd.DataFrame:
    return pd.DataFrame()

def collect_imported_external_packages(project_root: Path) -> pd.DataFrame:
    return pd.DataFrame()

def compare_imports_to_requirements(imports_df: pd.DataFrame, requirements_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def build_optional_dependency_map(project_root: Path) -> pd.DataFrame:
    return pd.DataFrame()

def build_dependency_audit_report(project_root: Path) -> tuple[dict[str, pd.DataFrame], dict]:
    return {}, {}
