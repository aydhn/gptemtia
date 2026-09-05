import pandas as pd
from .gap_closure_config import FunctionalGapClosureProfile

def build_no_scraping_allowed_patterns(profile: FunctionalGapClosureProfile) -> pd.DataFrame:
    return pd.DataFrame([{"pattern": "official API adapter"}, {"pattern": "user-provided CSV/parquet import"}])

def build_no_scraping_forbidden_patterns(profile: FunctionalGapClosureProfile) -> pd.DataFrame:
    return pd.DataFrame([{"pattern": "HTML scraping"}, {"pattern": "bypassing paywall"}])

def build_no_scraping_data_integration_boundary(profile: FunctionalGapClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"boundary": "no-scraping"}])
    return df, summarize_no_scraping_boundary(df)

def summarize_no_scraping_boundary(df: pd.DataFrame) -> dict: return {"total": len(df)}
