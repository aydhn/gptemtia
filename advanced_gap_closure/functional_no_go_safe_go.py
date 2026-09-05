import pandas as pd
from .gap_closure_config import FunctionalGapClosureProfile

def build_functional_no_go_conditions(profile: FunctionalGapClosureProfile) -> pd.DataFrame:
    return pd.DataFrame([{"condition": "live trading"}, {"condition": "scraping"}])

def build_functional_safe_go_conditions(profile: FunctionalGapClosureProfile) -> pd.DataFrame:
    return pd.DataFrame([{"condition": "local/offline gap closure"}, {"condition": "manual review"}])

def build_functional_no_go_safe_go_boundary(profile: FunctionalGapClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"type": "boundary"}])
    return df, summarize_functional_no_go_safe_go(df)

def summarize_functional_no_go_safe_go(df: pd.DataFrame) -> dict: return {"total": len(df)}
