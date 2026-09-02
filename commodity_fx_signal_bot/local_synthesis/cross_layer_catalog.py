import pandas as pd
from typing import Tuple, Dict
from pathlib import Path
from .synthesis_config import LocalSynthesisProfile


def build_final_cross_layer_catalog(project_root: Path, profile: LocalSynthesisProfile) -> Tuple[pd.DataFrame, Dict]:
    df = pd.DataFrame(columns=["item", "info"])
    return df, summarize_final_cross_layer_catalog(df)

def summarize_final_cross_layer_catalog(df: pd.DataFrame) -> Dict:
    return {"count": len(df)}
