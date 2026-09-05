"""Atlas family maps module."""
import pandas as pd
from pathlib import Path
from .atlas_config import LocalProjectAtlasProfile

def _build_dummy_map(name: str) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"family": name, "status": "mapped"}])
    return df, summarize_atlas_family_map(df)

def build_atlas_module_family_map(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_dummy_map("module")

def build_atlas_script_family_map(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_dummy_map("script")

def build_atlas_report_family_map(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_dummy_map("report")

def build_atlas_datalake_family_map(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_dummy_map("datalake")

def build_atlas_docs_family_map(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_dummy_map("docs")

def build_atlas_generated_docs_family_map(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_dummy_map("generated_docs")

def summarize_atlas_family_map(df: pd.DataFrame) -> dict:
    return {"count": len(df)}
