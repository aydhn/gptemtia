import pandas as pd
from typing import Tuple, Dict
from .archive_config import LocalArchiveProfile

def build_archive_gap_register(item_df: pd.DataFrame, snapshot_df: pd.DataFrame, manifest_index_df: pd.DataFrame, exclusion_df: pd.DataFrame, profile: LocalArchiveProfile) -> Tuple[pd.DataFrame, Dict]:
    gaps = []
    expected_domains = ["documentation_archive", "report_archive"]
    found = item_df['domain_label'].unique() if not item_df.empty and 'domain_label' in item_df.columns else []
    for d in expected_domains:
        if d not in found: gaps.append({"gap_type": "missing_domain", "description": d})
    if snapshot_df.empty: gaps.append({"gap_type": "missing_snapshot_catalog", "description": "missing"})
    if manifest_index_df.empty: gaps.append({"gap_type": "missing_cold_storage_manifest", "description": "missing"})
    df = pd.DataFrame(gaps)
    return df, {"total_gaps_identified": len(df)}
