import pandas as pd
from typing import Tuple, Dict
from pathlib import Path
from .synthesis_config import LocalSynthesisProfile

def classify_output_catalog_domain(path: Path, project_root: Path) -> str:
    return "unknown"

def build_end_state_output_catalog(project_root: Path, profile: LocalSynthesisProfile) -> Tuple[pd.DataFrame, Dict]:
    df = pd.DataFrame(columns=["path", "domain", "warnings"])
    return df, summarize_end_state_output_catalog(df)

def summarize_end_state_output_catalog(catalog_df: pd.DataFrame) -> Dict:
    return {"count": len(catalog_df)}
