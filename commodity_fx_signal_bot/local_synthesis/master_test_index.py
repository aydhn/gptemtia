import pandas as pd
from typing import Tuple, Dict
from pathlib import Path
from .synthesis_config import LocalSynthesisProfile

def classify_test_family(path: Path, project_root: Path) -> str:
    return "unknown_family"





def build_master_test_index(project_root: Path, profile: LocalSynthesisProfile) -> Tuple[pd.DataFrame, Dict]:
    df = pd.DataFrame(columns=["item_id", "item_label", "relative_path", "family_label", "source_layer", "file_type", "size_bytes", "modified_at_utc", "status", "warnings"])
    return df, summarize_master_test_index(df)

def summarize_master_test_index(index_df: pd.DataFrame) -> Dict:
    return {"count": len(index_df), "note": "Not official audit inventory"}
