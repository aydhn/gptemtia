import pandas as pd
from typing import Tuple, Dict
from pathlib import Path
from .synthesis_config import LocalSynthesisProfile

def build_final_no_go_conditions(profile: LocalSynthesisProfile) -> pd.DataFrame:
    return pd.DataFrame([{"condition": "raw secret output"}, {"condition": "live/broker/deploy claim"}])

def build_final_safe_go_conditions(profile: LocalSynthesisProfile) -> pd.DataFrame:
    return pd.DataFrame([{"condition": "local-only scope documented"}])

def build_final_no_go_safe_go_summary(project_root: Path, profile: LocalSynthesisProfile) -> Tuple[pd.DataFrame, Dict]:
    nogo = build_final_no_go_conditions(profile)
    safego = build_final_safe_go_conditions(profile)
    df = pd.concat([nogo, safego], ignore_index=True)
    return df, summarize_final_no_go_safe_go(df)

def summarize_final_no_go_safe_go(summary_df: pd.DataFrame) -> Dict:
    return {"count": len(summary_df)}
