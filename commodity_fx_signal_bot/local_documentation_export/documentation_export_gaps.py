"""Export gaps."""
import pandas as pd
from .export_config import LocalDocumentationExportProfile

def build_documentation_export_gap_register(domain_df: pd.DataFrame, page_df: pd.DataFrame, binder_df: pd.DataFrame, route_df: pd.DataFrame, profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    gaps = []
    gaps.append(detect_missing_documentation_export_domains(domain_df))
    gaps.append(detect_missing_static_pages(page_df))
    gaps.append(detect_missing_binder_items(binder_df))
    gaps.append(detect_missing_documentation_routes(route_df))
    
    df = pd.concat(gaps, ignore_index=True) if gaps else pd.DataFrame(columns=["gap_id", "description"])
    return df, summarize_documentation_export_gaps(df)

def detect_missing_documentation_export_domains(domain_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(columns=["gap_id", "description"])

def detect_missing_static_pages(page_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(columns=["gap_id", "description"])

def detect_missing_binder_items(binder_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(columns=["gap_id", "description"])

def detect_missing_documentation_routes(route_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(columns=["gap_id", "description"])

def summarize_documentation_export_gaps(gap_df: pd.DataFrame) -> dict:
    return {"count": len(gap_df)}
