"""Atlas glossary module."""
import pandas as pd
from .atlas_config import LocalProjectAtlasProfile

def build_default_atlas_glossary_terms(profile: LocalProjectAtlasProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"term": "Meta-Index", "definition": "Offline list of files and families. Not an official knowledge index."},
        {"term": "Atlas", "definition": "Project directory map. Not a cloud search tool."}
    ])

def build_atlas_glossary_index(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_atlas_glossary_terms(profile)
    return df, summarize_atlas_glossary(df)

def summarize_atlas_glossary(df: pd.DataFrame) -> dict:
    return {"terms": len(df)}
