"""Atlas phase maps module."""
import pandas as pd
from .atlas_config import LocalProjectAtlasProfile

def build_default_phase_dependencies(profile: LocalProjectAtlasProfile) -> pd.DataFrame:
    return pd.DataFrame([{"phase": "phase93", "depends_on": "phase92"}])

def build_default_phase_output_items(profile: LocalProjectAtlasProfile) -> pd.DataFrame:
    return pd.DataFrame([{"phase": "phase93", "outputs": "atlas"}])

def build_atlas_phase_dependency_map(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_phase_dependencies(profile)
    return df, summarize_atlas_phase_map(df)

def build_atlas_phase_to_output_map(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_phase_output_items(profile)
    return df, summarize_atlas_phase_map(df)

def build_atlas_output_to_script_map(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"output": "atlas", "script": "run_final_meta_index"}])
    return df, summarize_atlas_phase_map(df)

def build_atlas_command_to_output_map(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"command": "python run_final_meta_index", "output": "atlas"}])
    return df, summarize_atlas_phase_map(df)

def summarize_atlas_phase_map(df: pd.DataFrame) -> dict:
    return {"entries": len(df)}
