import pandas as pd
from typing import Tuple, Dict, Optional
from pathlib import Path
from .synthesis_config import LocalSynthesisProfile

def build_capability_summary_rows(profile: LocalSynthesisProfile) -> pd.DataFrame:
    return pd.DataFrame(columns=["capability", "description", "warnings"])

def map_capabilities_to_phase_families(capability_df: pd.DataFrame, family_df: Optional[pd.DataFrame] = None) -> pd.DataFrame:
    return capability_df

def build_end_state_capability_map(project_root: Path, profile: LocalSynthesisProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_capability_summary_rows(profile)
    return df, summarize_end_state_capability_map(df)

def summarize_end_state_capability_map(capability_df: pd.DataFrame) -> Dict:
    return {"count": len(capability_df)}
