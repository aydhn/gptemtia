"""
Hash of Hashes Catalog.
"""
import pandas as pd
import hashlib
from local_archival.archival_config import LocalArchivalProfile

def compute_hash_of_hashes(hash_df: pd.DataFrame, profile: LocalArchivalProfile) -> dict:
    if hash_df is None or hash_df.empty:
        return {"hash_of_hashes": None}
    
    h = hashlib.new(profile.hash_algorithm)
    valid_hashes = hash_df[hash_df["hash_value"].notna()]["hash_value"].sort_values().tolist()
    for v in valid_hashes:
        h.update(str(v).encode('utf-8'))
    return {"hash_of_hashes": h.hexdigest()}

def build_final_hash_of_hashes_catalog(hash_df: pd.DataFrame, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    res = compute_hash_of_hashes(hash_df, profile)
    df = pd.DataFrame([{"hash_algorithm": profile.hash_algorithm, "hash_of_hashes": res["hash_of_hashes"]}])
    return df, summarize_hash_of_hashes_catalog(df)

def summarize_hash_of_hashes_catalog(hoh_df: pd.DataFrame) -> dict:
    return {"status": "computed" if hoh_df is not None and not hoh_df.empty else "empty"}
