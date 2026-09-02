import pandas as pd
from typing import Tuple, Dict
from pathlib import Path
from .synthesis_config import LocalSynthesisProfile

def build_default_final_limitations(profile: LocalSynthesisProfile) -> pd.DataFrame:
    return pd.DataFrame([{"limitation": "offline/local only"}, {"limitation": "no live trading"}])

def build_final_limitation_register(project_root: Path, profile: LocalSynthesisProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_final_limitations(profile)
    return df, summarize_final_limitation_register(df)

def summarize_final_limitation_register(limit_df: pd.DataFrame) -> Dict:
    return {"count": len(limit_df)}
