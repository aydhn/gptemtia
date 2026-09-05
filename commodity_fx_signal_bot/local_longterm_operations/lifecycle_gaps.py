"""Lifecycle gaps."""
import pandas as pd
from .longterm_config import LocalLongTermOperationsProfile

def detect_missing_lifecycle_domains(domain_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def detect_missing_calendar_items(calendar_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def detect_missing_workbook_items(workbook_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def detect_missing_roadmap_items(roadmap_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def build_lifecycle_gap_register(domain_df: pd.DataFrame, calendar_df: pd.DataFrame, workbook_df: pd.DataFrame, roadmap_df: pd.DataFrame, profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    df1 = detect_missing_lifecycle_domains(domain_df)
    df2 = detect_missing_calendar_items(calendar_df)
    df3 = detect_missing_workbook_items(workbook_df)
    df4 = detect_missing_roadmap_items(roadmap_df)
    df = pd.concat([df1, df2, df3, df4], ignore_index=True) if not all(x.empty for x in [df1, df2, df3, df4]) else pd.DataFrame([{"gap": "none", "warnings": ["auto-fix yoktur"]}])
    return df, summarize_lifecycle_gaps(df)

def summarize_lifecycle_gaps(gap_df: pd.DataFrame) -> dict:
    return {"total_items": len(gap_df)}
