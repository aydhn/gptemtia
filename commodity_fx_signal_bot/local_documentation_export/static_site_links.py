"""Static site links."""
import pandas as pd
from .export_config import LocalDocumentationExportProfile

def build_static_site_link_map(profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"source": "index.html", "target": "about.html"}])
    return df, summarize_static_site_links(df)

def build_static_site_broken_link_rehearsal(link_df: pd.DataFrame, profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    df = link_df.copy()
    df["broken"] = False
    return df, summarize_static_site_links(df)

def summarize_static_site_links(df: pd.DataFrame) -> dict:
    return {"count": len(df)}
