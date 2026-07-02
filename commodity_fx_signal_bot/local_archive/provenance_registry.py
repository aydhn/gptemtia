import pandas as pd
from typing import Tuple, Dict
from .archive_config import LocalArchiveProfile

def infer_archive_item_provenance(item_row: pd.Series) -> Dict:
    rel_path = item_row.get("relative_path", "")
    layer = "unknown"
    if "data/lake" in rel_path: layer = "storage"
    elif "reports/output" in rel_path: layer = "presentation"
    return {
        "item_id": item_row.get("item_id"),
        "relative_path": rel_path,
        "source_layer": layer
    }

def build_archive_provenance_registry(item_df: pd.DataFrame, profile: LocalArchiveProfile) -> Tuple[pd.DataFrame, Dict]:
    records = []
    if not item_df.empty and 'item_status' in item_df.columns:
        cand_df = item_df[item_df['item_status'] == 'archive_candidate']
        for _, row in cand_df.iterrows():
            records.append(infer_archive_item_provenance(row))
    df = pd.DataFrame(records)
    return df, {"total_records": len(df)}
