import pandas as pd
from typing import Tuple, Dict
from pathlib import Path
from .synthesis_config import LocalSynthesisProfile

def collect_manual_review_items_from_final_layers(project_root: Path, profile: LocalSynthesisProfile) -> pd.DataFrame:
    return pd.DataFrame(columns=["item", "reason"])

def build_final_manual_review_register(project_root: Path, profile: LocalSynthesisProfile) -> Tuple[pd.DataFrame, Dict]:
    df = collect_manual_review_items_from_final_layers(project_root, profile)
    return df, summarize_final_manual_review_register(df)

def summarize_final_manual_review_register(review_df: pd.DataFrame) -> Dict:
    return {"count": len(review_df)}
