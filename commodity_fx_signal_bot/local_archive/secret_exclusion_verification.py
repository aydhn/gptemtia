import pandas as pd
from typing import Tuple, Dict
from .archive_config import LocalArchiveProfile

def build_secret_exclusion_verification_report(exclusion_df: pd.DataFrame, item_df: pd.DataFrame, profile: LocalArchiveProfile) -> Tuple[pd.DataFrame, Dict]:
    mismatches = []
    if not item_df.empty and 'item_status' in item_df.columns:
        cand_df = item_df[item_df['item_status'] == 'archive_candidate']
        for _, row in cand_df.iterrows():
            if ".env" in row['relative_path'].lower():
                mismatches.append({"relative_path": row['relative_path'], "expected_status": "archive_excluded"})
    df = pd.DataFrame(mismatches)
    return df, {"mismatches_found": len(df)}
