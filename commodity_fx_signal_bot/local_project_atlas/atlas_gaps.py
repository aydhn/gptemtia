"""Atlas gaps module."""
import pandas as pd
from .atlas_config import LocalProjectAtlasProfile

def detect_missing_atlas_domains(domain_df: pd.DataFrame) -> pd.DataFrame: return pd.DataFrame()
def detect_missing_meta_index_items(meta_df: pd.DataFrame) -> pd.DataFrame: return pd.DataFrame()
def detect_missing_lookup_items(lookup_df: pd.DataFrame) -> pd.DataFrame: return pd.DataFrame()
def detect_missing_navigation_items(nav_df: pd.DataFrame) -> pd.DataFrame: return pd.DataFrame()

def build_meta_index_gap_register(
    domain_df: pd.DataFrame, meta_df: pd.DataFrame, lookup_df: pd.DataFrame, nav_df: pd.DataFrame, profile: LocalProjectAtlasProfile
) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"gap": "none"}])
    return df, summarize_meta_index_gaps(df)

def summarize_meta_index_gaps(gap_df: pd.DataFrame) -> dict:
    return {"gaps": len(gap_df)}
