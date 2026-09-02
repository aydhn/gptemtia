import pandas as pd
from typing import Tuple, Dict
from .synthesis_config import LocalSynthesisProfile

def build_final_boundary_rows(profile: LocalSynthesisProfile) -> pd.DataFrame:
    return pd.DataFrame([{"boundary": "no live trading"}, {"boundary": "no broker execution"}, {"boundary": "no investment advice"}])

def build_end_state_boundary_map(profile: LocalSynthesisProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_final_boundary_rows(profile)
    return df, summarize_end_state_boundary_map(df)

def summarize_end_state_boundary_map(boundary_df: pd.DataFrame) -> Dict:
    return {"count": len(boundary_df)}
