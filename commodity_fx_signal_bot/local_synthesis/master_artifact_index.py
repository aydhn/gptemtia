import pandas as pd
from typing import Tuple, Dict
from pathlib import Path
from .synthesis_config import LocalSynthesisProfile

def classify_artifact_family(path: Path, project_root: Path) -> str:
    return "unknown_family"

def classify_artifact_status(path: Path, profile: LocalSynthesisProfile) -> str: return 'unknown'



def build_master_artifact_index(project_root: Path, family_df: pd.DataFrame, profile: LocalSynthesisProfile) -> Tuple[pd.DataFrame, Dict]:
    df = pd.DataFrame(columns=["item_id", "item_label", "relative_path", "family_label", "source_layer", "file_type", "size_bytes", "modified_at_utc", "status", "warnings"])
    return df, summarize_master_artifact_index(df)

def summarize_master_artifact_index(index_df: pd.DataFrame) -> Dict:
    return {"count": len(index_df), "note": "Not official audit inventory"}
