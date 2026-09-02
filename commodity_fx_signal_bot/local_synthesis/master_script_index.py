import pandas as pd
from typing import Tuple, Dict
from pathlib import Path
from .synthesis_config import LocalSynthesisProfile

def classify_script_family(path: Path, project_root: Path) -> str:
    return "unknown_family"



def detect_forbidden_script_names(index_df: pd.DataFrame) -> pd.DataFrame: return index_df

def build_master_script_index(project_root: Path, profile: LocalSynthesisProfile) -> Tuple[pd.DataFrame, Dict]:
    df = pd.DataFrame(columns=["item_id", "item_label", "relative_path", "family_label", "source_layer", "file_type", "size_bytes", "modified_at_utc", "status", "warnings"])
    return df, summarize_master_script_index(df)

def summarize_master_script_index(index_df: pd.DataFrame) -> Dict:
    return {"count": len(index_df), "note": "Not official audit inventory"}
