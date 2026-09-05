"""Presentation freeze maps."""
import pandas as pd
from .export_config import LocalDocumentationExportProfile

def build_presentation_freeze_section_registry(profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"section": "introduction"}])
    return df, summarize_presentation_freeze_map(df)

def build_presentation_freeze_snapshot_index(profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"snapshot": "v1.0.0-rehearsal"}])
    return df, summarize_presentation_freeze_map(df)

def build_presentation_freeze_narrative_map(profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"narrative": "System Architecture"}])
    return df, summarize_presentation_freeze_map(df)

def build_presentation_freeze_non_goals_registry(profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([
        {"non_goal": "no slides generation"},
        {"non_goal": "no PowerPoint export"},
        {"non_goal": "no Canva/Figma export"},
        {"non_goal": "no presentation publishing"},
        {"non_goal": "no official investor deck"},
        {"non_goal": "no legal/compliance deck"},
        {"non_goal": "no production approval deck"},
        {"non_goal": "no investment advice"}
    ])
    return df, summarize_presentation_freeze_map(df)

def summarize_presentation_freeze_map(df: pd.DataFrame) -> dict:
    return {"count": len(df)}
