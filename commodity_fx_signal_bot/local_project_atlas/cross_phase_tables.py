"""Cross-phase lookup tables module."""
import pandas as pd
from pathlib import Path
from .atlas_config import LocalProjectAtlasProfile

def _build_dummy_table(name: str) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"id": f"dummy_{name}", "note": f"{name} placeholder"}])
    return df, summarize_cross_phase_table(df)

def build_cross_phase_output_lookup_table(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_dummy_table("output")

def build_cross_phase_script_lookup_table(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_dummy_table("script")

def build_cross_phase_docs_lookup_table(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_dummy_table("docs")

def build_cross_phase_datalake_lookup_table(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_dummy_table("datalake")

def build_cross_phase_report_lookup_table(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_dummy_table("report")

def build_cross_phase_generated_docs_lookup_table(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_dummy_table("generated_docs")

def build_cross_phase_safety_boundary_lookup_table(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_dummy_table("safety_boundary")

def summarize_cross_phase_table(df: pd.DataFrame) -> dict:
    return {"total_rows": len(df)}
